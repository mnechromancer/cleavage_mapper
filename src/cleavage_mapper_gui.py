#!/usr/bin/env python3
"""
CLEAVAGE MAPPER - User-Friendly Interface
A simple tool for analyzing peptide cleavage data

Just run this script and follow the prompts!
"""

import os
import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading

# Try to import required modules
try:
    from cleavage_mapper import AdvancedCleavageMapper
    import pandas as pd
except ImportError as e:
    print(f"Missing required packages. Please install with: pip install -r requirements.txt")
    print(f"Error: {e}")
    sys.exit(1)

class CleavageMapperGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cleavage Mapper - Peptide Analysis Tool")
        self.root.geometry("700x600")
        
        # Variables
        self.excel_file = tk.StringVar()
        self.output_folder = tk.StringVar(value=str(Path.cwd()))
        self.selected_worksheets = []
        self.sample_names = []
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main title
        title_frame = ttk.Frame(self.root, padding="10")
        title_frame.pack(fill=tk.X)
        
        ttk.Label(title_frame, text="🧬 Cleavage Mapper", 
                 font=("Arial", 16, "bold")).pack()
        ttk.Label(title_frame, text="Peptide Cleavage Analysis Tool", 
                 font=("Arial", 10)).pack()
        
        # File selection
        file_frame = ttk.LabelFrame(self.root, text="1. Select Your Excel File", padding="10")
        file_frame.pack(fill=tk.X, padx=10, pady=5)
        
        file_row = ttk.Frame(file_frame)
        file_row.pack(fill=tk.X)
        
        ttk.Entry(file_row, textvariable=self.excel_file, width=60).pack(side=tk.LEFT, padx=(0,5))
        ttk.Button(file_row, text="Browse...", command=self.browse_file).pack(side=tk.RIGHT)
        
        # Worksheet selection
        self.worksheet_frame = ttk.LabelFrame(self.root, text="2. Select Worksheets to Analyze", padding="10")
        self.worksheet_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.worksheet_listbox = tk.Listbox(self.worksheet_frame, height=4, selectmode=tk.MULTIPLE)
        self.worksheet_listbox.pack(fill=tk.X)
        
        # Sample names
        sample_frame = ttk.LabelFrame(self.root, text="3. Sample Names (Optional)", padding="10")
        sample_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(sample_frame, text="Leave blank to use default names (Sample_1, Sample_2, etc.)").pack(anchor=tk.W)
        self.sample_text = tk.Text(sample_frame, height=3, wrap=tk.WORD)
        self.sample_text.pack(fill=tk.X, pady=(5,0))
        self.sample_text.insert("1.0", "AspN_Fxn2, AspN_Fxn3, AspN_Fxn4, AspN_Fxn5, AspN_Fxn6, AspN_Fxn7, AspN_Fxn8")
        
        # Output folder
        output_frame = ttk.LabelFrame(self.root, text="4. Output Folder", padding="10")
        output_frame.pack(fill=tk.X, padx=10, pady=5)
        
        output_row = ttk.Frame(output_frame)
        output_row.pack(fill=tk.X)
        
        ttk.Entry(output_row, textvariable=self.output_folder, width=60).pack(side=tk.LEFT, padx=(0,5))
        ttk.Button(output_row, text="Browse...", command=self.browse_folder).pack(side=tk.RIGHT)
        
        # Analysis options
        options_frame = ttk.LabelFrame(self.root, text="5. Analysis Options", padding="10")
        options_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.create_excel = tk.BooleanVar(value=True)
        self.create_heatmaps = tk.BooleanVar(value=True)
        self.create_positional = tk.BooleanVar(value=True)
        self.create_comparison = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(options_frame, text="Generate processed Excel files", 
                       variable=self.create_excel).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Create sequence heatmaps", 
                       variable=self.create_heatmaps).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Create positional heatmaps", 
                       variable=self.create_positional).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Create comprehensive comparison report", 
                       variable=self.create_comparison).pack(anchor=tk.W)
        
        # Run button
        run_frame = ttk.Frame(self.root, padding="10")
        run_frame.pack(fill=tk.X)
        
        self.run_button = ttk.Button(run_frame, text="🚀 Run Analysis", 
                                   command=self.run_analysis, style="Accent.TButton")
        self.run_button.pack(pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(run_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=(0,10))
        
        # Results area
        results_frame = ttk.LabelFrame(self.root, text="Results", padding="10")
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.results_text = tk.Text(results_frame, height=8, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def browse_file(self):
        """Browse for Excel file"""
        filename = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
        )
        if filename:
            self.excel_file.set(filename)
            self.load_worksheets()
    
    def browse_folder(self):
        """Browse for output folder"""
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_folder.set(folder)
    
    def load_worksheets(self):
        """Load worksheets from selected Excel file"""
        try:
            self.worksheet_listbox.delete(0, tk.END)
            
            if not self.excel_file.get():
                return
            
            # Try to load the file and get worksheet names
            file_path = self.excel_file.get()
            
            # Handle old Excel format
            if file_path.endswith('.xls'):
                self.log("Converting old Excel format...")
                excel_file = pd.ExcelFile(file_path, engine='xlrd')
                worksheets = excel_file.sheet_names
            else:
                import openpyxl
                wb = openpyxl.load_workbook(file_path)
                worksheets = wb.sheetnames
            
            # Add worksheets to listbox
            for ws in worksheets:
                self.worksheet_listbox.insert(tk.END, ws)
            
            # Auto-select worksheets containing "glucose"
            for i, ws in enumerate(worksheets):
                if 'glucose' in ws.lower():
                    self.worksheet_listbox.selection_set(i)
            
            self.log(f"Loaded {len(worksheets)} worksheets from file")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not load Excel file:\n{str(e)}")
    
    def log(self, message):
        """Add message to results area"""
        self.results_text.insert(tk.END, f"{message}\n")
        self.results_text.see(tk.END)
        self.root.update()
    
    def run_analysis(self):
        """Run the cleavage analysis"""
        # Validate inputs
        if not self.excel_file.get():
            messagebox.showerror("Error", "Please select an Excel file")
            return
        
        selected_indices = self.worksheet_listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Error", "Please select at least one worksheet")
            return
        
        # Disable run button and start progress
        self.run_button.config(state='disabled')
        self.progress.start()
        
        # Run analysis in separate thread
        thread = threading.Thread(target=self._run_analysis_thread)
        thread.daemon = True
        thread.start()
    
    def _run_analysis_thread(self):
        """Run analysis in background thread"""
        try:
            self.log("🚀 Starting cleavage analysis...")
            
            # Get selected worksheets
            selected_indices = self.worksheet_listbox.curselection()
            worksheets = [self.worksheet_listbox.get(i) for i in selected_indices]
            
            # Get sample names
            sample_text = self.sample_text.get("1.0", tk.END).strip()
            if sample_text:
                sample_names = [name.strip() for name in sample_text.split(',')]
            else:
                sample_names = None
            
            # Setup output directory
            output_dir = Path(self.output_folder.get())
            output_dir.mkdir(exist_ok=True)
            
            # Convert file if needed
            input_file = self.excel_file.get()
            if input_file.endswith('.xls'):
                self.log("Converting Excel file format...")
                converted_file = output_dir / "converted_data.xlsx"
                self._convert_excel_file(input_file, str(converted_file))
                input_file = str(converted_file)
            
            # Initialize mapper
            self.log("Initializing cleavage mapper...")
            mapper = AdvancedCleavageMapper(input_file)
            
            # Process each worksheet
            conditions = []
            for worksheet in worksheets:
                self.log(f"Processing worksheet: {worksheet}")
                
                try:
                    # Process the worksheet
                    if self.create_excel.get():
                        output_name = f"{worksheet} PROCESSED"
                        mapper.process(worksheet, output_name, sample_names)
                    
                    # Create visualizations
                    if any([self.create_heatmaps.get(), self.create_positional.get()]):
                        safe_name = worksheet.replace(' ', '_').replace('/', '_')
                        viz_files = mapper.create_visualizations(
                            worksheet, sample_names, 
                            str(output_dir / f"analysis_{safe_name}"),
                            top_n_peptides=25
                        )
                        
                        for viz_file in viz_files:
                            if os.path.exists(viz_file):
                                # Move to output directory
                                new_path = output_dir / os.path.basename(viz_file)
                                os.rename(viz_file, str(new_path))
                    
                    conditions.append((worksheet, worksheet.replace(' mgd glucose', ' mgd')))
                    self.log(f"✓ Completed: {worksheet}")
                    
                except Exception as e:
                    self.log(f"✗ Error processing {worksheet}: {str(e)}")
            
            # Save Excel file
            if self.create_excel.get():
                excel_output = output_dir / "cleavage_analysis_results.xlsx"
                mapper.save(str(excel_output))
                self.log(f"✓ Excel results saved: {excel_output.name}")
            
            # Create comprehensive comparison
            if self.create_comparison.get() and len(conditions) > 1:
                self.log("Creating comprehensive comparison report...")
                comp_output = output_dir / "comprehensive_comparison_report.png"
                mapper.create_comprehensive_report(
                    conditions=conditions,
                    sample_labels=sample_names,
                    output_path=str(comp_output)
                )
                self.log(f"✓ Comparison report saved: {comp_output.name}")
            
            self.log(f"\n🎉 Analysis complete! Check output folder: {output_dir}")
            self.log(f"📊 Generated files:")
            
            for file in output_dir.iterdir():
                if file.suffix in ['.xlsx', '.png']:
                    self.log(f"  - {file.name}")
            
        except Exception as e:
            self.log(f"✗ Analysis failed: {str(e)}")
            messagebox.showerror("Error", f"Analysis failed:\n{str(e)}")
        
        finally:
            # Re-enable button and stop progress
            self.root.after(0, self._analysis_complete)
    
    def _convert_excel_file(self, input_file, output_file):
        """Convert old Excel format to new format"""
        excel_file = pd.ExcelFile(input_file, engine='xlrd')
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            for sheet_name in excel_file.sheet_names:
                df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
                df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
    
    def _analysis_complete(self):
        """Called when analysis is complete"""
        self.run_button.config(state='normal')
        self.progress.stop()
    
    def run(self):
        """Start the GUI"""
        self.root.mainloop()

def main():
    """Main entry point"""
    print("🧬 Starting Cleavage Mapper GUI...")
    app = CleavageMapperGUI()
    app.run()

if __name__ == "__main__":
    main()