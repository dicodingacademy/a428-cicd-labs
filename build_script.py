# your_build_script.py

import subprocess

def install_dependencies():
    subprocess.run(["python3", "-m", "pip", "install", "-r", "requirements.txt"])

def main():
    print("Building the Python project...")
    install_dependencies()
    # Tambahkan langkah-langkah build tambahan sesuai kebutuhan

if __name__ == "__main__":
    main()
