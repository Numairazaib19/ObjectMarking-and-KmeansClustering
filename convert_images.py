import os
from PIL import Image

# Define the folder containing images (jpg, jpeg, png, etc.) and the output folder for BMP images
input_folder = './Cyclist_dataset'
output_folder = './Cyclist_dataset_bmp'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize a counter for naming the output files sequentially
counter = 1

# List of valid image extensions to be converted
valid_extensions = ['.jpg', '.jpeg', '.png']

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    file_extension = os.path.splitext(filename)[1].lower()  # Get file extension and convert to lowercase
    if file_extension in valid_extensions:
        # Open the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Generate sequential file name like 1.bmp, 2.bmp, etc.
        bmp_filename = f"{counter}.bmp"
        bmp_path = os.path.join(output_folder, bmp_filename)
        
        # Save the image as BMP
        img.save(bmp_path, "BMP")
        
        # Increment the counter for the next file
        counter += 1

print("Conversion and renaming completed successfully!")
