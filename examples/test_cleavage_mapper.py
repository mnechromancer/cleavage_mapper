#!/usr/bin/env python3
"""
Test script for the Cleavage Mapper
This script demonstrates how to use the AdvancedCleavageMapper class
"""

from cleavage_mapper import AdvancedCleavageMapper
import os

def main():
    print("=== Cleavage Mapper Test ===")
    
    # Check if the required files exist
    if not os.path.exists('example_data_converted.xlsx'):
        print("Converting Excel file format...")
        import pandas as pd
        try:
            # Convert old Excel format to new format
            excel_file = pd.ExcelFile('example_data.xlsx', engine='xlrd')
            with pd.ExcelWriter('example_data_converted.xlsx', engine='openpyxl') as writer:
                for sheet_name in excel_file.sheet_names:
                    df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
                    df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
            print("✓ Conversion completed")
        except Exception as e:
            print(f"✗ Conversion failed: {e}")
            return
    
    # Initialize the mapper
    print("Initializing cleavage mapper...")
    mapper = AdvancedCleavageMapper('example_data_converted.xlsx')
    
    # Show available worksheets
    print(f"Available worksheets: {mapper.wb.sheetnames}")
    
    # Process the 500 mgd glucose worksheet
    print("\nProcessing '500 mgd glucose' worksheet...")
    sample_names = [
        'AspN_Fxn2', 'AspN_Fxn3', 'AspN_Fxn4', 
        'AspN_Fxn5', 'AspN_Fxn6', 'AspN_Fxn7', 'AspN_Fxn8'
    ]
    
    try:
        mapper.process('500 mgd glucose', '500 mgd PROCESSED', sample_names)
        mapper.save('cleavage_mapper_output.xlsx')
        print("✓ Processing completed successfully!")
        print("✓ Output saved to 'cleavage_mapper_output.xlsx'")
        
        # Show summary of results
        ws = mapper.wb['500 mgd PROCESSED']
        print(f"✓ Generated worksheet with {ws.max_row} rows and {ws.max_column} columns")
        
        # Create visualizations
        print("\nCreating visualizations...")
        viz_files = mapper.create_visualizations(
            '500 mgd glucose', 
            sample_names, 
            'cleavage_500mgd',
            top_n_peptides=30  # Show top 30 peptides for better readability
        )
        print(f"✓ Visualization files created: {viz_files}")
        
        # Create comprehensive report comparing all conditions
        print("\nCreating comprehensive comparative report...")
        try:
            conditions = [
                ('100 mgd glucose', '100 mgd'),
                ('200 mgd glucose', '200 mgd'), 
                ('500 mgd glucose', '500 mgd')
            ]
            mapper.create_comprehensive_report(
                conditions=conditions,
                sample_labels=sample_names,
                output_path='test_comprehensive_report.png'
            )
            print("✓ Comprehensive report created!")
        except Exception as e:
            print(f"⚠ Comprehensive report failed: {e}")
        
    except Exception as e:
        print(f"✗ Processing failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()