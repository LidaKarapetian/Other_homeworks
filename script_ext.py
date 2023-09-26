#!/usr/bin/python

#Python code in which there is a directory, we need to create new directories with the names of the file extensions in it
#and move the files with the corresponding extension into those directories

import os
import shutil

# Function to create new directories for file extensions
def create_new_directories(directory_name):
    for fname in os.listdir(directory_name):
        if os.path.isfile(os.path.join(directory_name, fname)):
            extension = get_file_extensions(fname)
            if extension:
                ext_directory = os.path.join(directory_name, extension[1:])
                os.makedirs(ext_directory, exist_ok=True)
                initial_dir_path = os.path.join(directory_name, fname)
                new_dir_path = os.path.join(ext_directory, fname)
                shutil.move(initial_dir_path, new_dir_path) # Move the file to the corresponding directory

# Function to get the file extension from a filename
def get_file_extensions(filename):
    _, file_ext = os.path.splitext(filename)  # '_' is a variable name used to "throw away" the base name of the file
     #and keep only the file extension in the extension variable.
    return file_ext.lower()


def main():
    directory_name = "directory_name"
    if os.path.exists(directory_name) and os.path.isdir(directory_name):
        create_new_directories(directory_name)
        print("Done")
    else:
        print("The directory doesn't exist or invalid directory name")

if __name__ == "__main__":
    main()