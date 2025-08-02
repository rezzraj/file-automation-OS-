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
