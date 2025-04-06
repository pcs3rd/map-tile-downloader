import subprocess
import sys

# Ensure dependencies are installed
def install_dependencies():
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read().splitlines()
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *requirements])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)

# Install dependencies on startup if not already installed
install_dependencies()