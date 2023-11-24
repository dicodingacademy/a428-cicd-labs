import subprocess
import sys

def install_dependencies():
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    subprocess.run(["venv/bin/python", "-m", "pip", "install", "-r", "requirements.txt"])

def main():
    print("Building the Python project...")
    install_dependencies()
    # Add additional build steps as needed
    print("Build completed successfully!")

if __name__ == "__main__":
    main()
