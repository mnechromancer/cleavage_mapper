# Output Directory

This directory contains the results of cleavage mapping analysis.

## Generated Files

When you run the cleavage mapper, the following types of files will be created here:

### Excel Reports
- `cleavage_analysis_results.xlsx` - Main analysis results with peptide data
- `cleavage_mapper_output.xlsx` - Detailed cleavage mapping results

### Visualizations
- `*_heatmap.png` - Traditional sequence-based heatmaps
- `*_positional_heatmap.png` - Amino acid position-based heatmaps  
- `*_cleavage_summary.png` - Cleavage pattern summary charts
- `comprehensive_cleavage_report.png` - Multi-condition comparison report

### Organization
- Results are automatically organized by analysis run
- Each run creates its own subdirectory with timestamp
- Files are named with condition identifiers (e.g., 100mgd, 200mgd, 500mgd)

## Note
Files in this directory are excluded from version control (.gitignore) to keep the repository clean, but the directory structure is preserved for functionality.