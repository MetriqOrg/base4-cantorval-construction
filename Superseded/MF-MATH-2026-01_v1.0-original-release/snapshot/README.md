# Metriq Foundation research preprint source

**Title:** An Explicit Cantorval Achievement Set with Convergent Consecutive-Term Ratio  
**Identifier:** MF-MATH-2026-01  
**Version:** 1.0  
**Date:** 15 July 2026

## Build

Compile with LuaLaTeX from this directory:

```bash
latexmk -lualatex -interaction=nonstopmode -halt-on-error metriq_second_jones_preprint.tex
```

The source uses the included Metriq vector logo assets and the auto-generated `cantorval_intervals.tex` file. The interval graphic is mathematically generated from exact rational outer approximations of the constructed achievement set.

## Status

Candidate proof; not peer reviewed. Independent specialist verification is required before treating the claimed resolution as established.


## Reproducibility

Regenerate the exact interval figure:

```bash
python generate_intervals.py
```

Run finite exact-arithmetic consistency checks:

```bash
python verify_construction.py
```

The checker uses Python's rational arithmetic and is supplementary; the general proof is contained in the manuscript.
