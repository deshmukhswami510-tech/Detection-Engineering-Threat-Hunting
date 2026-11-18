
import yaml
import os

def validate_yaml_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            yaml.safe_load(file)

        print(f"[SUCCESS] {file_path} is valid YAML.")

    except yaml.YAMLError as error:
        print(f"[ERROR] Invalid YAML: {error}")

    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")


if __name__ == "__main__":
    print("=== YAML VALIDATOR ===")

    file_path = input("Enter YAML file path: ")
    validate_yaml_file(file_path)


