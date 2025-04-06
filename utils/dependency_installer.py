import subprocess
import sys

# Ensure dependencies are installed
def install_dependencies():
    """
    Installs all libraries located inside the requirements.txt

    Args
        - The path is automatic no inputs for the user are required.
        - Path location for requirements.txt
    
    Returns
        - sys.executable for pip install requirements in requirements.txt
        - print statement for Successul installation
    """
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read().splitlines()
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *requirements])
        print(f"Dependencies Installed Successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)

# Install dependencies on startup if not already installed
install_dependencies()