import pandas as pd
import cv2
import os

# Step 1: Load the CSV file
csv_file = 'bounding_boxes_file.csv'
df = pd.read_csv(csv_file)

# Step 2: Define the folder where images are located
image_folder = 'Cyclist_dataset_bmp'


# Step 3: Process each image by grouping them
for image_path, group in df.groupby('image_path'):
    # Full image path
    full_image_path = os.path.join(image_folder, image_path)

    # Step 4: Load the image
    image = cv2.imread(full_image_path)

    if image is None:
        print(f"Error loading image: {full_image_path}")
        continue

    # Step 5: Draw bounding boxes on the image
    for index, row in group.iterrows():
        x, y, width, height, cluster = row['x'], row['y'], row['width'], row['height'], row['cluster']
        
        # Define the top-left and bottom-right points of the bounding box
        start_point = (x, y)
        end_point = (x + width, y + height)
        
        # Choose color based on cluster (you can adjust the colors as needed)
        color = (0, 255, 0) if cluster == 1 else (0, 0, 255)
        
        # Draw the rectangle (bounding box)
        cv2.rectangle(image, start_point, end_point, color, 2)
        
        # Optionally, add text for the cluster
        cv2.putText(image, f'Cluster {cluster}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Step 6: Save or display the processed image
    output_path = os.path.join('output_images', image_path)  # Save to an output folder
    os.makedirs('output_images', exist_ok=True)  # Create output folder if it doesn't exist
    cv2.imwrite(output_path, image)  # Save the image with bounding boxes
    print(f"Processed image saved at: {output_path}")

