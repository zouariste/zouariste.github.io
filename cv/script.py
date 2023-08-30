import os
import platform
import subprocess

def clear_screen():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def install_dependencies():
    # Install pre-commit using pip
    subprocess.run(["pip3", "install", "pre-commit"])

    system = platform.system()
    if system == "Windows":
        # Windows installation steps
        subprocess.run(["git", "clone", "https://github.com/awslabs/git-secrets.git"])
        subprocess.run(["powershell", "git-secrets/install.ps1"])
        subprocess.run(["rm", "-rf", "git-secrets"])
    else:
        # macOS installation steps
        try:
            subprocess.run(["brew", "install", "git-secrets"], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
        	print(f"Error installing git-secrets: {e.stderr.decode('utf-8')}")

def configure_git_secrets():
    # Common configuration steps for both macOS and Windows
    subprocess.run(["git", "secrets", "--add", "sshpass|password|pwd|passwd|pass[\\W_]", "--global"])
    subprocess.run(["git", "secrets", "--add", "[-]{5}BEGIN", "--global"])
    subprocess.run(["git", "secrets", "--add", "EAACEdEose0cBA[0-9A-Za-z]+", "--global"])
    subprocess.run(["git", "secrets", "--add", "[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com", "--global"])
    subprocess.run(["git", "secrets", "--add", "AKIA[0-9A-Z]{16}", "--global"])
    subprocess.run(["git", "secrets", "--add", "[0-9a-fA-F]{7}\\.[0-9a-fA-F]{32}", "--global"])
    subprocess.run(["git", "secrets", "--add", "^(sha)?[1-9][0-9]+-[0-9a-zA-Z]{40}", "--global"])
    subprocess.run(["git", "secrets", "--add", "key-[0-9a-zA-Z]{32}", "--global"])
    subprocess.run(["git", "secrets", "--add", "[0-9a-f]{32}-us[0-9]{1,2}", "--global"])

def main():

    # Install dependencies and configure git-secrets
    install_dependencies()
    configure_git_secrets()


    # Print a message for manual steps
    print("\n**IMPORTANT:**")
    print("After running this script, you need to manually run the following commands under each repo:")
    print("1. git secrets --install")
    print("2. pre-commit install")


if __name__ == "__main__":
    main()

