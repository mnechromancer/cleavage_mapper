# Backlog: Cleavage Mapping Excel Pipeline

This backlog is intended for GitHub Copilot (or any AI agent) to bootstrap and iterate on the **Excel-based cleavage mapping pipeline** project. It focuses on formula‑only automation, repo structure, and documentation.

---

## Milestone v0.1 – Project Setup

### Task 1: Repo Bootstrap ✅ COMPLETED
- **Description:** Create initial repository structure.
- **Deliverables:**
  - `/excel/` folder with placeholder template workbook ✅
  - `/docs/` folder with `FORMULAS.md` and `WORKFLOW.md` ✅
  - `/data/` folder with sample raw CSVs for 100/200/500 mgd ✅
  - `.gitignore` with Office temp + OS junk ✅
  - `README.md` with overview and quick start ✅
  - `LICENSE` (MIT) ✅
- **Acceptance Criteria:** Repo builds cleanly; file structure is present; README renders correctly. ✅

### Task 2: Excel Template – Raw Sheets ✅ COMPLETED
- **Description:** Add workbook `CleavagePipeline_Template.xlsx` with sheets `Raw_100`, `Raw_200`, `Raw_500`.
- **Details:** Each raw sheet should have headers: `Sequence`, contiguous block of Left Fxn2–Fxn8, contiguous block of Right Fxn2.1–Fxn8.1.
- **Acceptance Criteria:** Template workbook opens; each Raw sheet has headers only, no data. ✅
- **Implementation Notes:** Created Raw sheets with actual data structure from sample files: # column, Sequence column, and Han_StemCells_[concentration]mgdl_Glucose_AspN_Fxn2-8 columns.

### Task 3: Excel Template – Calc Sheets ✅ COMPLETED
- **Description:** Add sheets `Calc_100`, `Calc_200`, `Calc_500` with columns:
  - Sequence ✅
  - LeftResidue ✅
  - RightResidue ✅
  - CorePeptide ✅
  - Left_Sum, Right_Sum, Total_Sum ✅
  - Left_Percentage, Right_Percentage ✅
- **Acceptance Criteria:** Calc sheets exist; formulas are documented in `/docs/FORMULAS.md`. ✅

### Task 4: Docs – Formula Reference ✅ COMPLETED
- **Description:** Document drop‑in formulas for residues, sums, percentages, and dynamic array outputs (Left‑anchored and Right‑anchored tables).
- **Acceptance Criteria:** `FORMULAS.md` includes: ✅
  - Residue parsing formulas ✅
  - Left/Right sums ✅
  - sum + percentage ✅
  - Dynamic view formulas (`SORTBY + HSTACK + FILTER`) ✅
- **Implementation Notes:** Complete Excel formula reference with 9 core formulas, error handling, and dynamic array outputs. All formulas tested with sample data.

### Task 5: Docs – Workflow
- **Description:** Write step‑by‑step usage doc for non‑technical users.
- **Acceptance Criteria:** `WORKFLOW.md` explains:
  - How to paste raw data into Raw sheets
  - How Calc auto‑updates
  - Where to find Left‑anchored vs Right‑anchored outputs

---

## Milestone v0.2 – Enhancements

### Task 6: Header‑Driven Summation
- **Description:** Implement optional formulas using `BYCOL + MASK` to detect `.1` suffix for Right block.
- **Acceptance Criteria:** `FORMULAS.md` contains a second variant that removes need for hard‑coded ranges.

### Task 7: Sample Data
- **Description:** Add small sample CSVs for Raw 100/200/500 mgd with 2–3 fake rows.
- **Acceptance Criteria:** Users can import these into the template and see the pipeline produce outputs.

### Task 8: CI/Validation
- **Description:** Add a GitHub Actions workflow to check repo integrity (lint Markdown, ensure sample CSVs exist, etc.).
- **Acceptance Criteria:** Actions run green on every push.

---

## Milestone v1.0 – Release

### Task 9: Publish Starter Release
- **Description:** Tag `v1.0.0` with template, formulas, and docs.
- **Acceptance Criteria:** Users can download `CleavagePipeline_Template.xlsx`, paste their data, and immediately get Left‑anchored and Right‑anchored cleavage tables.

---

## Future Ideas
- Optional Office Script for one‑button refresh.
- Visual QA (conditional formatting for %Left, totals check).
- Extend template to >2 anchor types (if more than Left/Right needed).

