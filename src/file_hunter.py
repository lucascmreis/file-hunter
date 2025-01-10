import os
import pandas as pd
from tqdm import tqdm  # For progress bar
from tabulate import tabulate  # For summary table

def get_files_from_directory(source_dir):
    """Retrieve all file paths from a source directory."""
    file_paths = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            # Normalize file paths relative to the source directory
            relative_path = os.path.relpath(os.path.join(root, file), start=source_dir)
            file_paths.append(os.path.normpath(relative_path))
    return file_paths

def compare_files_inverted(source_files, target_files):
    """Find files in the source that are not in the target."""
    # Normalize target file paths for cross-platform compatibility
    target_files = [os.path.normpath(file) for file in target_files]

    # Find files that exist in source but not in target
    missing_in_target = [file for file in source_files if file not in target_files]
    return missing_in_target

def display_summary(missing_files):
    """Display a summary table of missing files."""
    summary_data = [{"File Name": os.path.basename(file), "File Path": file} for file in missing_files]
    print("\nSummary of Missing Files:")
    print(tabulate(summary_data, headers="keys", tablefmt="grid"))

def main():
    print("=== Files Missing in Target Checker ===\n")
    
    # Input paths
    source_dir = input("Enter the path to the source directory: ").strip()
    target_csv = input("Enter the path to the target CSV file: ").strip()
    target_column = input("Enter the column name in the CSV containing file paths: ").strip()
    
    # Validate inputs
    if not os.path.isdir(source_dir):
        print("Invalid source directory path.")
        return
    if not os.path.isfile(target_csv):
        print("Invalid target CSV file path.")
        return
    
    # Load the target file list
    try:
        target_files = pd.read_csv(target_csv)[target_column].tolist()
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return
    
    # Get all files in the source directory
    print("\nScanning source directory...")
    source_files = get_files_from_directory(source_dir)
    print(f"Total files found in source: {len(source_files)}")
    
    # Compare files and find missing ones
    print("\nComparing files...")
    missing_files = []
    for _ in tqdm(range(1), desc="Checking files", unit="file"):
        missing_files = compare_files_inverted(source_files, target_files)
    
    # Output results
    print(f"\nTotal files in source but not in target: {len(missing_files)}")
    
    if missing_files:
        # Save missing files to a text file
        output_file = "missing_in_target.txt"
        with open(output_file, "w") as f:
            for file in missing_files:
                f.write(file + "\n")
        print(f"Missing files list saved to {output_file}")
        display_summary(missing_files)
    else:
        print("All files in source are present in target.")

if __name__ == "__main__":
    try:
        from tqdm import tqdm
        from tabulate import tabulate
        main()
    except ImportError as e:
        print(f"Missing required library: {e}. Install it using 'pip install tqdm tabulate'.")
