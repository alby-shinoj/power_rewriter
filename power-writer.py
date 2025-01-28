import os

def rename_files_and_directories(directory, old_word, new_word):
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory, topdown=False):
        # Rename files first
        for filename in files:
            file_path = os.path.join(root, filename)
            new_filename = filename.replace(old_word, new_word)
            new_file_path = os.path.join(root, new_filename)
            
            # Rename the file if the new name is different
            if new_filename != filename:
                os.rename(file_path, new_file_path)
                print(f'Renamed file: {file_path} -> {new_file_path}')
                file_path = new_file_path  # Update file_path to the new path
            
            # Replace content in the file
            replace_file_content(file_path, old_word, new_word)
        
        # Rename directories
        for dirname in dirs:
            dir_path = os.path.join(root, dirname)
            new_dirname = dirname.replace(old_word, new_word)
            new_dir_path = os.path.join(root, new_dirname)
            
            # Rename the directory if the new name is different
            if new_dirname != dirname:
                os.rename(dir_path, new_dir_path)
                print(f'Renamed directory: {dir_path} -> {new_dir_path}')

def replace_file_content(file_path, old_word, new_word):
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace the old word with the new word in the content
        new_content = content.replace(old_word, new_word)
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f'Updated content in file: {file_path}')
    except Exception as e:
        print(f'Error processing file {file_path}: {e}')

def main():
    # Take directory path as input from the user
    directory = input("Enter the directory path: ").strip()
    
    # Validate if the directory exists
    if not os.path.isdir(directory):
        print("Error: The specified directory does not exist.")
        return
    
    # Take the word to be replaced as input from the user
    old_word = input("Enter the word to be replaced: ").strip()
    
    # Take the new word as input from the user
    new_word = input("Enter the new word: ").strip()
    
    # Call the function to rename files and directories and update file content
    rename_files_and_directories(directory, old_word, new_word)

if __name__ == "__main__":
    main()