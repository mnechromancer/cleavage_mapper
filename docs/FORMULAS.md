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

## Data Format Understanding

### Sequence Format
Protein sequences in the data follow this pattern:
```
(LEFT_RESIDUE)CORE_PEPTIDE(RIGHT_RESIDUE)
```

**Example**: `(E)AEDLQVGQVELGGGPGAGSLQ(P)`
- **Left Residue**: E
- **Core Peptide**: AEDLQVGQVELGGGPGAGSLQ
- **Right Residue**: P

## Core Formulas

### 1. Sequence Reference (Column A)
**Purpose**: Copy sequence data from Raw sheet to Calc sheet  
**Formula**: `=Raw_100!B2`  
**Usage**: Place in Calc_100!A2, adjust sheet name for other concentrations  

### 2. Left Residue Extraction (Column B)
**Purpose**: Extract the first amino acid residue in parentheses  
**Formula**: 
```excel
=IF(ISERROR(FIND("(",A2)),"",MID(A2,FIND("(",A2)+1,FIND(")",A2)-FIND("(",A2)-1))
```
**Explanation**:
- `FIND("(",A2)` - Locates position of first opening parenthesis
- `MID()` - Extracts text between first ( and first )
- `IF(ISERROR())` - Returns empty string if no parentheses found

**Example**: For `(E)AEDLQVGQVELGGGPGAGSLQ(P)` → Returns `E`

### 3. Right Residue Extraction (Column C)
**Purpose**: Extract the second amino acid residue in parentheses  
**Formula**: 
```excel
=IF(LEN(A2)-LEN(SUBSTITUTE(A2,"(",""))<2,"",MID(A2,FIND("(",SUBSTITUTE(A2,"(","♦",LEN(A2)-LEN(SUBSTITUTE(A2,"(",""))-1))+1,FIND(")",A2,FIND("(",SUBSTITUTE(A2,"(","♦",LEN(A2)-LEN(SUBSTITUTE(A2,"(",""))-1)))-FIND("(",SUBSTITUTE(A2,"(","♦",LEN(A2)-LEN(SUBSTITUTE(A2,"(",""))-1))-1))
```
**Explanation**:
- Uses SUBSTITUTE with marker (♦) to find second occurrence of (
- Counts parentheses to ensure there are at least 2
- Extracts text between second ( and corresponding )

**Example**: For `(E)AEDLQVGQVELGGGPGAGSLQ(P)` → Returns `P`

### 4. Core Peptide Extraction (Column D)
**Purpose**: Extract the main peptide sequence between residues  
**Formula**: 
```excel
=IF(OR(ISERROR(FIND(")",A2)),LEN(A2)-LEN(SUBSTITUTE(A2,"(",""))<2),"",MID(A2,FIND(")",A2)+1,FIND("(",SUBSTITUTE(A2,"(","♦",LEN(A2)-LEN(SUBSTITUTE(A2,"(",""))-1))-FIND(")",A2)-1))
```
**Explanation**:
- Finds position after first )
- Finds position of second (
- Extracts text between these positions

**Example**: For `(E)AEDLQVGQVELGGGPGAGSLQ(P)` → Returns `AEDLQVGQVELGGGPGAGSLQ`

### 5. Left Sum Calculation (Column E)
**Purpose**: Sum all function values for left-side analysis  
**Formula**: `=SUM(Raw_100!C2:I2)`  
**Usage**: Sums columns C through I from corresponding Raw sheet row  

### 6. Right Sum Calculation (Column F)
**Purpose**: Sum all function values for right-side analysis  
**Formula**: `=0`  
**Note**: Currently set to 0 since sample data doesn't have separate right function columns  

### 7. Total Sum Calculation (Column G)
**Purpose**: Calculate total intensity across all functions  
**Formula**: `=E2+F2`  
**Usage**: Adds Left_Sum + Right_Sum  

### 8. Left Percentage (Column H)
**Purpose**: Calculate percentage of total intensity from left functions  
**Formula**: `=IF(G2=0,0,E2/G2*100)`  
**Explanation**:
- Checks for division by zero
- Returns (Left_Sum / Total_Sum) * 100

### 9. Right Percentage (Column I)
**Purpose**: Calculate percentage of total intensity from right functions  
**Formula**: `=IF(G2=0,0,F2/G2*100)`  
**Explanation**:
- Checks for division by zero  
- Returns (Right_Sum / Total_Sum) * 100

## Dynamic Array Outputs

### Left-Anchored Cleavage Table
**Purpose**: Create sortable table grouped by Left Residue  
**Location**: Columns K-N in Calc sheets  
**Formula**: `=FILTER(B2:E100,(B2:B100<>"")*(E2:E100>0))`  
**Explanation**: Filters data where LeftResidue exists and Left_Sum > 0

### Right-Anchored Cleavage Table  
**Purpose**: Create sortable table grouped by Right Residue  
**Location**: Columns P-S in Calc sheets  
**Formula**: `=FILTER(C2:E100,(C2:C100<>"")*(E2:E100>0))`  
**Explanation**: Filters data where RightResidue exists and Left_Sum > 0

## Advanced Formulas (Optional)

### Header-Driven Function Detection
**Purpose**: Automatically detect Left vs Right function columns by header suffix  
**Formula Concept**: 
```excel
=BYCOL(Raw_100!C1:I1,LAMBDA(col,IF(RIGHT(col,2)=".1","Right","Left")))
```
**Usage**: Could be used to automatically separate Left/Right functions if data structure changes

## Implementation Notes

### Formula Copying
- All formulas are designed to be copy-pasteable down rows
- Sheet references (e.g., `Raw_100!`) need manual adjustment for different concentrations
- Cell references are relative and will adjust automatically when copied

### Error Handling
- All formulas include error checking with `IF(ISERROR())`
- Division by zero is prevented in percentage calculations
- Empty string returns for missing data

### Performance Considerations
- Formulas use standard Excel functions for maximum compatibility
- Complex nested formulas may recalculate slowly with large datasets
- Consider using helper columns for very complex parsing if performance becomes an issue

## Testing the Formulas

### Sample Data
The template includes sample data to test formulas:
- Row 2: `(E)AEDLQVGQVELGGGPGAGSLQ(P)` with sample function values
- Row 3: `(E)DLQVGQVELGGGPGAGSLQ(P)` with sample function values

### Expected Results
For sample sequence `(E)AEDLQVGQVELGGGPGAGSLQ(P)`:
- **LeftResidue**: E
- **RightResidue**: P  
- **CorePeptide**: AEDLQVGQVELGGGPGAGSLQ
- **Left_Sum**: Sum of function values (C2:I2)
- **Left_Percentage**: 100% (since Right_Sum = 0)

---

*This formula reference enables complete automation of the cleavage mapping pipeline using only Excel's built-in functions.*