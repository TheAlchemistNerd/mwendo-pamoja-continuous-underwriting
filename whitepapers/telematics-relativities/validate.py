import re

text = """
## Abstract

The transition from static pricing variables to high-frequency telematics in the gig economy presents a fundamental challenge for motor insurance underwriting today. While deep neural networks excel at extracting kinematic and environmental patterns from massive data streams, their raw outputs lack the interpretability, tariff neutrality, and regulatory transparency required by modern actuarial standards, such as the International Financial Reporting Standard 17 (IFRS 17). This paper introduces a comprehensive hybrid quantitative architecture that integrates explicit actuarial variables with residualised neural embeddings within a Hierarchical Bayesian framework. By formally separating claim frequency (utilizing a Negative Binomial distribution) and claim severity (employing a conditional Gamma distribution) and scaling them via exposure-normalised modulating variables, we ensure that telematics redistributes risk fairly without silently inflating the aggregate base tariff. Furthermore, we demonstrate that Hierarchical Bayes serves as a mathematically rigorous generalization of classical Bühlmann-Straub credibility, naturally addressing sparse data cohorts through the mechanism of partial pooling. Ultimately, this framework provides a continuous, theoretically sound, and transparent underwriting mechanism tailored for usage-based insurance (UBI) models.

## 1. Introduction

The rapid evolution of Usage-Based Insurance (UBI) has fundamentally altered the landscape of motor insurance, particularly within the rapidly expanding gig economy. Historically, actuaries relied on static rating factors, such as policyholder age, vehicle class, and geographic territory, to assign drivers to discrete and rigid tariff cells. These generalized linear model (GLM) frameworks provided long-term stability and high interpretability, satisfying stringent regulatory requirements for transparency and fairness [1]. However, in a modern gig-economy context, where drivers experience extreme volatility in working hours, urban congestion, and platform-driven incentive structures, static variables systematically fail to capture the true, dynamic risk profile of the individual policyholder. A driver traversing a hazardous urban corridor during peak surge pricing faces an entirely different risk environment than one operating in a quiet suburban zone, exposing the fundamental limitations of static models.

The advent of high-frequency telematics, incorporating GPS, accelerometer, and onboard diagnostic data, offers a profound observational advantage for risk assessors. Modern machine learning architectures, including Gradient Boosting Machines and deep neural networks, can ingest these massive, high-dimensional streams to detect complex, non-linear kinematic patterns such as hard braking, aggressive cornering rhythms, and driver fatigue [2]. Yet, despite their undeniable predictive power, the direct application of raw neural network outputs to insurance pricing is highly problematic for regulated markets. Unconstrained neural networks function as opaque black boxes, making it exceedingly difficult for actuaries to explain precisely how a specific driving event translates into a premium adjustment. This opacity directly violates a critical requirement under prevailing actuarial standards and consumer protection regulations [1]. Furthermore, deep learning models are inherently prone to causal confusion and the implicit double-counting of baseline exposure metrics.

To bridge this widening gap between predictive capability and regulatory compliance, this paper proposes a hybrid architecture that combines the predictive capacity of deep learning with the structural rigor of actuarial science. We introduce the concept of an exposure-normalised actuarial modulating variable. Rather than replacing the conventional tariff structure, the neural embedding is orthogonalized (residualised) against explicit actuarial features, ensuring it only captures incremental behavioral risk. The resulting metrics are subsequently fed into a Hierarchical Bayesian Logistic Regression engine. The objectives of this paper are threefold (1) to formally define the actuarial modulating variable with a strict separation of frequency and severity, (2) to demonstrate how Bayesian partial pooling extends classical credibility theory to resolve data sparsity in high-dimensional UBI portfolios, and (3) to ground the methodology in robust accounting and statistical principles, adhering strictly to IFRS 17 standards.
"""

paragraphs = text.strip().split('\n\n')
for i, p in enumerate(paragraphs):
    if p.startswith('##'):
        print(f"Header: {p}")
        continue
    words = len(re.findall(r'\b[\w-]+\b', p))
    print(f"Paragraph {i} word count: {words}")
    if not (130 <= words <= 160):
        print(f"WARNING: Paragraph {i} fails constraint! (Count: {words})")
    if '—' in p or '–' in p:
        print(f"WARNING: Paragraph {i} contains a dash!")
