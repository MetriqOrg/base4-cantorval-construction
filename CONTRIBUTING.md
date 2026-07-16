# Contributing to Metriq PRISM Laboratory Research

PRISM welcomes rigorous mathematical review, reproducibility work, corrections, and relevant prior-art identification.

## Appropriate contributions

Contributions may include:

- proof audits tied to exact theorem, lemma, equation, or page references;
- counterexamples or demonstrations that a hypothesis is insufficient;
- independent implementations of computational checks;
- corrected derivations or simplified proofs;
- bibliographic corrections and relevant prior art;
- build fixes that do not alter mathematical content;
- accessibility and typesetting corrections.

General praise, unsupported declarations that a proof is correct, and purely stylistic rewrites are not substitutes for mathematical review.

## Before opening a pull request

1. Open an issue describing the proposed change.
2. Identify the affected paper, version, and exact location.
3. Separate mathematical changes from editorial or build changes.
4. Include a minimal reproducible example for computational issues.
5. State whether you have any conflict of interest or prior involvement with the work.

## Mathematical corrections

A proposed mathematical correction should contain:

- the precise claim being challenged;
- the reason the existing argument fails or is incomplete;
- a corrected statement or proof, when available;
- the effect on downstream results;
- references or independently checkable computations supporting the correction.

Do not silently revise a theorem or proof. Material changes require a new paper version and changelog entry.

## Computational contributions

Verification code should:

- use exact arithmetic where feasible;
- document software and runtime requirements;
- avoid network dependencies during verification;
- produce deterministic output or document all randomness;
- include tests for boundary and degenerate cases;
- state exactly what the computation proves and what it does not prove.

## Pull-request review

Metriq Foundation retains editorial control over PRISM publications. Acceptance of a contribution does not imply endorsement of unrelated claims by the contributor.

Contributors whose work materially changes a paper will be credited in the paper, changelog, acknowledgments, or repository history as appropriate. AI systems are not credited as authors.

## Conduct

Criticism may be direct and technically severe, but it must remain focused on the mathematics, evidence, attribution, or reproducibility. Harassment, impersonation, threats, and knowingly fabricated evidence are not permitted.
