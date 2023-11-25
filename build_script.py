import subprocess
import sys

def install_dependencies():
    try:
        print("Installing dependencies...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        subprocess.run(["venv/bin/python", "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    print("Building the Python project...")
    install_dependencies()
    # Add additional build steps as needed
    print("Build completed successfully!")

if __name__ == "__main__":
    main()
