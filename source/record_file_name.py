import os

def traverse_directory(folder_path, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                file.write(filename + '\n')

# set the folder want to find and the output path
folder_path = '/path/to/your/folder'
output_file = 'file_names.txt'

# find all the file and record to txt
traverse_directory(folder_path, output_file)
