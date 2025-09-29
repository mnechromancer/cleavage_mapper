# 🧬 Cleavage Mapper - User Guide

## 🚀 Getting Started (3 Easy Steps!)

### Step 1: Install
- **Option A**: Double-click `setup.py` (automatic)
- **Option B**: Run `pip install -r requirements.txt` in terminal

### Step 2: Prepare Your Data
Your Excel file should have:
- **Row 4**: Full reference peptide sequence
- **Row 5+**: Individual sequences with cleavage notation like `(E)PEPTIDE(S)`
- **Column A**: Sequence numbers  
- **Column B**: Sequences
- **Columns C+**: Intensity values for each sample

### Step 3: Run Analysis
- **Easiest**: Double-click `START_HERE.py`
- **GUI**: Run `python cleavage_mapper_gui.py`  
- **Command Line**: Run `python run_analysis.py your_file.xlsx`

---

## 📊 What You'll Get

### Excel Output
- **Processed worksheets** with calculated formulas
- **Left panel**: N-terminal cleavage analysis
- **Right panel**: C-terminal cleavage analysis
- **Summary statistics**: Totals and percentages

### Visualizations
- **📈 Sequence Heatmaps**: Individual peptide sequences vs samples
- **🧬 Positional Heatmaps**: Amino acid positions vs samples (NEW!)  
- **📊 Cleavage Summaries**: N-terminal and C-terminal patterns
- **📋 Comprehensive Report**: All conditions compared side-by-side

---

## 💡 Pro Tips

### For Best Results:
- Use consistent sample naming across worksheets
- Include reference sequence in row 4
- Use proper cleavage notation: `(ResidueLeft)SEQUENCE(ResidueRight)`
- Keep worksheet names descriptive (e.g., "100 mgd glucose")

### Understanding Positional Heatmaps:
- **Y-axis**: Each amino acid position (E1, A2, E3, etc.)
- **X-axis**: Your sample conditions
- **Colors**: Intensity levels (log scale for wide ranges)
- **Purpose**: See which amino acid positions show most cleavage activity

### Sample Names:
Default: `AspN_Fxn2, AspN_Fxn3, AspN_Fxn4, AspN_Fxn5, AspN_Fxn6, AspN_Fxn7, AspN_Fxn8`

You can customize these in the GUI or command line.

---

## 🎯 Example Workflow

1. **Load your Excel file** with peptide cleavage data
2. **Select worksheets** (e.g., "100 mgd glucose", "200 mgd glucose", "500 mgd glucose")
3. **Choose output folder** for results
4. **Run analysis** - tool processes everything automatically
5. **Review results**:
   - Open `comprehensive_comparison_report.png` for overview
   - Check individual heatmaps for detailed analysis
   - Use Excel file for further calculations

---

## 🆘 Common Issues

**"No positional data to plot"**
- Some worksheets may not have peptides that map to reference sequence
- This is normal - tool will skip positional analysis for those sheets

**"File format not supported"**  
- Tool automatically converts old Excel formats
- Make sure file isn't corrupted

**Visualization files in wrong location**
- Check your specified output folder
- Files are organized by analysis type

**GUI won't start**
- Try command line version instead
- Check Python and tkinter installation

---

## 📁 File Organization

After analysis, your output folder contains:
```
output_folder/
├── 📋 cleavage_analysis_results.xlsx          # Main Excel results
├── 📊 analysis_*_heatmap.png                  # Sequence heatmaps  
├── 📊 analysis_*_positional_heatmap.png       # Position heatmaps
├── 📊 analysis_*_cleavage_summary.png         # Cleavage patterns
└── 📊 comprehensive_comparison_report.png     # Complete comparison
```

---

## 🔧 Advanced Usage

### Command Line Options
```bash
# Basic usage
python run_analysis.py data.xlsx

# Custom output folder  
python run_analysis.py data.xlsx --output my_results

# Custom sample names
python run_analysis.py data.xlsx --samples "S1,S2,S3,S4,S5,S6,S7"

# Specific worksheets only
python run_analysis.py data.xlsx --worksheets "100 mgd,200 mgd"
```

### Batch Processing
The tool automatically processes multiple worksheets and creates comparative analysis across all conditions.

---

## 🏆 Best Practices

1. **Organize your data** consistently across all worksheets
2. **Use descriptive names** for conditions and samples  
3. **Check the reference sequence** is correct in row 4
4. **Review all outputs** - each visualization shows different insights
5. **Keep original files** - tool creates new processed versions

---

Happy analyzing! 🧬✨