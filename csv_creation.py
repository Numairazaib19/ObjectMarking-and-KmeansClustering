import pandas as pd

# Create a dictionary with your bounding box data
data = {
    'image_path': ['6.bmp', '7.bmp', '8.bmp', '9.bmp', '1.bmp', '10.bmp', '11.bmp', '2.bmp', '1.bmp', '10.bmp', '11.bmp', '2.bmp', '3.bmp', '4.bmp', '5.bmp', '6.bmp', '7.bmp', '8.bmp', '9.bmp', '3.bmp', '4.bmp', '5.bmp'],
    'x': [199, 308, 130, 213, 211, 107, 156, 122, 252, 167, 291, 144, 86, 67, 20, 61, 194, 43, 59, 160, 183, 127],
    'y': [18, 97, 28, 6, 146, 182, 186, 113, 80, 51, 14, 62, 114, 167, 150, 198, 240, 165, 180, 14, 4, 22],
    'width': [172, 154, 98, 129, 165, 336, 303, 151, 74, 113, 105, 83, 271, 395, 312, 434, 363, 285, 410, 77, 118, 86],
    'height': [368, 287, 264, 342, 104, 254, 244, 106, 147, 315, 338, 146, 138, 217, 151, 238, 206, 143, 198, 223, 324, 264],
    'cluster': [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = 'bounding_boxes_file.csv'  # Specify your CSV file path
df.to_csv(csv_file_path, index=False)

print(f'CSV file created at {csv_file_path}')
