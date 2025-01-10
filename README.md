---

# File-Hunt

**File-Hunt** is a Python script that helps you compare the files in a **source directory** with those listed in a **target CSV file**. It identifies files that exist in the source directory but do not appear in the target file list, even across multiple subfolders.

---

## Features

- **Cross-platform**: Works on Windows, Linux, and MacOS by normalizing file paths.
- **Subfolder Support**: The script checks files in all subdirectories of the source directory.
- **Missing Files Report**: Identifies files that exist in the source but are missing from the target CSV list.
- **Progress Bar**: Displays a progress bar during the file comparison process for better feedback.
- **Summary Table**: Outputs a summary table of missing files in the console.
- **File Export**: Saves a list of missing files to a text file.

---

## Requirements

- **Python 3.6+**
- **Required Libraries**:
  - `pandas`
  - `tqdm`
  - `tabulate`

You can install the required libraries using `pip`:

```bash
pip install pandas tqdm tabulate
```

---

## Usage

### 1. Clone this repository

```bash
git clone https://github.com/your-username/file-hunt.git
cd file-hunt
```

### 2. Run the script

After cloning the repository, navigate to the directory where the script is located. Run the script with the following command:

```bash
python file_hunt.py
```

### 3. Provide Inputs

The script will prompt you for the following inputs:

- **Source Directory**: The local directory containing the files you want to compare.
- **Target CSV File**: The path to the CSV file that contains the list of target files.
- **Target Column Name**: The column name in the CSV file that contains the file paths.

### 4. Script Output

The script will display the total number of files in the source that are missing from the target directory, along with a summary table of those files. The missing files will also be saved to a text file (`missing_in_target.txt`).

---

## Example

Assume your **source directory** contains the following files:

```
source/
├── folder1/
│   └── file1.txt
├── folder2/
│   └── file2.txt
├── folder3/
│   ├── file3.txt
│   └── file4.txt
└── folder4/
    └── file5.txt
```

Your **target CSV file** (`target_files.csv`) looks like:

```
File Name,File Path,Last Update
file1.txt,folder1/file1.txt,2025-01-01 10:00:00
file2.txt,folder2/file2.txt,2025-01-02 11:00:00
```

The script will identify the missing files (`file3.txt`, `file4.txt`, `file5.txt`) and output the following:

```
Total files in source but not in target: 3
Missing files list saved to missing_in_target.txt

Summary of Missing Files:
+------------+----------------------------+
| File Name  | File Path                  |
+------------+----------------------------+
| file3.txt  | folder3/file3.txt          |
| file4.txt  | folder3/file4.txt          |
| file5.txt  | folder4/file5.txt          |
+------------+----------------------------+
```

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---
