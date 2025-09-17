# Excel Formulas Reference

This document provides technical reference for all Excel formulas used in the Cleavage Mapping Pipeline.

## Overview
The pipeline uses formula-only automation (no VBA) to process protein sequence data with Left/Right cleavage anchor points.

## Excel Template Structure

### Raw Sheets (`Raw_100`, `Raw_200`, `Raw_500`)
Each Raw sheet contains the following columns:
- **Column A**: `#` (Row numbers from source data)
- **Column B**: `Sequence` (Protein sequences with cleavage indicators in parentheses)
- **Columns C-I**: Function data (`Han_StemCells_[concentration]mgdl_Glucose_AspN_Fxn2` through `Fxn8`)

### Calc Sheets (`Calc_100`, `Calc_200`, `Calc_500`)
Each Calc sheet contains the following columns:
- **Column A**: `Sequence` (Processed sequence data)
- **Column B**: `LeftResidue` (Extracted left cleavage residue)
- **Column C**: `RightResidue` (Extracted right cleavage residue)  
- **Column D**: `CorePeptide` (Core peptide sequence)
- **Column E**: `Left_Sum` (Sum of Left function values)
- **Column F**: `Right_Sum` (Sum of Right function values)
- **Column G**: `Total_Sum` (Left + Right totals)
- **Column H**: `Left_Percentage` (Left percentage of total)
- **Column I**: `Right_Percentage` (Right percentage of total)

## Core Formulas

### Residue Parsing
*Formulas to extract LeftResidue and RightResidue from sequence data will be documented here.*

### Dynamic Array Outputs
*SORTBY + HSTACK + FILTER formulas for Left-anchored and Right-anchored tables will be documented here.*

### Header-Driven Logic
*Optional BYCOL + MASK formulas to detect .1 suffix for Right block auto-detection will be documented here.*

---

*This document will be populated with detailed formulas in subsequent tasks.*