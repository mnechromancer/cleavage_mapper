#!/usr/bin/env python3
"""
Simple example demonstrating the visualization features
"""

from cleavage_mapper import AdvancedCleavageMapper

def simple_visualization_example():
    """Create a quick heatmap visualization"""
    print("=== Simple Visualization Example ===")
    
    # Initialize mapper
    mapper = AdvancedCleavageMapper('example_data_converted.xlsx')
    
    # Sample names
    sample_names = [
        'AspN_Fxn2', 'AspN_Fxn3', 'AspN_Fxn4', 
        'AspN_Fxn5', 'AspN_Fxn6', 'AspN_Fxn7', 'AspN_Fxn8'
    ]
    
    # Create just a heatmap for the 500 mgd condition
    print("Creating heatmap for 500 mgd glucose condition...")
    
    # Parse the data
    raw_data = mapper.parse_raw_worksheet('500 mgd glucose')
    
    # Create heatmap (top 20 peptides for better visibility)
    fig = mapper.create_intensity_heatmap(
        raw_data, 
        sample_names, 
        'simple_heatmap.png',
        figsize=(10, 8),
        top_n=20
    )
    
    print("✓ Simple heatmap created!")
    print("📊 Open 'simple_heatmap.png' to view your peptide intensity heatmap")

if __name__ == "__main__":
    simple_visualization_example()