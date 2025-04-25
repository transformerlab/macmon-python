from setuptools import setup, find_packages
import os
import platform
import sys
from pathlib import Path

# Get package directory
package_dir = Path(__file__).parent.resolve()

# Read the README file for the long description
with open(os.path.join(package_dir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Check platform compatibility
def check_platform_compatibility():
    """Check if the current platform is compatible (macOS with ARM)"""
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    is_compatible = (system == 'darwin' and ('arm' in machine or 'm1' in machine or 'm2' in machine))
    
    if not is_compatible:
        print("WARNING: macmon-python only works on macOS with Apple Silicon (ARM) chips", file=sys.stderr)
    
    return is_compatible

# Run platform check
check_platform_compatibility()

# Setup configuration
setup(
    name="macmon-python",
    version="0.1.1",
    description="Python wrapper for macmon binary (macOS Apple Silicon only)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ali Asaria",
    author_email="developers@transformerlab.ai",
    url="https://github.com/transformerlab/macmon-python",
    packages=find_packages(),
    include_package_data=True,  # This tells setuptools to include data files specified in MANIFEST.in
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: MacOS :: MacOS X",
    ],
    # Entry points for command-line scripts
    entry_points={
        "console_scripts": [
            "macmon-cli=macmon.cli:main",
        ],
    },
)