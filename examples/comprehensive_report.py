#!/usr/bin/env python3
"""
Comprehensive Cleavage Analysis Report Generator
Creates a single comprehensive visualization comparing all conditions
"""

from cleavage_mapper import AdvancedCleavageMapper
import matplotlib.pyplot as plt
import os

def create_comprehensive_analysis():
    """Create a comprehensive analysis report with all conditions"""
    print("=== Comprehensive Cleavage Analysis Report ===")
    
    # Check if converted data exists
    if not os.path.exists('example_data_converted.xlsx'):
        print("Please run the main script first to convert the data format")
        return
    
    # Initialize mapper
    mapper = AdvancedCleavageMapper('example_data_converted.xlsx')
    
    # Sample names
    sample_names = [
        'AspN_Fxn2', 'AspN_Fxn3', 'AspN_Fxn4', 
        'AspN_Fxn5', 'AspN_Fxn6', 'AspN_Fxn7', 'AspN_Fxn8'
    ]
    
    print(f"Available worksheets: {mapper.wb.sheetnames}")
    
    # Define conditions to compare
    conditions = [
        ('100 mgd glucose', '100 mgd'),
        ('200 mgd glucose', '200 mgd'), 
        ('500 mgd glucose', '500 mgd')
    ]
    
    # Create comprehensive report
    print("\nGenerating comprehensive report...")
    report_fig = mapper.create_comprehensive_report(
        conditions=conditions,
        sample_labels=sample_names,
        output_path='comprehensive_cleavage_report.png',
        figsize=(20, 16)
    )
    
    # Also create individual positional heatmaps for each condition
    print("\nCreating individual positional heatmaps...")
    
    for worksheet, display_name in conditions:
        if worksheet in mapper.wb.sheetnames:
            try:
                print(f"Processing {display_name}...")
                raw_data = mapper.parse_raw_worksheet(worksheet)
                
                # Create positional heatmap
                output_path = f'positional_{display_name.replace(" ", "_")}_heatmap.png'
                mapper.create_positional_intensity_heatmap(
                    raw_data, 
                    sample_names, 
                    output_path,
                    figsize=(12, 10)
                )
                
            except Exception as e:
                print(f"⚠ Failed to process {worksheet}: {e}")
    
    # Close all plots
    plt.close('all')
    
    print("\n=== Report Complete ===")
    print("Generated files:")
    for file in os.listdir('.'):
        if (file.startswith('comprehensive_') or file.startswith('positional_')) and file.endswith('.png'):
            print(f"  📊 {file}")
    
    print("\n🎉 Comprehensive analysis complete!")
    print("📋 Open 'comprehensive_cleavage_report.png' for the full comparative report")

def create_detailed_positional_analysis():
    """Create detailed positional analysis for a single condition"""
    print("\n=== Detailed Positional Analysis ===")
    
    mapper = AdvancedCleavageMapper('example_data_converted.xlsx')
    sample_names = [
        'AspN_Fxn2', 'AspN_Fxn3', 'AspN_Fxn4', 
        'AspN_Fxn5', 'AspN_Fxn6', 'AspN_Fxn7', 'AspN_Fxn8'
    ]
    
    # Focus on 500 mgd condition for detailed analysis
    worksheet = '500 mgd glucose'
    raw_data = mapper.parse_raw_worksheet(worksheet)
    
    print(f"Analyzing {worksheet}...")
    print(f"Reference sequence: {raw_data['reference']}")
    print(f"Reference length: {len(raw_data['reference'])} amino acids")
    print(f"Number of sequences: {len(raw_data['sequences'])}")
    
    # Create detailed positional heatmap
    fig = mapper.create_positional_intensity_heatmap(
        raw_data, 
        sample_names, 
        'detailed_positional_500mgd.png',
        figsize=(16, 12)
    )
    
    plt.close('all')
    print("✓ Detailed positional analysis complete!")

if __name__ == "__main__":
    # Create comprehensive report
    create_comprehensive_analysis()
    
    # Create detailed analysis
    create_detailed_positional_analysis()
    
    print("\n📈 All analyses complete! Check the PNG files for your results.")