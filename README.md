# Cleavage Mapping Excel Pipeline

An **Excel-only cleavage mapping pipeline** for bioinformatics data processing, focusing on protein sequence analysis with Left/Right cleavage anchor points.

## Overview

This project provides a formula-driven automation solution (no VBA required) for processing protein sequence data through Excel templates. The pipeline processes raw CSV data through calculation sheets to produce dynamic Left-anchored and Right-anchored cleavage tables.

## Quick Start

1. **Open Template**: Use `excel/CleavagePipeline_Template.xlsx`
2. **Paste Data**: Copy your CSV data into the appropriate Raw sheets (`Raw_100`, `Raw_200`, `Raw_500`)
3. **View Results**: Calculation sheets auto-update with processed cleavage analysis

## Project Structure

```
/excel/          # Excel template workbooks
/docs/           # Technical documentation (FORMULAS.md, WORKFLOW.md)  
/data/           # Sample CSV files for testing
/tracking/       # Project management and backlog
```

## Key Features

- **Pure Excel formulas** - No VBA or external scripts required
- **Multi-concentration support** - 100/200/500 mgd processing
- **Dynamic output tables** - Left-anchored and Right-anchored views
- **Template-based workflow** - Copy-paste CSV data for instant results
- **Residue analysis** - Automated LeftResidue/RightResidue extraction

## Documentation

- [`docs/FORMULAS.md`](docs/FORMULAS.md) - Technical formula reference
- [`docs/WORKFLOW.md`](docs/WORKFLOW.md) - Step-by-step user guide
- [`tracking/cleavage_pipeline_backlog.md`](tracking/cleavage_pipeline_backlog.md) - Development roadmap

## Requirements

- Modern Excel with dynamic array support (Office 365/Excel 2021+)
- Functions used: `FILTER`, `SORTBY`, `HSTACK`, `BYCOL` (optional)

## Sample Data

Test the pipeline with provided sample files:
- `data/sample_100mgd.csv`
- `data/sample_200mgd.csv`  
- `data/sample_500mgd.csv`

## Getting Started

1. Download `excel/CleavagePipeline_Template.xlsx`
2. Open in Excel (Office 365 recommended)
3. Paste sample data from `/data/` folder into Raw sheets
4. Review calculated results in Calc sheets
5. Refer to `docs/WORKFLOW.md` for detailed instructions

## License

MIT License - see [`LICENSE`](LICENSE) for details.

## Contributing

This project follows the development roadmap in `tracking/cleavage_pipeline_backlog.md`. The pipeline is designed for bioinformatics researchers who need Excel-based protein sequence analysis without programming requirements.