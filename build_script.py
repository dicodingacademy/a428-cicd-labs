import subprocess
import sys

def install_dependencies():
    subprocess.run([sys.executable, "-m", "venv", "venv"])
    subprocess.run(["venv/bin/python", "-m", "pip", "install", "-r", "requirements.txt"])
    if result.returncode != 0:
        print("Error installing dependencies:")
        print(result.stderr.decode("utf-8"))
        exit(1)

def main():
    print("Building the Python project...")
    install_dependencies()
    # Add additional build steps as needed
    print("Build completed successfully!")

if __name__ == "__main__":
    main()
