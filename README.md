# **File Renamer & Organizer**

### **Overview**
This Python script automates the process of **renaming files with a custom prefix** and **organizing them into a new folder**.  
It is useful when you have multiple files and want to **rename them sequentially** (e.g., `image1.jpg`, `image2.jpg`) and **store them in a separate directory** without affecting the original files.

---

## **Features**
✔ Takes **source folder path** as input  
✔ Lets you set a **custom prefix for renamed files**  
✔ Creates a **new folder** for renamed files  
✔ Preserves **file extensions**  
✔ Prevents overwriting by checking if the destination folder already exists  

---

## **How It Works**
1. **User Inputs:**
   - `Source Folder Path` – Path of the original files.
   - `Name Prefix` – Prefix for renamed files (e.g., `image`, `doc`).
   - `New Folder Name` – Folder to save renamed files.

2. **Script Actions:**
   - Creates the new folder inside the **same parent directory** as the source folder.
   - Renames files sequentially:  
     Example:  
     ```
     image1.jpg  
     image2.jpg  
     image3.jpg
     ```
   - Copies renamed files into the new folder.

---

## **Code Snippet**
```python
import sys
import os
import shutil

source_folder = input('Enter the complete source path of source folder: ')
name_prefix = input('Enter the new name prefix: ')
new_folder_name = input('Enter the new folder name to save files: ')

parent_dir = os.path.dirname(source_folder)
destination_folder = os.path.join(parent_dir, new_folder_name)

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
else:
    print('The folder already exists')
    sys.exit()

file_list = os.listdir(source_folder)
count = 1

for file in file_list:
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1]
        new_file_name = f"{name_prefix}{count}{file_ext}"
        new_path = os.path.join(destination_folder, new_file_name)
        shutil.copy(file_path, new_path)
        count += 1

print("Done!")
