#!/usr/bin/env python3
"""
Cleavage Mapping Pipeline Processor
Processes raw cleavage data according to the Excel formulas defined in FORMULAS.md
"""

import pandas as pd
import re
import numpy as np

def extract_right_residue(sequence):
    """Extract right residue from sequence format like 'PEPTIDE(K)'"""
    if pd.isna(sequence) or sequence.strip() == '':
        return ''
    
    # Find the last occurrence of parentheses
    match = re.search(r'\(([A-Z])\)$', str(sequence).strip())
    if match:
        return match.group(1)
    return ''

def extract_core_peptide(sequence):
    """Extract core peptide by removing the right residue in parentheses"""
    if pd.isna(sequence) or sequence.strip() == '':
        return ''
    
    # Remove the trailing (X) pattern
    core = re.sub(r'\([A-Z]\)$', '', str(sequence).strip())
    return core

def process_cleavage_data(csv_file_path, output_path=None):
    """
    Process cleavage mapping data according to pipeline formulas
    """
    print(f"Processing {csv_file_path}...")
    
    # Read the CSV file
    df = pd.read_csv(csv_file_path, sep='\t')
    
    # Clean up column names and handle the data structure
    df.columns = df.columns.str.strip()
    
    # Remove empty rows and header-only rows
    df = df[df['Sequence'].notna() & (df['Sequence'].str.strip() != '')]
    df = df[df['Sequence'].str.contains(r'\([A-Z]\)$', na=False)]
    
    # Create calculation dataframe
    calc_df = pd.DataFrame()
    
    # Column A: Sequence (copy from raw)
    calc_df['Sequence'] = df['Sequence'].str.strip()
    
    # Column B: LeftResidue (empty in this data format - no left residue in parentheses)
    calc_df['LeftResidue'] = ''
    
    # Column C: RightResidue (extract from sequence ending)
    calc_df['RightResidue'] = calc_df['Sequence'].apply(extract_right_residue)
    
    # Column D: CorePeptide (remove right residue parentheses)
    calc_df['CorePeptide'] = calc_df['Sequence'].apply(extract_core_peptide)
    
    # Columns E: Left_Sum (sum of function columns C through I)
    function_cols = [col for col in df.columns if 'Fxn' in col]
    print(f"Found function columns: {function_cols}")
    
    # Convert function columns to numeric, handling scientific notation
    for col in function_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    # Calculate Left_Sum (sum of all function values)
    calc_df['Left_Sum'] = df[function_cols].sum(axis=1)
    
    # Column F: Right_Sum (currently 0 as per documentation)
    calc_df['Right_Sum'] = 0
    
    # Column G: Total_Sum (Left + Right)
    calc_df['Total_Sum'] = calc_df['Left_Sum'] + calc_df['Right_Sum']
    
    # Column H: Left_Percentage
    calc_df['Left_Percentage'] = np.where(
        calc_df['Total_Sum'] == 0, 
        0, 
        (calc_df['Left_Sum'] / calc_df['Total_Sum'] * 100)
    )
    
    # Column I: Right_Percentage  
    calc_df['Right_Percentage'] = np.where(
        calc_df['Total_Sum'] == 0,
        0,
        (calc_df['Right_Sum'] / calc_df['Total_Sum'] * 100)
    )
    
    # Save results
    if output_path:
        calc_df.to_csv(output_path, index=False)
        print(f"Results saved to {output_path}")
    
    return calc_df

def analyze_results(calc_df):
    """Analyze the processed results"""
    print("\n=== CLEAVAGE MAPPING ANALYSIS ===\n")
    
    # Filter out zero-sum entries for analysis
    active_df = calc_df[calc_df['Total_Sum'] > 0].copy()
    
    print(f"Total sequences processed: {len(calc_df)}")
    print(f"Sequences with function values: {len(active_df)}")
    
    # Right-anchored analysis
    print("\n--- RIGHT-ANCHORED CLEAVAGE ANALYSIS ---")
    right_summary = active_df.groupby('RightResidue').agg({
        'Total_Sum': ['count', 'sum', 'mean'],
        'CorePeptide': 'count'
    }).round(0)
    
    right_summary.columns = ['Count', 'Total_Intensity', 'Mean_Intensity', 'Peptide_Count']
    right_summary = right_summary.sort_values('Total_Intensity', ascending=False)
    
    print("Right Residue Summary (Top 10):")
    print(right_summary.head(10))
    
    # Show top sequences by intensity
    print(f"\n--- TOP 10 SEQUENCES BY INTENSITY ---")
    top_sequences = active_df.nlargest(10, 'Total_Sum')[['CorePeptide', 'RightResidue', 'Total_Sum']]
    print(top_sequences.to_string(index=False))
    
    return right_summary

if __name__ == "__main__":
    # Process the 100_mgd data
    input_file = "/Users/jamison.ducey/Desktop/GH Repos/cleavage_mapper/data/100_mgd.csv"
    output_file = "/Users/jamison.ducey/Desktop/GH Repos/cleavage_mapper/excel/Calc_100_Processed.csv"
    
    # Process the data
    results_df = process_cleavage_data(input_file, output_file)
    
    # Analyze results
    summary = analyze_results(results_df)
    
    print(f"\nProcessing complete! Check {output_file} for detailed results.")