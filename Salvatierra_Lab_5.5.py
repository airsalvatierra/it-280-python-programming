import zipfile
import os


file_name1 = 'random_file_lab53.txt'
file_name2 = 'random_file_lab54.txt'

# Created directory on the root app directory
folder = 'Zip'
os.makedirs(folder, exist_ok=True)

# This path works in any OS
path_to_zip_file = os.path.join(folder, 'compressed_files.zip')

# Compress files in 1 file
with zipfile.ZipFile(path_to_zip_file, 'w') as zip:
    zip.write(file_name1)
    zip.write(file_name2)
