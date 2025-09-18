# Workflow Guide

This guide provides step-by-step instructions for non-technical users to use the Cleavage Mapping Excel Pipeline.

## Quick Start

### Step 1: Open Template
Open `CleavagePipeline_Template.xlsx` from the `/excel/` folder.

### Step 2: Paste Raw Data
Paste your CSV data into the appropriate Raw sheets:
- `Raw_100` for 100 mgd concentration data
- `Raw_200` for 200 mgd concentration data  
- `Raw_500` for 500 mgd concentration data

### Step 3: View Results
The Calc sheets will auto-update with processed results:
- Left-anchored cleavage tables
- Right-anchored cleavage tables
- Residue analysis and percentages

## Detailed Instructions

### Data Format Requirements

Your CSV data should contain protein sequences in this format:
```
(LEFT_RESIDUE)CORE_PEPTIDE(RIGHT_RESIDUE)
```

**Examples:**
- `(E)AEDLQVGQVELGGGPGAGSLQ(P)` 
- `(K)RQLEQVGQVELGGGPGAGSLQPLA(L)`
- `(D)LQVGQVELGGGPGAGSLQ(P)`

### Step-by-Step Workflow

#### 1. Prepare Your Data
- Ensure your CSV files have the correct column headers:
  - Column A: `#` (row numbers)
  - Column B: `Sequence` (protein sequences with cleavage indicators)
  - Columns C-I: Function data (`Han_StemCells_[concentration]mgdl_Glucose_AspN_Fxn2` through `Fxn8`)

#### 2. Import Data to Raw Sheets
1. Open the Excel template
2. Navigate to the appropriate Raw sheet (`Raw_100`, `Raw_200`, or `Raw_500`)
3. Copy your CSV data (including headers)
4. Paste into cell A1 of the Raw sheet
5. Repeat for each concentration dataset

#### 3. Review Calculated Results
Navigate to the corresponding Calc sheets to view processed results:

**Core Analysis (Columns A-I):**
- **Sequence**: Original protein sequence
- **LeftResidue**: Extracted left cleavage residue (e.g., "E" from "(E)PEPTIDE(P)")
- **RightResidue**: Extracted right cleavage residue (e.g., "P" from "(E)PEPTIDE(P)")
- **CorePeptide**: Core peptide sequence (e.g., "PEPTIDE" from "(E)PEPTIDE(P)")
- **Left_Sum**: Sum of all function values (Fxn2-Fxn8)
- **Right_Sum**: Reserved for future Right function data (currently 0)
- **Total_Sum**: Left_Sum + Right_Sum
- **Left_Percentage**: Percentage of total represented by Left functions
- **Right_Percentage**: Percentage of total represented by Right functions

**Dynamic Output Tables (Columns K-S):**
- **Left-Anchored Table** (Columns K-N): Data grouped by Left Residue
- **Right-Anchored Table** (Columns P-S): Data grouped by Right Residue

#### 4. Interpret Results

**Left-Anchored Analysis:**
Use this view to analyze cleavage patterns based on the amino acid residue on the left side of the cleavage site. This helps identify:
- Which left residues are most common in your dataset
- Function value distributions for each left residue type
- Core peptide sequences associated with specific left residues

**Right-Anchored Analysis:**
Use this view to analyze cleavage patterns based on the amino acid residue on the right side of the cleavage site. This helps identify:
- Which right residues are most common in your dataset  
- Function value distributions for each right residue type
- Core peptide sequences associated with specific right residues

### Using Sample Data

Test the pipeline with the provided sample files:
1. Navigate to the `/data/` folder
2. Open `sample_100mgd.csv`, `sample_200mgd.csv`, or `sample_500mgd.csv`
3. Copy the data and paste into the corresponding Raw sheet
4. Observe the automatic calculations in the Calc sheets

### Expected Results with Sample Data

For the sample sequence `(E)AEDLQVGQVELGGGPGAGSLQ(P)`:
- **LeftResidue**: E
- **RightResidue**: P  
- **CorePeptide**: AEDLQVGQVELGGGPGAGSLQ
- **Left_Sum**: Sum of function values from columns C-I
- **Left_Percentage**: 100% (since Right_Sum = 0 in current version)

## Troubleshooting

### Common Issues

**Problem**: Formulas show as text instead of calculating
**Solution**: Ensure Excel is set to automatically calculate formulas (File → Options → Formulas → Automatic)

**Problem**: #VALUE! errors in residue extraction columns
**Solution**: Check that your sequences follow the exact format `(LEFT)CORE(RIGHT)` with parentheses

**Problem**: Zero sums in function columns
**Solution**: Verify that your function data (columns C-I) contains numeric values, not text

**Problem**: Dynamic tables show #SPILL! error
**Solution**: Ensure columns K-S have sufficient empty space for the filtered results

### Data Validation

Before using your own data, verify:
1. ✅ Sequences contain exactly two sets of parentheses
2. ✅ Function columns contain numeric values
3. ✅ Headers match the expected format
4. ✅ No extra spaces or special characters in critical columns

### Performance Notes

- The template is optimized for datasets up to 100 rows per sheet
- For larger datasets, consider splitting into multiple files
- Complex formulas may recalculate slowly on older Excel versions
- Use Excel Office 365 or Excel 2021+ for best performance with dynamic arrays

---

*For technical details about the formulas used, see [`docs/FORMULAS.md`](FORMULAS.md)*