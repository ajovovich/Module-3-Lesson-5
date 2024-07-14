import os

def list_directory_contents(path):
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                print("File:", entry)
            elif os.path.isdir(full_path):
                print("Directory:", entry)
    except FileNotFoundError:
        print("Invalid path or directory does not exist.")
    except PermissionError:
        print("Permission denied to access the directory.")

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    list_directory_contents(path)