# Quality-control report

**Canonical papers:** 7<br>
**Total PDF pages:** 75<br>
**Release date:** 16 July 2026

## PDF checks

- All seven PDFs open successfully, are unencrypted, contain extractable text, and have no XFA form content.
- All fonts reported by `pdffonts` are embedded; some are deliberately not subset because they originate in vector figures.
- Both Poppler and PDFium rendered every page. Side-by-side review found no renderer-specific missing content, clipping, broken glyphs, or legacy-brand residue.
- Covers, first manuscript pages, figures, disclaimers, references, and final-page footers were inspected page by page.

## Reproducibility-package checks

- Every verification script was rerun from the cleaned package and completed successfully.
- Every source package was rebuilt with LuaLaTeX. At 96 dpi, each rebuilt PDF was visually pixel-identical to the corresponding release PDF.
- CFF metadata parses as YAML; package manifests and SHA-256 checksums were regenerated after final cleanup.
- No font files are included.

## Disclaimer checks

- MF-MATH-2026-01: source disclaimer match=True; PDF phrase check=True; rebuild changed pages=0.
- MF-MATH-2026-02: source disclaimer match=True; PDF phrase check=True; rebuild changed pages=0.
- MF-MATH-2026-03: source disclaimer match=True; PDF phrase check=True; rebuild changed pages=0.
- MF-MATH-2026-04: source disclaimer match=True; PDF phrase check=True; rebuild changed pages=0.
- MF-MATH-2026-05: source disclaimer match=True; PDF phrase check=True; rebuild changed pages=0.
- MF-MATH-2026-06: source disclaimer match=True; PDF phrase check=True; rebuild changed pages=0.
- MF-MATH-2026-08: source disclaimer match=True; PDF phrase check=True; rebuild changed pages=0.

## Scope limitation

These checks establish release integrity and reproducibility of the packaged files. They do not constitute independent peer review, validate novelty or priority, or replace mathematical examination of the candidate proofs.

## Repository integration verification

- All seven canonical paper-level checksum files validate their release PDFs, cover images, and source packages.
- All canonical PDFs open successfully, are unencrypted, and match the page counts recorded in `CATALOG.md` and `CATALOG.json`.
- All canonical and superseded source ZIP files pass archive-integrity testing.
- Local Markdown links resolve, `CATALOG.json` parses as JSON, and `CITATION.cff` parses as YAML.
- `Superseded/MF-MATH-2026-01_v1.0-original-release/snapshot/` is byte-for-byte identical to the repository's `v1.0.0` tag.
- The original tag contains a pre-existing checksum mismatch for `TRADEMARKS.md`; the tagged files are retained unchanged and the recorded and actual hashes are documented in that snapshot's parent README.
