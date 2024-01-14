import os
def replace_text_in_files_and_filenames(folder_path, original_text, new_text):
    """
    Replace text in all files and their filenames within the given folder.

    :param folder_path: Path to the folder containing files.
    :param original_text: Text to be replaced in files and filenames.
    :param new_text: Text to replace with.
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Replace text in file contents
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_contents = f.read()
                
                file_contents = file_contents.replace(original_text, new_text)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(file_contents)
            except Exception as e:
                print(f"Error processing file contents of {file_path}: {e}")

            # Replace text in filename
            new_file_path = os.path.join(root, file.replace(original_text, new_text))
            try:
                if file_path != new_file_path:
                    os.rename(file_path, new_file_path)
            except Exception as e:
                print(f"Error renaming file {file_path} to {new_file_path}: {e}")

replace_Dir="./oolong"


# Example usage (commented out to prevent execution)
replace_text_in_files_and_filenames(replace_Dir, 'superior', 'oolong')
replace_text_in_files_and_filenames(replace_Dir, 'Superior', 'Oolong')
replace_text_in_files_and_filenames(replace_Dir, 'SUPERIOR', 'OOLONG')
