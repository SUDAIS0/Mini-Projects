import os
import subprocess

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

def display_menu():
    print("\nFile System Navigator")
    print("-" * 30)
    print("1. List contents of the current directory")
    print("2. Change directory")
    print("3. View file contents")
    print("4. Create a new folder")
    print("5. Create a new file")
    print("6. Delete a folder")
    print("7. Delete a file")
    print("8. Rename a folder")
    print("9. Rename a file")
    print("10. Edit a file")
    print("11. Execute a file")
    print("12. Go to parent directory")
    print("0. Exit")
    print("-" * 30)

def list_contents(path):
    try:
        contents = os.listdir(path)
        print("\nContents of", path)
        for item in contents:
            print("- ", item)
    except PermissionError:
        print("Permission denied: Cannot access this directory.")

def change_directory(current_path):
    new_dir = input("Enter the directory name to navigate into: ")
    new_path = os.path.join(current_path, new_dir)
    if os.path.isdir(new_path):
        return new_path
    else:
        print("Invalid directory.")
        return current_path

def view_file_contents(path):
    file_name = input("Enter the file name to view: ")
    file_path = os.path.join(path, file_name)
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as file:
                print("\nContents of", file_name)
                print("-" * 30)
                print(file.read())
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print("Invalid file.")

def create_new_folder(path):
    folder_name = input("Enter the name of the new folder: ")
    folder_path = os.path.join(path, folder_name)
    if os.path.exists(folder_path):
        print("Folder already exists.")
    else:
        try:
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}' created successfully at '{folder_path}'.")
        except Exception as e:
            print(f"Error creating folder: {e}")

def create_new_file(path):
    file_name = input("Enter the name of the new file: ")
    file_path = os.path.join(path, file_name)
    if os.path.exists(file_path):
        print("File already exists.")
    else:
        try:
            with open(file_path, 'w') as file:
                print(f"File '{file_name}' created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")

def delete_folder(path):
    folder_name = input("Enter the name of the folder to delete: ")
    folder_path = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
    else:
        try:
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_name}' and all its contents deleted successfully.")
        except Exception as e:
            print(f"Error deleting folder: {e}.")

def delete_file(path):
    file_name = input("Enter the name of the file to delete: ")
    file_path = os.path.join(path, file_name)
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_name}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")
    else:
        print("File not found.")

def rename_folder(path):
    current_name = input("Enter the current name of the folder: ")
    new_name = input("Enter the new name for the folder: ")

    current_path = os.path.join(path, current_name)
    new_path = os.path.join(path, new_name)

    if not os.path.exists(current_path):
        print("Folder does not exist.")
    elif os.path.exists(new_path):
        print("A folder with the new name already exists.")
    else:
        try:
            os.rename(current_path, new_path)
            print(f"Folder '{current_name}' renamed to '{new_name}' successfully.")
        except Exception as e:
            print(f"Error renaming folder: {e}")

def rename_file(path):
    current_name = input("Enter the current name of the file (with extension): ")
    new_name = input("Enter the new name for the file (with extension): ")
    
    current_file_path = os.path.join(path, current_name)
    new_file_path = os.path.join(path, new_name)

    if not os.path.exists(current_file_path):
        print(f"The file '{current_name}' does not exist.")
        return

    if os.path.exists(new_file_path):
        print(f"A file with the name '{new_name}' already exists.")
        return

    try:
        os.rename(current_file_path, new_file_path)
        print(f"File '{current_name}' renamed to '{new_name}' successfully.")
    except Exception as e:
        print(f"Error renaming file: {e}")

def edit_file(path):
    file_name = input("Enter the name of the file to edit: ")
    file_path = os.path.join(path, file_name)
    
    # Check if the file exists
    if os.path.isfile(file_path):
        try:
            # Open the file in nano editor
            subprocess.run(['notepad', file_path])
            print(f"File '{file_name}' edited successfully.")
        
        except Exception as e:
            print(f"Error editing file: {e}")
    else:
        print("File not found.")

def execute_file(path):
    file_name = input("Enter the name of the file to execute/open: ")
    file_path = os.path.join(path, file_name)

    if not os.path.exists(file_path):
        print("File not found.")
        return

    try:
        # For executable files (e.g., .exe, .bat)
        if file_path.endswith('.exe') or file_path.endswith('.bat'):
            subprocess.run(file_path, shell=True)

        # For other file types
        else:
            if os.name == 'nt':  # Windows
                # Use subprocess.run for blocking behavior
                subprocess.run(['cmd', '/c', 'start', '', file_path], shell=True)
            elif os.name == 'posix':  # macOS/Linux
                # Use open or xdg-open depending on the platform
                subprocess.run(['open' if sys.platform == 'darwin' else 'xdg-open', file_path])
                
        print(f"File '{file_name}' executed/opened successfully.")
    except Exception as e:
        print(f"Error executing/opening file: {e}")

def main():
    current_path = os.getcwd()
    
    while True:
        print("\nCurrent Directory:", current_path)
        display_menu()
        
        choice = input("Choose an option: ")
        clear_screen()

        if choice == '1':
            list_contents(current_path)
        elif choice == '2':
            current_path = change_directory(current_path)
        elif choice == '3':
            view_file_contents(current_path)
        elif choice == '4':
            create_new_folder(current_path)
        elif choice == '5':
            create_new_file(current_path)
        elif choice == '6':
            delete_folder(current_path)
        elif choice == '7':
            delete_file(current_path)
        elif choice == '8':
            rename_folder(current_path)
        elif choice == '9':
            rename_file(current_path)
        elif choice == '10':
            edit_file(current_path)
        elif choice == '11':
            execute_file(current_path)
        elif choice == '12':
            current_path = os.path.dirname(current_path)
        elif choice == '0':
            print("Exiting File System Navigator. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

