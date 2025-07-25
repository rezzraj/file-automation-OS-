import sys
import os
import shutil


source_folder=input('Enter the complete source path of source folder: ')
name_prefix=input('Enter the new name prefix: ')
new_folder_name=input('Enter the new folder name to save files: ')

parent_dir=os.path.dirname(source_folder)
destination_folder=os.path.join(parent_dir,new_folder_name)

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
else:
    print('the folder already exists')
    sys.exit()

file_list=os.listdir(source_folder)
count= 1

for file in file_list:
    file_path= os.path.join(source_folder,file)

    if os.path.isfile(file_path):
        file_ext=os.path.splitext(file)[1]
        new_file_name=f"{name_prefix}{count}{file_ext}"
        new_path= os.path.join(destination_folder, new_file_name)


        shutil.copy(file_path,new_path)
        count+=1

print("done")