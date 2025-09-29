#!/usr/bin/env python3
"""
SIMPLE CLEAVAGE MAPPER - Command Line Version
Easy-to-use command line interface for peptide cleavage analysis

Usage: python run_analysis.py [your_excel_file.xlsx]
"""

import sys
import os
from pathlib import Path
import argparse

# Add src directory to Python path
current_dir = Path(__file__).parent
src_dir = current_dir / "src"
sys.path.insert(0, str(src_dir))

def main():
    print("🧬 CLEAVAGE MAPPER - Simple Analysis Tool")
    print("=" * 50)
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Analyze peptide cleavage data')
    parser.add_argument('excel_file', nargs='?', help='Excel file to analyze')
    parser.add_argument('--output', '-o', help='Output directory', default='cleavage_results')
    parser.add_argument('--samples', '-s', help='Sample names (comma-separated)')
    parser.add_argument('--worksheets', '-w', help='Worksheet names (comma-separated)')
    args = parser.parse_args()
    
    # Check if GUI should be launched
    if not args.excel_file:
        print("No file specified. Launching GUI interface...")
        try:
            from cleavage_mapper_gui import main as gui_main
            gui_main()
            return
        except ImportError:
            print("GUI not available. Please specify an Excel file:")
            print("Usage: python run_analysis.py your_file.xlsx")
            return
    
    # Validate file exists
    excel_file = Path(args.excel_file)
    if not excel_file.exists():
        print(f"❌ Error: File '{excel_file}' not found")
        return
    
    print(f"📁 Input file: {excel_file}")
    
    try:
        # Import required modules
        from cleavage_mapper import AdvancedCleavageMapper
        import pandas as pd
        import openpyxl
        
        # Setup output directory (ensure it's in the output folder)
        if not args.output.startswith('output/'):
            output_dir = Path('output') / args.output
        else:
            output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"📂 Output directory: {output_dir}")
        
        # Handle old Excel format
        input_file = str(excel_file)
        if excel_file.suffix == '.xls':
            print("🔄 Converting old Excel format...")
            excel_data = pd.ExcelFile(input_file, engine='xlrd')
            converted_file = Path('data') / "converted_data.xlsx"
            converted_file.parent.mkdir(exist_ok=True)
            
            with pd.ExcelWriter(str(converted_file), engine='openpyxl') as writer:
                for sheet_name in excel_data.sheet_names:
                    df = pd.read_excel(excel_data, sheet_name=sheet_name, header=None)
                    df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
            
            input_file = str(converted_file)
            print("✅ Conversion complete")
        
        # Initialize mapper
        print("🔬 Initializing cleavage mapper...")
        mapper = AdvancedCleavageMapper(input_file)
        
        # Get available worksheets
        available_worksheets = mapper.wb.sheetnames
        print(f"📋 Available worksheets: {', '.join(available_worksheets)}")
        
        # Determine which worksheets to process
        if args.worksheets:
            worksheets_to_process = [w.strip() for w in args.worksheets.split(',')]
        else:
            # Auto-select worksheets containing 'glucose', but avoid duplicates
            glucose_sheets = [ws for ws in available_worksheets if 'glucose' in ws.lower()]
            # Prefer sheets without "(2)" in the name, or take first 3
            preferred_sheets = [ws for ws in glucose_sheets if '(2)' not in ws]
            if len(preferred_sheets) >= 3:
                worksheets_to_process = preferred_sheets[:3]
            else:
                worksheets_to_process = glucose_sheets[:3] if glucose_sheets else available_worksheets[:3]
        
        print(f"🎯 Processing worksheets: {', '.join(worksheets_to_process)}")
        
        # Get sample names
        if args.samples:
            sample_names = [s.strip() for s in args.samples.split(',')]
        else:
            sample_names = [
                'AspN_Fxn2', 'AspN_Fxn3', 'AspN_Fxn4', 
                'AspN_Fxn5', 'AspN_Fxn6', 'AspN_Fxn7', 'AspN_Fxn8'
            ]
        
        print(f"🔬 Sample names: {', '.join(sample_names)}")
        print()
        
        # Process each worksheet
        conditions = []
        for worksheet in worksheets_to_process:
            if worksheet not in available_worksheets:
                print(f"⚠️  Skipping '{worksheet}' - not found in file")
                continue
            
            print(f"📊 Processing: {worksheet}")
            
            try:
                # Process the data
                output_name = f"{worksheet} PROCESSED"
                mapper.process(worksheet, output_name, sample_names)
                
                # Create visualizations
                safe_name = worksheet.replace(' ', '_').replace('/', '_')
                prefix = str(output_dir / f"analysis_{safe_name}")
                
                viz_files = mapper.create_visualizations(
                    worksheet, sample_names, prefix, top_n_peptides=25
                )
                
                # Move visualization files to output directory
                for viz_file in viz_files:
                    if os.path.exists(viz_file):
                        new_path = output_dir / os.path.basename(viz_file)
                        if viz_file != str(new_path):
                            os.rename(viz_file, str(new_path))
                
                conditions.append((worksheet, worksheet.replace(' mgd glucose', ' mgd')))
                print(f"✅ Completed: {worksheet}")
                
            except Exception as e:
                print(f"❌ Error processing {worksheet}: {str(e)}")
        
        # Save Excel results
        excel_output = output_dir / "cleavage_analysis_results.xlsx"
        mapper.save(str(excel_output))
        print(f"💾 Excel results saved: {excel_output.name}")
        
        # Create comprehensive comparison if multiple conditions
        if len(conditions) > 1:
            print("📈 Creating comprehensive comparison report...")
            comp_output = output_dir / "comprehensive_comparison_report.png"
            mapper.create_comprehensive_report(
                conditions=conditions,
                sample_labels=sample_names,
                output_path=str(comp_output)
            )
            print(f"✅ Comparison report saved: {comp_output.name}")
        
        # Summary
        print()
        print("🎉 ANALYSIS COMPLETE!")
        print("=" * 30)
        print(f"📂 Results folder: {output_dir}")
        print("📊 Generated files:")
        
        generated_files = []
        for file in output_dir.iterdir():
            if file.suffix in ['.xlsx', '.png']:
                generated_files.append(file)
                file_type = "📋" if file.suffix == '.xlsx' else "📊"
                print(f"  {file_type} {file.name}")
        
        if generated_files:
            print(f"\n✨ Total files generated: {len(generated_files)}")
        
        print(f"\n💡 Tip: Open the PNG files to view your heatmaps and analysis plots!")
        
    except ImportError as e:
        print(f"❌ Missing required packages: {e}")
        print("📦 Please install requirements: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Analysis failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()