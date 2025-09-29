# Cleavage Mapper - Project Summary

## What This Tool Does
The Cleavage Mapper analyzes peptide cleavage patterns from mass spectrometry data, providing both traditional sequence-based analysis and advanced positional amino acid analysis with comprehensive visualizations.

## Key Features Implemented
✅ **Core Analysis Engine** - Bidirectional peptide cleavage mapping  
✅ **Traditional Heatmaps** - Individual sequence intensity visualization  
✅ **Positional Heatmaps** - Amino acid position-based analysis (Y-axis shows amino acids, not individual sequences)  
✅ **Comprehensive Reports** - Multi-condition comparative visualizations (100, 200, 500 mgd)  
✅ **User-Friendly GUI** - Point-and-click interface for non-programmers  
✅ **Command-Line Interface** - Advanced batch processing capabilities  
✅ **Professional Structure** - Clean, organized codebase  

## Directory Structure
```
cleavage_mapper/
├── START_HERE.py          # Main entry point - start here!
├── run_analysis.py        # Command-line interface
├── setup.py              # Automatic installation
├── requirements.txt       # Dependencies
├── README.md             # Full documentation
├── src/                  # Core source code
├── data/                 # Sample data files
├── docs/                 # User guides
├── examples/             # Advanced usage examples
└── output/               # Analysis results
```

## How to Use
1. **For beginners**: Run `python START_HERE.py` and choose option 1 (GUI)
2. **For advanced users**: Use `python run_analysis.py` with command-line arguments
3. **For developers**: See examples/ directory for advanced usage

## Generated Outputs
- Excel files with detailed cleavage analysis
- Traditional heatmaps showing sequence intensities
- Positional heatmaps showing amino acid patterns
- Cleavage summary visualizations
- Comprehensive multi-condition comparison reports

## Installation
Run `python setup.py` for automatic environment setup and dependency installation.

---
*This project evolved from a simple script to a comprehensive analysis tool with professional structure and user-friendly interfaces.*