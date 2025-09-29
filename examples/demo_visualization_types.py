#!/usr/bin/env python3
"""
Quick demonstration of the new positional vs traditional visualization
"""

from cleavage_mapper import AdvancedCleavageMapper
import matplotlib.pyplot as plt

def demonstrate_visualization_types():
    """Show the difference between traditional and positional heatmaps"""
    print("=== Visualization Types Demonstration ===")
    
    # Initialize mapper
    mapper = AdvancedCleavageMapper('example_data_converted.xlsx')
    
    # Sample names
    sample_names = [
        'AspN_Fxn2', 'AspN_Fxn3', 'AspN_Fxn4', 
        'AspN_Fxn5', 'AspN_Fxn6', 'AspN_Fxn7', 'AspN_Fxn8'
    ]
    
    # Get data for 500 mgd condition
    raw_data = mapper.parse_raw_worksheet('500 mgd glucose')
    
    print(f"Reference sequence: {raw_data['reference']}")
    print(f"Sequence length: {len(raw_data['reference'])} amino acids")
    print(f"Number of individual sequences: {len(raw_data['sequences'])}")
    
    print("\n--- Creating Traditional Sequence Heatmap ---")
    print("Shows intensities for individual peptide sequences (Y-axis = different sequences)")
    mapper.create_intensity_heatmap(
        raw_data, 
        sample_names, 
        'demo_traditional_heatmap.png',
        figsize=(12, 8),
        top_n=20  # Show only top 20 sequences
    )
    
    print("\n--- Creating Positional Heatmap ---")
    print("Shows intensities aggregated by amino acid position (Y-axis = amino acid positions)")
    mapper.create_positional_intensity_heatmap(
        raw_data, 
        sample_names, 
        'demo_positional_heatmap.png',
        figsize=(12, 8)
    )
    
    plt.close('all')
    
    print("\n✓ Demonstration complete!")
    print("\n📊 Compare these files to see the difference:")
    print("  - demo_traditional_heatmap.png (shows individual sequences)")
    print("  - demo_positional_heatmap.png (shows amino acid positions)")
    print("\n💡 The positional heatmap is ideal for understanding which")
    print("   amino acid positions in your reference sequence show")
    print("   the most cleavage activity across all your peptide variants!")

if __name__ == "__main__":
    demonstrate_visualization_types()