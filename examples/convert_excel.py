#!/usr/bin/env python3
"""
Convert old Excel format to new xlsx format
"""
import pandas as pd
import sys

def convert_xls_to_xlsx(input_file, output_file):
    """Convert old Excel format to xlsx"""
    try:
        # Read all sheets from the old format
        excel_file = pd.ExcelFile(input_file, engine='xlrd')
        
        # Create a new Excel writer
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            for sheet_name in excel_file.sheet_names:
                # Read each sheet
                df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
                # Write to new format
                df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
        
        print(f"Successfully converted {input_file} to {output_file}")
        print(f"Sheets: {excel_file.sheet_names}")
        
    except Exception as e:
        print(f"Error converting file: {e}")

if __name__ == "__main__":
    convert_xls_to_xlsx('example_data.xlsx', 'example_data_converted.xlsx')