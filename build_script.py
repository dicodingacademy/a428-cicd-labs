# your_build_script.py

import subprocess

def install_dependencies():
    result = subprocess.run(["python3", "-m", "pip", "install", "-r", "requirements.txt"], capture_output=True)
    if result.returncode != 0:
        print("Error installing dependencies:")
        print(result.stderr.decode("utf-8"))
        exit(1)

def main():
    print("Building the Python project...")
    install_dependencies()
    print("Build completed successfully!")

if __name__ == "__main__":
    main()
