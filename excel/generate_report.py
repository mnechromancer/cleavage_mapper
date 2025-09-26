#!/usr/bin/env python3
"""
Cleavage Mapping Pipeline - Summary Report Generator
Creates left and right-anchored analysis tables
"""

import pandas as pd
import numpy as np

def create_summary_report(processed_file):
    """Create summary analysis report with left/right anchored tables"""
    
    df = pd.read_csv(processed_file)
    
    # Filter active sequences (with function values > 0)
    active_df = df[df['Total_Sum'] > 0].copy()
    
    print("="*80)
    print("CLEAVAGE MAPPING PIPELINE - 100 mgd GLUCOSE RESULTS")
    print("="*80)
    
    print(f"\nDATA SUMMARY:")
    print(f"Total sequences in dataset: {len(df)}")
    print(f"Sequences with measurable function values: {len(active_df)}")
    print(f"Percentage of active sequences: {len(active_df)/len(df)*100:.1f}%")
    
    # RIGHT-ANCHORED CLEAVAGE TABLE (Primary analysis for this data)
    print(f"\nRIGHT-ANCHORED CLEAVAGE ANALYSIS")
    print("-" * 50)
    
    right_anchored = active_df.groupby('RightResidue').agg({
        'CorePeptide': 'count',
        'Total_Sum': ['sum', 'mean', 'std'],
        'Left_Sum': ['sum', 'mean']
    }).round(0)
    
    # Flatten column names
    right_anchored.columns = ['Count', 'Total_Intensity', 'Mean_Intensity', 'Std_Intensity', 
                             'Left_Total', 'Left_Mean']
    right_anchored = right_anchored.sort_values('Total_Intensity', ascending=False)
    
    print("Right Residue Cleavage Summary:")
    print(right_anchored)
    
    # TOP PEPTIDES BY RIGHT RESIDUE
    print(f"\nTOP 5 PEPTIDES BY RIGHT RESIDUE TYPE")
    print("-" * 50)
    
    for residue in right_anchored.index[:5]:  # Top 5 residues
        top_peptides = active_df[active_df['RightResidue'] == residue].nlargest(3, 'Total_Sum')
        print(f"\n{residue} - Cleavage (Top 3 peptides):")
        for idx, row in top_peptides.iterrows():
            print(f"  {row['CorePeptide'][:50]:<50} | Intensity: {row['Total_Sum']:,.0f}")
    
    # SEQUENCE LENGTH ANALYSIS
    print(f"\nSEQUENCE LENGTH ANALYSIS")
    print("-" * 30)
    
    active_df['PeptideLength'] = active_df['CorePeptide'].str.len()
    length_analysis = active_df.groupby('PeptideLength').agg({
        'CorePeptide': 'count',
        'Total_Sum': ['sum', 'mean']
    }).round(0)
    length_analysis.columns = ['Count', 'Total_Intensity', 'Mean_Intensity']
    length_analysis = length_analysis.sort_values('Total_Intensity', ascending=False)
    
    print("Peptide Length Distribution (Top 10):")
    print(length_analysis.head(10))
    
    # CLEAVAGE PATTERN INSIGHTS
    print(f"\nCLEAVAGE PATTERN INSIGHTS")
    print("-" * 30)
    
    # Most abundant right residues
    total_intensity = right_anchored['Total_Intensity'].sum()
    right_anchored['Percentage'] = (right_anchored['Total_Intensity'] / total_intensity * 100).round(1)
    
    print("Right Residue Abundance (% of total intensity):")
    for residue, data in right_anchored.head(8).iterrows():
        print(f"  {residue}: {data['Percentage']:>6.1f}% ({data['Count']} peptides)")
    
    # Highest intensity individual peptides
    print(f"\nTOP 10 INDIVIDUAL PEPTIDES BY INTENSITY")
    print("-" * 45)
    top_peptides = active_df.nlargest(10, 'Total_Sum')
    
    for idx, (_, row) in enumerate(top_peptides.iterrows(), 1):
        core_display = row['CorePeptide'][:40] + "..." if len(row['CorePeptide']) > 40 else row['CorePeptide']
        print(f"{idx:2d}. [{row['RightResidue']}] {core_display:<43} | {row['Total_Sum']:>12,.0f}")
    
    return right_anchored, active_df

def create_excel_compatible_tables(active_df, output_dir):
    """Create Excel-compatible output tables as per pipeline spec"""
    
    # Left-Anchored Table (Note: This data doesn't have left residues, so this will be empty)
    left_anchored = active_df[active_df['LeftResidue'] != ''][['LeftResidue', 'CorePeptide', 'Left_Sum']].copy()
    left_anchored.to_csv(f"{output_dir}/Left_Anchored_Table.csv", index=False)
    
    # Right-Anchored Table (Primary table for this dataset)
    right_anchored = active_df[active_df['RightResidue'] != ''][['RightResidue', 'CorePeptide', 'Left_Sum', 'Total_Sum']].copy()
    right_anchored = right_anchored.sort_values(['RightResidue', 'Total_Sum'], ascending=[True, False])
    right_anchored.to_csv(f"{output_dir}/Right_Anchored_Table.csv", index=False)
    
    print(f"\nEXCEL TABLES CREATED:")
    print(f"- Left_Anchored_Table.csv: {len(left_anchored)} rows")
    print(f"- Right_Anchored_Table.csv: {len(right_anchored)} rows")
    
    return left_anchored, right_anchored

if __name__ == "__main__":
    processed_file = "/Users/jamison.ducey/Desktop/GH Repos/cleavage_mapper/excel/Calc_100_Processed.csv"
    output_dir = "/Users/jamison.ducey/Desktop/GH Repos/cleavage_mapper/excel"
    
    # Generate summary report
    right_summary, active_data = create_summary_report(processed_file)
    
    # Create Excel-compatible tables
    left_table, right_table = create_excel_compatible_tables(active_data, output_dir)
    
    print(f"\n" + "="*80)
    print("PIPELINE PROCESSING COMPLETE")
    print("="*80)
    print("Files created:")
    print("- Calc_100_Processed.csv (Main calculation results)")
    print("- Left_Anchored_Table.csv (Left-anchored cleavage view)")
    print("- Right_Anchored_Table.csv (Right-anchored cleavage view)")