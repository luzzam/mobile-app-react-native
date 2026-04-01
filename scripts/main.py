# main.py
import os
import argparse
import subprocess
import sys

def install_dependencies():
    """Installs dependencies using npm or yarn, prioritizing yarn."""
    try:
        subprocess.run(["yarn", "--version"], check=True, capture_output=True)
        print("Yarn found, installing dependencies with yarn...")
        subprocess.run(["yarn", "install"], check=True)
    except FileNotFoundError:
        print("Yarn not found, installing dependencies with npm...")
        subprocess.run(["npm", "install"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def run_react_native(platform="ios"):
    """Runs the React Native application for the specified platform."""
    try:
        if platform == "ios":
            print("Running on iOS...")
            subprocess.run(["npx", "react-native", "run-ios"], check=True)
        elif platform == "android":
            print("Running on Android...")
            subprocess.run(["npx", "react-native", "run-android"], check=True)
        else:
            print(f"Invalid platform: {platform}. Supported platforms are 'ios' and 'android'.")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running React Native: {e}")
        sys.exit(1)

def lint_code():
    """Lints the code using ESLint."""
    try:
        print("Linting code...")
        subprocess.run(["npx", "eslint", "."], check=True)
    except subprocess.CalledProcessError as e:
        print(f"ESLint found errors: {e}")
        sys.exit(1)

def format_code():
    """Formats the code using Prettier."""
    try:
        print("Formatting code...")
        subprocess.run(["npx", "prettier", "--write", "."], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Prettier failed: {e}")
        sys.exit(1)

def main():
    """Main function to parse arguments and execute commands."""
    parser = argparse.ArgumentParser(description="React Native CLI Helper")
    parser.add_argument("command", choices=["install", "run", "lint", "format"], help="Command to execute")
    parser.add_argument("--platform", choices=["ios", "android"], default="ios", help="Platform to run on (ios or android)")

    args = parser.parse_args()

    if args.command == "install":
        install_dependencies()
    elif args.command == "run":
        run_react_native(args.platform)
    elif args.command == "lint":
        lint_code()
    elif args.command == "format":
        format_code()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()