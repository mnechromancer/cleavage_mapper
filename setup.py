#!/usr/bin/env python3
"""
CLEAVAGE MAPPER SETUP
Automatic setup script for non-programmers
"""

import subprocess
import sys
import os
from pathlib import Path

def print_header():
    print("🧬 CLEAVAGE MAPPER SETUP")
    print("=" * 40)
    print("Setting up your peptide analysis environment...")
    print()

def check_python():
    """Check Python version"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python {version.major}.{version.minor} detected")
        print("⚠️  Python 3.7 or higher is required")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
    return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    
    requirements_file = Path("requirements.txt")
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    try:
        # Install packages
        cmd = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ All packages installed successfully!")
            return True
        else:
            print(f"❌ Installation failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Installation error: {e}")
        return False

def test_imports():
    """Test if all required modules can be imported"""
    print("\n🔧 Testing package imports...")
    
    required_modules = [
        ('openpyxl', 'Excel file handling'),
        ('pandas', 'Data processing'),
        ('matplotlib', 'Plotting'),
        ('seaborn', 'Advanced plotting'),
        ('numpy', 'Numerical operations'),
        ('tkinter', 'User interface')
    ]
    
    all_good = True
    for module, description in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} - {description}")
        except ImportError:
            print(f"❌ {module} - {description} (FAILED)")
            all_good = False
    
    return all_good

def create_shortcuts():
    """Create easy-to-use shortcuts"""
    print("\n🔗 Creating user-friendly shortcuts...")
    
    # Create a simple start script
    start_script_content = '''#!/usr/bin/env python3
"""
EASY START - Cleavage Mapper
Double-click this file to start the analysis tool!
"""

import sys
import os
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def main():
    print("🧬 Starting Cleavage Mapper...")
    print("Choose your preferred interface:")
    print("1. Graphical Interface (recommended for beginners)")
    print("2. Command Line Interface")
    print("3. Quick analysis with example data")
    print()
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            try:
                from cleavage_mapper_gui import main as gui_main
                gui_main()
                break
            except Exception as e:
                print(f"GUI failed to start: {e}")
                print("Falling back to command line...")
                choice = "2"
        
        if choice == "2":
            print("\\nCommand line mode:")
            print("Usage: python run_analysis.py your_file.xlsx")
            break
        
        elif choice == "3":
            try:
                from run_analysis import main as cli_main
                # Use example data if available
                if Path("example_data_converted.xlsx").exists():
                    sys.argv = ["start.py", "example_data_converted.xlsx"]
                else:
                    sys.argv = ["start.py", "example_data.xlsx"]
                cli_main()
                break
            except Exception as e:
                print(f"Quick analysis failed: {e}")
        
        else:
            print("Please enter 1, 2, or 3")

if __name__ == "__main__":
    main()
'''
    
    with open("START_HERE.py", "w") as f:
        f.write(start_script_content)
    
    print("✅ Created START_HERE.py - double-click this to begin!")
    
    return True

def main():
    print_header()
    
    # Check Python version
    if not check_python():
        input("Press Enter to exit...")
        return
    
    # Install packages
    if not install_requirements():
        print("\n⚠️  Package installation failed. You may need to:")
        print("   - Run as administrator/with sudo")
        print("   - Use: pip install --user -r requirements.txt")
        input("Press Enter to continue anyway...")
    
    # Test imports
    if not test_imports():
        print("\n⚠️  Some packages failed to import. The tool may not work properly.")
        input("Press Enter to continue anyway...")
    
    # Create shortcuts
    create_shortcuts()
    
    # Final instructions
    print("\n🎉 SETUP COMPLETE!")
    print("=" * 30)
    print("To start using Cleavage Mapper:")
    print("1. Double-click 'START_HERE.py' for the easiest experience")
    print("2. Or run: python cleavage_mapper_gui.py for the graphical interface")
    print("3. Or run: python run_analysis.py your_file.xlsx for command line")
    print()
    print("📖 See README.md for detailed instructions")
    print("🆘 Having issues? Check the troubleshooting section in README.md")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()