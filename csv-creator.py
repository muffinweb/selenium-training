import csv
import openpyxl

# Create a new Excel workbook
workbook = openpyxl.Workbook()
# Select the default sheet (usually named 'Sheet')
sheet = workbook.active
# Add data to the Excel sheet
data = [
    ["Name", "Age", "City"]
]

another_data = [
    ["Uğur", 28, "New York"],
    ["Angélique", 24, "San Francisco"],
    ["Özğür", 32, "Los Angeles"],
    ["Mbappe", 25, "Madrid"]
]

data += another_data

for row in data:
    sheet.append(row)
# Save the workbook to a file
workbook.save("my_excel_file.xlsx")
# Print a success message
print("Excel file created successfully!")
