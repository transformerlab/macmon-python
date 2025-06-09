import asyncio
import json
import os
import platform
import subprocess
from pathlib import Path
from typing import Any, Dict, Optional


class MacMonError(Exception):
    """Exception raised for errors in the MacMon class."""
    pass


class MacMon:
    """
    A wrapper for the macmon binary that outputs system metrics as JSON.
    Only works on macOS with Apple Silicon (ARM) chips.
    """
    def __init__(self, binary_path: Optional[str] = None):
        """
        Initialize the MacMon class.
        
        Args:
            binary_path: Optional path to the binary. If not provided, will use the bundled binary.
        """
        # Check for macOS with ARM chip
        system = platform.system().lower()
        machine = platform.machine().lower()
        
        if system != 'darwin' or not ('arm' in machine or 'm1' in machine or 'm2' in machine):
            raise MacMonError("MacMon only supports macOS with Apple Silicon (ARM) chips")
            
        if binary_path:
            self.binary_path = binary_path
        else:
            # Get the directory where this module is located
            module_dir = Path(os.path.dirname(os.path.abspath(__file__)))
            self.binary_path = str(module_dir / "bin" / "macmon")
        
        # Ensure the binary exists and is executable
        if not os.path.isfile(self.binary_path):
            raise MacMonError(f"Binary not found at: {self.binary_path}")
        
        # Make the binary executable if it's not already
        if not os.access(self.binary_path, os.X_OK):
            try:
                os.chmod(self.binary_path, 0o755)  # rwx r-x r-x
            except OSError as e:
                raise MacMonError(f"Failed to make binary executable: {e}")

    def get_metrics(self) -> Dict[str, Any]:
        """
        Run the binary and return the metrics as a Python dictionary.
        
        Returns:
            A dictionary containing system metrics.
            
        Raises:
            MacMonError: If there's an error running the binary.
        """
        try:
            # Run the binary with the argument -s 1 and capture its output
            result = subprocess.run(
                [self.binary_path, "pipe", "-s", "1", "--soc-info"],
                capture_output=True,
                text=True,
                check=True
            )
            
            return result.stdout
        
        except subprocess.CalledProcessError as e:
            raise MacMonError(f"Error running binary: {e.stderr}")
        except json.JSONDecodeError as e:
            raise MacMonError(f"Error parsing JSON output: {e}")
        
    async def get_metrics_async(self) -> Dict[str, Any]:
        """
        Asynchronously run the binary and return the metrics as a Python dictionary.
        """
        try:
            proc = await asyncio.create_subprocess_exec(
                self.binary_path, "pipe", "-s", "1", "--soc-info",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await proc.communicate()

            if proc.returncode != 0:
                raise MacMonError(f"Error running binary: {stderr.decode().strip()}")

            return stdout.decode().strip()

        except json.JSONDecodeError as e:
            raise MacMonError(f"Error parsing JSON output: {e}")