# Low-Level Hardware & Theoretical Underpinnings of Bayesian Priors

*Note: While the production underwriting engine relies on XLA-compiled JAX (BlackJAX/NumPyro) for high-level tensor operations, this document serves to preserve the deep mathematical derivations and bare-metal hardware physics that govern those abstractions.*

---

## Part 1: Mathematical Foundations of the Heavy-Tailed Priors

### 1. The Half-Cauchy as the Extreme Boundary Case
The Half-Cauchy distribution is often referenced in Bayesian literature as the optimal prior for sparse, heavy-tailed variance parameters. However, it is not an independent phenomenon; it is mathematically derived as the extreme boundary case of the **Half-Student T** family, specifically when the degrees of freedom ($\nu$) collapses to exactly 1.

#### Deriving Half-Cauchy from Half-Student T
The generalized Probability Density Function (PDF) for a Half-Student T distribution with degrees of freedom $\nu > 0$ and scale parameter $\gamma > 0$ is:

$$f(x; \nu, \gamma) = \frac{2}{\gamma} \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right) \sqrt{\nu\pi}} \left( 1 + \frac{1}{\nu}\left(\frac{x}{\gamma}\right)^2 \right)^{-\frac{\nu+1}{2}}$$

By substituting $\nu = 1$, we evaluate the behavior at a single degree of freedom:

$$f(x; 1, \gamma) = \frac{2}{\gamma} \frac{\Gamma\left(\frac{1+1}{2}\right)}{\Gamma\left(\frac{1}{2}\right) \sqrt{1 \cdot \pi}} \left( 1 + \frac{1}{1}\left(\frac{x}{\gamma}\right)^2 \right)^{-\frac{1+1}{2}}$$

Using the known properties of the Gamma function ($\Gamma(1) = 1$ and $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$):

$$f(x; 1, \gamma) = \frac{2}{\gamma} \cdot \frac{1}{\pi} \left( 1 + \left(\frac{x}{\gamma}\right)^2 \right)^{-\frac{2}{2}}$$

The exponent reduces to $-1$, dropping the expression into the denominator to form the standard Half-Cauchy PDF:

$$f(x; 1, \gamma) = \frac{2}{\pi \gamma \left[ 1 + \left(\frac{x}{\gamma}\right)^2 \right]}$$

### 2. The Gamma Recurrence Relation
The Gamma function $\Gamma(z)$ is fundamentally defined by the recurrence relation: $\Gamma(z+1) = z \cdot \Gamma(z)$.
Because the Student-T PDF relies on evaluating $\Gamma\left(\frac{\nu+1}{2}\right)$ and $\Gamma\left(\frac{\nu}{2}\right)$, stepping the degrees of freedom triggers this recurrence relation, splitting the mathematics into two distinct tracks:

*   **Base Case A: Odd Degrees of Freedom ($\nu = 1, 3, 5 \dots$)**
    The absolute bottom of this recurrence track is **$\nu=1$ (The Half-Cauchy)**. Its integral evaluates to an arctangent function ($\arctan(x)$). Thus, any odd degree of freedom (such as $\nu=3$) inherits this foundational trigonometric geometry.
*   **Base Case B: Even Degrees of Freedom ($\nu = 2, 4, 6 \dots$)**
    The absolute bottom of this track is **$\nu=2$**. Its integral evaluates to a purely algebraic square root function ($\frac{x}{\sqrt{2+x^2}}$), avoiding trigonometry entirely.

Setting $\nu=3$ strategically starts the model at the Cauchy base to guarantee robustness to extreme gig-economy shocks, but steps forward through the recurrence relation just enough times to reign in the infinite variance and prevent MCMC sampler divergence.

---

## Part 2: Bare-Metal Hardware Acceleration (SIMD & AVX-512)

Evaluating these heavy-tailed Bayesian priors is computationally expensive during Hamiltonian Monte Carlo (HMC) sampling, requiring probabilities to be calculated across thousands of leapfrog steps. While JAX handles this via XLA, at the hardware level, this relies heavily on **AVX-512 (Advanced Vector Extensions)**.

AVX-512 provides 512-bit wide registers. Since a standard single-precision float is 32 bits, a single AVX-512 instruction processes **16 parameters simultaneously** in a single CPU clock cycle. 

### 1. Vectorizing the Half-Cauchy ($\nu=1$)
Because the Half-Cauchy is purely algebraic (no square roots or complex exponents), it is incredibly fast to vectorize.

```cpp
#include <immintrin.h>

// Computes Half-Cauchy PDF for an array of 16-byte aligned floats
void half_cauchy_pdf_avx512(const float* x, float gamma, float* out, size_t n) {
    float pi = 3.14159265359f;
    float num_const = (2.0f * gamma) / pi;
    float gamma_sq_const = gamma * gamma;

    __m512 v_num = _mm512_set1_ps(num_const);
    __m512 v_gamma_sq = _mm512_set1_ps(gamma_sq_const);

    for (size_t i = 0; i + 15 < n; i += 16) {
        __m512 v_x = _mm512_loadu_ps(&x[i]);
        __m512 v_x_sq = _mm512_mul_ps(v_x, v_x);                 // x^2
        __m512 v_den = _mm512_add_ps(v_x_sq, v_gamma_sq);        // x^2 + gamma^2
        __m512 v_pdf = _mm512_div_ps(v_num, v_den);              // Numerator / Denominator
        
        _mm512_storeu_ps(&out[i], v_pdf);
    }
}
```

### 2. Vectorizing the Half-Student T ($\nu=3$)
For $\nu=3$, the fractional exponent $-\frac{3+1}{2}$ cleanly becomes $-2$. This allows the use of highly efficient **Fused Multiply-Add (FMA)** instructions, avoiding `pow()` or `exp()` entirely.

```cpp
void half_student_t_v3_avx512(const float* x, float gamma, float* out, size_t n) {
    float k_const = 1.0f / (3.0f * gamma * gamma);
    float c_const = 0.36755f / gamma; 

    __m512 v_k = _mm512_set1_ps(k_const);
    __m512 v_c = _mm512_set1_ps(c_const);
    __m512 v_one = _mm512_set1_ps(1.0f);

    for (size_t i = 0; i + 15 < n; i += 16) {
        __m512 v_x = _mm512_loadu_ps(&x[i]);
        __m512 v_x_sq = _mm512_mul_ps(v_x, v_x);

        // FMA: Computes (v_x_sq * v_k) + 1.0 in a SINGLE instruction
        __m512 v_base = _mm512_fmadd_ps(v_x_sq, v_k, v_one);
        __m512 v_den = _mm512_mul_ps(v_base, v_base);            // (1 + k*x^2)^2
        __m512 v_pdf = _mm512_div_ps(v_c, v_den);                // Final division
        
        _mm512_storeu_ps(&out[i], v_pdf);
    }
}
```

### 3. The Paradigm Shift: SIMD Intrinsics vs. C99 High-Level Primitives
Writing raw SIMD via AVX-512 intrinsics is fundamentally different from writing high-level C99 scalar loops:

1.  **Bypassing the Auto-Vectorizer:** Compilers are conservative. If they suspect memory aliasing or strict IEEE compliance issues, they will refuse to vectorize a standard `for` loop. Intrinsics force the hardware to execute the specific assembly instructions (like `vaddps`).
2.  **The Death of the `if/else` Branch:** Branching (`if x > 0`) destroys pipeline efficiency in SIMD. Instead, AVX-512 relies on **Masking** (using `_mm512_cmp_ps_mask`). Math is executed on all 16 lanes simultaneously, and a 16-bit hardware mask determines which lanes are saved to memory.
3.  **Strict Memory Alignment:** AVX-512 demands that memory blocks be explicitly aligned to 64-byte boundaries. Attempting a strict load (`_mm512_load_ps`) on unaligned memory triggers an immediate hardware segmentation fault.

### 4. Hardware Architectures: AMD EPYC Zen 4 vs. Intel
Modern cloud deployments (like AWS EC2 `m7a` or GCP `c3d` instances) rely heavily on AMD EPYC architectures. While older Zen 2 and Zen 3 architectures were limited to AVX2 (256-bit), the **Zen 4 architecture (EPYC Genoa)** introduced full AVX-512 support with a unique hardware twist:

*   **Double-Pumped 256-bit Datapath:** Unlike Intel's massive, power-hungry true 512-bit silicon (which suffered from severe thermal throttling), AMD processes AVX-512 instructions by splitting them into two 256-bit chunks over two clock cycles.
*   **The Hardware Win:** Despite taking two cycles, this prevents the massive clock-speed drops seen on Intel chips. Furthermore, it unlocks the **32 massive 512-bit registers** and the dedicated hardware masking features (`k0` to `k7`), providing near-perfect branchless tensor execution for advanced machine learning pipelines.
