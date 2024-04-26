import os
import openpyxl

# Function to check if a file name contains any of the specified keywords
def contains_keywords(filename, keywords):
    for keyword in keywords:
        if keyword.lower() in filename.lower():
            return True
    return False

# Directory containing Excel files
directory = '/path/to/your/directory'

# Keywords to search for in file names
keywords = ["cam", "san diego", "uk"]

# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx') and contains_keywords(filename, keywords):
        # Load the Excel file
        wb = openpyxl.load_workbook(os.path.join(directory, filename))
        
        # Prompt user to select a sheet
        sheet_name = input(f"Select a sheet from {filename}: ")
        
        # Check if the selected sheet exists
        if sheet_name in wb.sheetnames:
            # Create a new workbook for the merged data
            merged_wb = openpyxl.Workbook()
            merged_ws = merged_wb.active
            
            # Copy data from selected sheet to merged workbook
            selected_ws = wb[sheet_name]
            for row in selected_ws.iter_rows():
                merged_ws.append([cell.value for cell in row])
            
            # Name the new sheet after the first 10 characters of the original file name
            new_sheet_name = filename[:10]
            merged_ws.title = new_sheet_name
            
            # Save the merged data to a new file
            merged_filename = "merged_data.xlsx"
            merged_wb.save(merged_filename)
            
            print(f"Sheet '{sheet_name}' from '{filename}' copied to '{merged_filename}' as '{new_sheet_name}'")

# Save the merged data file
merged_wb.save(merged_filename)
print("Merged data saved.")
