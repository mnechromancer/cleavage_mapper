# Cleavage Mapping Excel Pipeline - AI Coding Instructions

## Project Overview
This project builds an **Excel-only cleavage mapping pipeline** for bioinformatics data processing. The core philosophy is formula-driven automation without VBA or external scripts, focusing on protein sequence analysis with Left/Right cleavage anchor points.

## Key Architecture Principles

### Excel-First Design
- **No VBA or external scripts** - Pure Excel formulas only
- **Template-based workflow** - `CleavagePipeline_Template.xlsx` as the main deliverable
- **Multi-sheet structure**: Raw data input sheets (`Raw_100`, `Raw_200`, `Raw_500`) → Calculation sheets (`Calc_100`, `Calc_200`, `Calc_500`) → Dynamic output tables

### Data Flow Pattern
```
Raw CSV Data → Raw Sheets (paste) → Calc Sheets (formulas) → Left/Right-anchored Views (dynamic arrays)
```

## Critical Project Conventions

### Sheet Naming Convention
- **Raw sheets**: `Raw_100`, `Raw_200`, `Raw_500` (mgd concentrations)
- **Calc sheets**: `Calc_100`, `Calc_200`, `Calc_500` (formula processing)
- **Headers**: `Sequence`, Left functions (`Fxn2`-`Fxn8`), Right functions (`Fxn2.1`-`Fxn8.1`)

### Formula Strategy
- **Residue parsing**: Extract LeftResidue/RightResidue from sequence data
- **Dynamic arrays**: Use `SORTBY + HSTACK + FILTER` for output tables
- **Header-driven logic**: Optional `BYCOL + MASK` to detect `.1` suffix for Right block auto-detection
- **Two output modes**: Left-anchored and Right-anchored cleavage tables

### Repository Structure (Target)
```
/excel/          # Template workbooks
/docs/           # FORMULAS.md, WORKFLOW.md
/data/           # Sample CSV files for testing
tracking/        # Project management (backlog)
```

## Development Workflow

### File Creation Priority
1. **Excel template** (`CleavagePipeline_Template.xlsx`) - Core deliverable
2. **Formula documentation** (`/docs/FORMULAS.md`) - Technical reference
3. **User workflow** (`/docs/WORKFLOW.md`) - Non-technical usage guide
4. **Sample data** (`/data/` with 100/200/500 mgd CSVs)

### Formula Development Approach
- Start with hard-coded ranges, then evolve to header-driven formulas
- Document both simple and advanced variants in `FORMULAS.md`
- Test with sample data that represents real bioinformatics input patterns
- Ensure formulas work with copy-paste CSV data (no import wizards)

## External Dependencies
- **Target Excel version**: Modern Excel with dynamic array support (`FILTER`, `SORTBY`, `HSTACK`)
- **Input format**: CSV files with protein sequence data
- **No external libraries** - Pure Office 365/Excel functionality only

## Testing Strategy
- Create minimal sample CSVs (2-3 rows each) for quick validation
- Verify formulas auto-update when raw data is pasted
- Test both Left-anchored and Right-anchored output generation
- Ensure template works for non-technical bioinformatics users

## Key Files to Reference
- `tracking/cleavage_pipeline_backlog.md` - Complete project roadmap and task breakdown
- Future: `/docs/FORMULAS.md` - Technical formula specifications
- Future: `/docs/WORKFLOW.md` - End-user instructions

## Project-Specific Notes
- This is a **greenfield project** - currently only contains planning documents
- Focus on **formula documentation** alongside Excel template creation
- **End-user experience** is critical - bioinformatics researchers, not Excel experts
- **No programming languages** - This is purely an Excel automation project