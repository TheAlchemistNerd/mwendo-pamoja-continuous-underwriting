# Comprehensive Glossary: Gig-Economy Insurtech Architecture

This glossary aggregates all the specialized variables, economic concepts, and architectural components developed across Parts 1, 2a, 2b, and 3. While these concepts are explained within the text, they are not currently consolidated into a single reference document until now.

## 1. Economic & Domain Concepts (Parts 1 & 3)

*   **Correlated Default Cascade:** The phenomenon where a gig driver's default on a small microloan triggers a cascading inability to pay larger obligations (like vehicle leases or Insurance Premium Financing), ultimately forcing them offline entirely.
*   **Suffocation Threshold ($I_{\text{net}} < S$):** The critical boundary where a driver's net operational income falls below their minimum structural debt service requirements. Crossing this threshold guarantees a default cascade.
*   **Insurance Premium Financing (IPF):** A credit product that allows drivers to pay expensive annual insurance premiums in small daily/weekly installments, collateralized by the unearned premium.
*   **Algorithmic Redlining:** A statistical bias vulnerability where a neural network learns to penalize protected demographic groups by using geographic data (geohashes) or specific behaviors as proxies for race or income. Mitigated via **Equalized Odds** and **Maximum Mean Discrepancy (MMD)** regularization.
*   **ZEV Smart Fleet Routing:** A regulatory intervention where the platform routes Zero-Emission Vehicle (ZEV) drivers to areas overlapping with rapid-charging infrastructure, ensuring charging downtime coincides with demand lulls rather than peak surges.

## 2. Engineered Variables: The Neural Pipeline (Part 2a)

These variables are processed entirely within the Deep Learning pipeline to generate the driver's dynamic behavioral embedding.

*   **Wallet Cash-Flow Asymmetry (CFA):** The ratio of a driver's top 5% outlier surge earnings to their baseline rolling average. A high CFA indicates dangerous structural dependency on algorithmic windfalls rather than stable income.
*   **Earnings Velocity ($\nu_{\text{earn}}$):** The ratio of net earnings realized over the trailing 7 days compared to the driver's historical 90-day baseline. Declining velocity indicates cash-flow suffocation.
*   **Algorithmic Matching Elasticity:** A macroeconomic proxy measuring the localized density and availability of trip dispatches in a specific market. A severe drop indicates structural market deterioration.
*   **Circadian Fatigue Accumulation:** The integration of trailing hours driven during a driver's historical biological sleep window. Used by the GRU as a kinematic measure of behavioral desperation.

## 3. Engineered Variables: The Tabular Bypass (Parts 2a & 2b)

These variables intentionally *bypass* the neural network to avoid structural multicollinearity. They are routed directly to the Bayesian layer where they are modeled explicitly via B-Splines or linear interaction terms.

*   **Dynamic Debt-to-Liquidity Ratio (DLR):** Total short-term debt obligations divided by the 7-day rolling average net wallet balance. Modeled via explicit non-linear B-Splines.
*   **Repayment Velocity ($v_{\text{repay}}$):** Ratio of principal actually repaid to the contractually scheduled repayment. Modeled via explicit non-linear B-Splines.
*   **Explicit Interaction Set ($\mathcal{G}$):** Four specific pairwise interactions routed directly to the Bayesian layer:
    1.  High revolving utilization Ã,  Prior delinquency
    2.  Platform commission increase Ã,  High DLR
    3.  Late-night driving concentration Ã,  Microloan arrears
    4.  ZEV mandate deadline proximity Ã,  ICE vehicle ownership

## 4. Deep Learning & Data Architecture (Part 2a)

*   **Dual-Regime Neural Architecture:** The core predictive engine split into two temporal regimes: High-frequency telematics (GRU) and Low-frequency macro context (Transformer).
*   **Gated Recurrent Unit (GRU):** A sequential neural network that processes 14 days of daily telematics and wallet transactions to output a terminal hidden state ($\mathbf{h}_T^{\text{GRU}}$), representing the driver's latent "desperation profile".
*   **Multi-Head Self-Attention Transformer:** A parallel neural network that processes 24 months of macroeconomic and regulatory history to output a context vector ($\mathbf{c}_{L,\tau}$), representing the structural market regime.
*   **Cross-Attention Feature Fusion:** The mechanism that merges the GRU and Transformer outputs. The GRU state acts as the "Query" to dynamically weigh which macro "Keys/Values" from the Transformer are most relevant to the driver's current stress level.
*   **Point-in-Time Correctness:** An engineering guarantee (enforced via dual-timestamp Debezium CDC and Flink asynchronous joins) ensuring the model is never trained using data that wasn't actually available at the exact moment of the historical prediction, preventing look-ahead bias.

## 5. Bayesian & Probabilistic Architecture (Part 2b)

*   **Hierarchical Bayesian Logistic Regression:** The final underwriting engine. Instead of outputting a single credit score, it outputs a full posterior probability distribution of default, explicitly quantifying uncertainty.
*   **B-Splines:** Mathematical functions used to explicitly model non-linear relationships (e.g., the threshold effect of DLR) directly in the Bayesian layer without using a neural network.
*   **Hamiltonian Monte Carlo (HMC):** The advanced Markov Chain Monte Carlo sampling algorithm used to efficiently compute the Bayesian posterior distributions.
*   **Asymmetric Clayton Copula:** A statistical function used to link the default probabilities of different products (e.g., Microloan and IPF). It is "asymmetric" because it specifically captures *tail dependence* — meaning defaults are highly correlated during bad economic times, but weakly correlated during good times.

