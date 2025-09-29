#!/usr/bin/env python3
"""
Standalone visualization script for Cleavage Mapper
Creates heatmaps and summary plots from cleavage data
"""

from cleavage_mapper import AdvancedCleavageMapper
import matplotlib.pyplot as plt
import os

def create_all_visualizations():
    """Create visualizations for all available worksheets"""
    print("=== Cleavage Mapper Visualization Tool ===")
    
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
    
    # Available worksheets (skip the duplicate one)
    worksheets_to_process = [
        ('100 mgd glucose', '100mgd'),
        ('200 mgd glucose', '200mgd'), 
        ('500 mgd glucose', '500mgd')
    ]
    
    print(f"Found worksheets: {mapper.wb.sheetnames}")
    
    # Create visualizations for each worksheet
    for worksheet, prefix in worksheets_to_process:
        if worksheet in mapper.wb.sheetnames:
            print(f"\n--- Processing {worksheet} ---")
            try:
                viz_files = mapper.create_visualizations(
                    worksheet, 
                    sample_names, 
                    f"viz_{prefix}",
                    top_n_peptides=25
                )
                print(f"✓ Created visualizations: {viz_files}")
            except Exception as e:
                print(f"✗ Failed to process {worksheet}: {e}")
        else:
            print(f"⚠ Worksheet '{worksheet}' not found")
    
    print("\n=== Visualization Summary ===")
    print("Generated files:")
    for file in os.listdir('.'):
        if file.startswith('viz_') and file.endswith('.png'):
            print(f"  📊 {file}")

def create_comparison_heatmap():
    """Create a side-by-side comparison of different glucose conditions"""
    print("\n=== Creating Comparison Heatmap ===")
    
    mapper = AdvancedCleavageMapper('example_data_converted.xlsx')
    sample_names = [
        'AspN_Fxn2', 'AspN_Fxn3', 'AspN_Fxn4', 
        'AspN_Fxn5', 'AspN_Fxn6', 'AspN_Fxn7', 'AspN_Fxn8'
    ]
    
    # Get data for all conditions
    conditions = ['100 mgd glucose', '200 mgd glucose', '500 mgd glucose']
    all_data = {}
    
    for condition in conditions:
        if condition in mapper.wb.sheetnames:
            try:
                raw_data = mapper.parse_raw_worksheet(condition)
                all_data[condition] = raw_data
            except Exception as e:
                print(f"⚠ Could not load {condition}: {e}")
    
    if not all_data:
        print("✗ No data available for comparison")
        return
    
    # Create comparison plot
    fig, axes = plt.subplots(1, len(all_data), figsize=(5 * len(all_data), 8))
    if len(all_data) == 1:
        axes = [axes]
    
    for idx, (condition, raw_data) in enumerate(all_data.items()):
        # Get top peptides by total intensity
        sequences = raw_data['sequences']
        peptide_intensities = [(seq['clean'][:15], sum(seq['intensities'])) 
                              for seq in sequences]
        peptide_intensities.sort(key=lambda x: x[1], reverse=True)
        top_peptides = peptide_intensities[:20]  # Top 20 peptides
        
        # Create matrix for this condition
        peptide_names = [p[0] for p in top_peptides]
        intensity_matrix = []
        
        for peptide_name, _ in top_peptides:
            # Find the sequence data
            for seq in sequences:
                if seq['clean'].startswith(peptide_name):
                    intensity_matrix.append(seq['intensities'])
                    break
        
        # Plot heatmap
        import numpy as np
        import seaborn as sns
        
        if intensity_matrix:
            log_data = np.log10(np.array(intensity_matrix) + 1)
            im = axes[idx].imshow(log_data, cmap='viridis', aspect='auto')
            axes[idx].set_title(f'{condition}\n(Top 20 peptides)')
            axes[idx].set_xlabel('Samples')
            axes[idx].set_ylabel('Peptides')
            axes[idx].set_yticks(range(len(peptide_names)))
            axes[idx].set_yticklabels(peptide_names, fontsize=8)
            axes[idx].set_xticks(range(len(sample_names)))
            axes[idx].set_xticklabels([s.replace('AspN_', '') for s in sample_names], 
                                     rotation=45, fontsize=8)
            
            # Add colorbar for the last subplot
            if idx == len(all_data) - 1:
                cbar = plt.colorbar(im, ax=axes[idx])
                cbar.set_label('Log10(Intensity + 1)')
    
    plt.suptitle('Peptide Intensity Comparison Across Glucose Conditions', 
                 fontsize=14, y=0.98)
    plt.tight_layout()
    
    comparison_path = 'comparison_heatmap.png'
    plt.savefig(comparison_path, dpi=300, bbox_inches='tight')
    print(f"✓ Comparison heatmap saved to: {comparison_path}")
    
    plt.close()

if __name__ == "__main__":
    # Create individual visualizations
    create_all_visualizations()
    
    # Create comparison plot
    create_comparison_heatmap()
    
    print("\n🎉 All visualizations completed!")
    print("\nTip: Open the .png files to view your heatmaps and analysis plots.")