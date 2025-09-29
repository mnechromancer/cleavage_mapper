# 🧬 Cleavage Mapper
### Professional Peptide Cleavage Analysis Tool

An easy-to-use tool for analyzing peptide cleavage data with beautiful visualizations and comprehensive reports. **No programming experience required!**

![Analysis Example](https://img.shields.io/badge/Analysis-Automated-green) ![Visualizations](https://img.shields.io/badge/Visualizations-Advanced-blue) ![User_Friendly](https://img.shields.io/badge/Interface-User_Friendly-orange)

## 🚀 Quick Start

1. **Double-click `START_HERE.py`** to begin
2. **Choose your interface** (Graphical recommended for beginners)
3. **Select your Excel file** with peptide data
4. **Get professional results** in minutes!

## 📁 Project Structure

```
cleavage_mapper/
├── 🚀 START_HERE.py          # Main entry point - double-click to begin!
├── ⚙️ setup.py               # Automatic installation
├── 🏃 run_analysis.py        # Command line interface
├── 📋 requirements.txt       # Required packages
├── 📖 README.md              # This file
│
├── 📂 src/                   # Core application code
│   ├── cleavage_mapper.py    # Main analysis engine
│   └── cleavage_mapper_gui.py # Graphical interface
│
├── 📂 data/                  # Sample data and inputs
│   ├── example_data.xlsx     # Sample dataset
│   └── example_data_converted.xlsx
│
├── 📂 docs/                  # Documentation
│   ├── USER_GUIDE.md         # Detailed user instructions
│   └── OVERVIEW.md           # Quick reference
│
├── 📂 examples/              # Example scripts for developers
│   ├── comprehensive_report.py
│   ├── demo_visualization_types.py
│   └── ...
│
└── 📂 output/                # Generated results and visualizations
    ├── demo_results/         # Sample outputs
    └── [your_analysis]/      # Your results will appear here
```

## ✨ What This Tool Does

Transform your peptide cleavage data into professional analysis reports with just a few clicks!

### 🎯 **Key Features**
- **🖱️ Easy Graphical Interface** - No coding required, just point and click
- **📊 Beautiful Visualizations** - Professional heatmaps and comparison charts
- **⚡ Automated Analysis** - Complete peptide cleavage mapping with bidirectional analysis
- **📈 Comparative Reports** - Compare multiple experimental conditions side-by-side
- **💾 Excel Integration** - Generates processed Excel files with formulas and calculations
- **� Advanced Analytics** - Position-based intensity analysis and cleavage pattern recognition

### 📊 **Types of Analysis**
1. **Positional Intensity Heatmaps** - See which amino acid positions show the most activity
2. **Sequence-Based Heatmaps** - Traditional peptide sequence analysis  
3. **Cleavage Pattern Analysis** - N-terminal and C-terminal cleavage summaries
4. **Comprehensive Comparative Reports** - Multi-condition analysis in one visualization
5. **Statistical Summaries** - Automated calculations and summary tables

## � System Requirements

- **Python 3.7 or higher** ([Download here](https://python.org))
- **Windows, Mac, or Linux**
- **~50MB disk space** for installation
- **Excel files** (.xlsx or .xls format) with your peptide data

## 🛠️ Installation

### **Option 1: Automatic Setup (Recommended)**
1. **Download** this tool to your computer
2. **Double-click** `setup.py` to automatically install everything
3. **Double-click** `START_HERE.py` to begin analysis

### **Option 2: Manual Setup**
```bash
pip install -r requirements.txt
python START_HERE.py
```

## 🎯 How to Use

### **🖱️ Graphical Interface (Easiest)**
1. **Double-click `START_HERE.py`** → Choose option 1
2. **Select your Excel file** using the Browse button
3. **Choose worksheets** to analyze (auto-selects glucose conditions)
4. **Enter sample names** (or use defaults)
5. **Choose output folder** (results go to `output/` directory)
6. **Click "Run Analysis"** and wait for completion!

### **⌨️ Command Line Interface**
```bash
# Basic analysis
python run_analysis.py data/your_file.xlsx

# Custom output location
python run_analysis.py data/your_file.xlsx --output my_analysis

# Quick demo
python START_HERE.py  # Then choose option 3
```

## Data Format

The tool expects Excel files with:

1. **Row 4**: Reference sequence (full peptide sequence)
2. **Row 5+**: Individual sequences with:
   - Column A: Sequence number
   - Column B: Sequence with cleavage notation like `(E)AEDLQVGQVELGGGPGA(S)`
   - Columns C-I: Intensity values across different samples

## Output Format

### Excel Output
The processed worksheet includes:

- **Left Panel**: N-terminal cleavage analysis
- **Right Panel**: C-terminal cleavage analysis  
- **Calculated Columns**: Sums, percentages, and linkage formulas
- **Summary Statistics**: Total intensities and percentages

### Visualization Output
The visualization tools generate:

- **Intensity Heatmaps**: Show peptide intensities across samples using log-scale coloring
- **Cleavage Summary Plots**: Bar charts showing N-terminal and C-terminal cleavage patterns
- **Comparison Heatmaps**: Side-by-side comparison of different experimental conditions

### Generated Files
- `*_heatmap.png`: Traditional sequence-based intensity heatmap (top N peptides)
- `*_positional_heatmap.png`: **NEW!** Amino acid position-based intensity heatmap
- `*_cleavage_summary.png`: N-terminal and C-terminal cleavage pattern analysis
- `comprehensive_cleavage_report.png`: **NEW!** Multi-panel comparative report with:
  - Positional heatmaps for each condition
  - Side-by-side cleavage pattern comparisons
  - Total intensity comparisons
  - Summary statistics table
- `comparison_heatmap.png`: Simple multi-condition comparison

## Positional Analysis Features

### 🧬 **NEW: Amino Acid Position-Based Analysis**

The enhanced visualization system now includes positional analysis that maps intensities to specific amino acid positions in your reference sequence:

- **Y-axis**: Amino acid positions (e.g., E1, A2, E3, D4, L5, ...)
- **X-axis**: Sample conditions  
- **Color intensity**: Log10-scaled peptide intensities

This provides insights into:
- Which amino acid positions show highest cleavage activity
- How cleavage patterns vary across experimental conditions
- Sequence regions with consistent or variable cleavage

### 📊 **Comprehensive Comparative Reports**

The new comprehensive report combines multiple analysis types in a single visualization:
- **Top row**: Positional heatmaps for each glucose condition (100, 200, 500 mgd)
- **Middle row**: Side-by-side cleavage pattern comparisons and total intensity analysis
- **Bottom row**: Summary statistics table

## File Compatibility

If you have older Excel formats (.xls), the tool will automatically convert them to the newer .xlsx format using pandas and xlrd.

## Examples

### Single Sheet Processing
```python
def example_single_sheet():
    mapper = AdvancedCleavageMapper('example_data_converted.xlsx')
    sample_names = ['AspN_Fxn2', 'AspN_Fxn3', 'AspN_Fxn4', 
                   'AspN_Fxn5', 'AspN_Fxn6', 'AspN_Fxn7', 'AspN_Fxn8']
    mapper.process('500 mgd glucose', '500 mgd PROCESSED', sample_names)
    mapper.save()
```

### Batch Processing
```python
def example_batch_processing():
    mapper = AdvancedCleavageMapper('your_data.xlsx')
    sample_names = ['AspN_Fxn2', 'AspN_Fxn3', 'AspN_Fxn4', 
                   'AspN_Fxn5', 'AspN_Fxn6', 'AspN_Fxn7', 'AspN_Fxn8']
    
    worksheets = [
        ('100 mgd glucose', '100 mgd PROCESSED'),
        ('200 mgd glucose', '200 mgd PROCESSED'),
        ('500 mgd glucose', '500 mgd PROCESSED')
    ]
    
    for input_ws, output_ws in worksheets:
        mapper.process(input_ws, output_ws, sample_names)
    
    mapper.save('batch_processed_output.xlsx')
```

### Creating Visualizations
```python
def example_with_visualizations():
    mapper = AdvancedCleavageMapper('example_data_converted.xlsx')
    sample_names = ['AspN_Fxn2', 'AspN_Fxn3', 'AspN_Fxn4', 
                   'AspN_Fxn5', 'AspN_Fxn6', 'AspN_Fxn7', 'AspN_Fxn8']
    
    # Process data and create visualizations
    mapper.process('500 mgd glucose', '500 mgd PROCESSED', sample_names)
    
    # Create heatmap and cleavage summary plots
    viz_files = mapper.create_visualizations(
        '500 mgd glucose', 
        sample_names, 
        'glucose_500mgd_analysis',
        top_n_peptides=25
    )
    
    mapper.save('output_with_viz.xlsx')
    print(f"Visualization files: {viz_files}")
```

## 🆘 Troubleshooting

### **Common Issues & Solutions**

**❓ "Python is not recognized"**
- Install Python from [python.org](https://python.org)
- Make sure to check "Add Python to PATH" during installation

**❓ "Package installation failed"**
- Try: `pip install --user -r requirements.txt`
- On Mac/Linux, try: `pip3 install -r requirements.txt`
- Run terminal/command prompt as administrator

**❓ "Excel file format not supported"**
- Tool automatically converts old .xls files to .xlsx
- Make sure your file isn't corrupted
- Try opening the file in Excel first

**❓ "No worksheets found" or "No sequences found"**
- Check that your data starts from **row 5** (row 4 = reference sequence)
- Worksheet names are case-sensitive
- Verify your data has the expected format (see Data Format section)

**❓ "GUI won't start"**
- Try the command line version: `python run_analysis.py your_file.xlsx`
- Check that tkinter is installed: `python -c "import tkinter"`

### **Data Format Requirements**
Your Excel file should have:
- **Row 4**: Reference sequence (full peptide sequence)
- **Row 5+**: Individual sequences with cleavage notation like `(E)PEPTIDE(S)`
- **Column A**: Sequence numbers
- **Column B**: Sequences with cleavage notation  
- **Columns C-I**: Intensity values for different samples

### **Getting Help**
1. Check the `examples/` folder for working examples
2. Run `python setup.py` to verify your installation
3. Look at the console output for detailed error messages

## 📜 License

This project is open source and free to use for research and commercial purposes.