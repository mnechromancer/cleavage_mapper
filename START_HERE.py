#!/usr/bin/env python3
"""
🧬 CLEAVAGE MAPPER - START HERE!

Double-click this file to begin peptide cleavage analysis!

This is the easiest way to get started - no programming required.
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
current_dir = Path(__file__).parent
src_dir = current_dir / "src"
sys.path.insert(0, str(src_dir))
sys.path.insert(0, str(current_dir))

def print_welcome():
    print("=" * 60)
    print("🧬 WELCOME TO CLEAVAGE MAPPER")
    print("=" * 60)
    print("Professional Peptide Cleavage Analysis Tool")
    print("No programming experience required!")
    print()

def main():
    print_welcome()
    
    print("Choose how you'd like to analyze your data:")
    print()
    print("1. 🖱️  Graphical Interface (RECOMMENDED)")
    print("   → Easy point-and-click interface")
    print("   → Perfect for beginners")
    print()
    print("2. ⌨️  Command Line Interface") 
    print("   → For advanced users")
    print("   → Faster for batch processing")
    print()
    print("3. 📊 Quick Demo with Example Data")
    print("   → See the tool in action")
    print("   → Uses included sample data")
    print()
    print("4. 🔧 Setup & Installation Check")
    print("   → Verify everything is installed correctly")
    print("   → Install missing packages")
    print()
    
    while True:
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == "1":
                print("\n🚀 Starting Graphical Interface...")
                try:
                    from cleavage_mapper_gui import main as gui_main
                    gui_main()
                    break
                except ImportError as e:
                    print(f"❌ GUI unavailable: {e}")
                    print("📦 Try running setup first (option 4)")
                    print("⚡ Or use command line interface (option 2)")
                    continue
                except Exception as e:
                    print(f"❌ GUI failed to start: {e}")
                    print("⚡ Try command line interface instead")
                    continue
            
            elif choice == "2":
                print("\n⌨️  Command Line Interface:")
                print("Usage examples:")
                print("  python run_analysis.py your_file.xlsx")
                print("  python run_analysis.py your_file.xlsx --output results")
                print()
                print("📁 Drag and drop your Excel file here, then press Enter:")
                file_path = input().strip().strip('"').strip("'")
                
                if file_path and Path(file_path).exists():
                    print(f"\n🔬 Analyzing: {Path(file_path).name}")
                    # Import and run analysis
                    try:
                        from run_analysis import main as cli_main
                        sys.argv = ["run_analysis.py", file_path]
                        cli_main()
                    except Exception as e:
                        print(f"❌ Analysis failed: {e}")
                else:
                    print("❌ File not found. Please check the path and try again.")
                break
            
            elif choice == "3":
                print("\n📊 Running Quick Demo...")
                try:
                    # Look for example data in data directory
                    data_dir = current_dir / "data"
                    example_files = [
                        data_dir / "example_data_converted.xlsx",
                        data_dir / "example_data.xlsx"
                    ]
                    
                    example_file = None
                    for file in example_files:
                        if file.exists():
                            example_file = str(file)
                            break
                    
                    if example_file:
                        print(f"📁 Using example file: {example_file}")
                        from run_analysis import main as cli_main
                        sys.argv = ["run_analysis.py", example_file, "--output", "output/demo_results"]
                        cli_main()
                    else:
                        print("❌ No example data found.")
                        print("💡 Place your Excel file in this folder and choose option 2")
                        
                except Exception as e:
                    print(f"❌ Demo failed: {e}")
                    import traceback
                    traceback.print_exc()
                break
            
            elif choice == "4":
                print("\n🔧 Running Setup Check...")
                try:
                    # Import setup and run
                    import setup
                    setup.main()
                except Exception as e:
                    print(f"❌ Setup check failed: {e}")
                    print("📦 Try running: pip install -r requirements.txt")
                break
            
            else:
                print("❌ Please enter 1, 2, 3, or 4")
                continue
                
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for using Cleavage Mapper!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            print("💡 Try option 4 to check your installation")
            continue
    
    print("\n" + "=" * 60)
    print("🧬 CLEAVAGE MAPPER")  
    print("💡 Need help? Check README.md or USER_GUIDE.md")
    print("🆘 Having issues? Check the troubleshooting section")
    print("=" * 60)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        print("📋 Please check that you have Python 3.7+ installed")
        print("📦 And run: pip install -r requirements.txt")
        input("\nPress Enter to exit...")