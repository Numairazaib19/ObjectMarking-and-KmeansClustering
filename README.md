# Object Marking & K-means Clustering for Multi-Detection for cyclist data

## Overview
This project involves processing a dataset of cyclist-related images. It covers the steps of image format conversion, object marking (bounding boxes around cycle and person), clustering, and storing the results for further analysis. The aim is to analyze the distribution of objects using KMeans clustering and generate a structured dataset for future insights.

## Steps Involved

### 1. Image Collection and Conversion
- **Image Collection**: All images (JPG, JPEG, PNG) are gathered in a folder called `Cyclist_dataset`.
- **Image Format Conversion**: Images are converted to the BMP format for easier processing. The converted images are saved in the `Cyclist_dataset_bmp` folder.

### 2. Object Marking and Information Collection
- **Object Marking**: Two objects (cycle and person) are marked in each image by defining bounding boxes.
- **Data Collection**: Coordinates (x, y), width, and height of the bounding boxes are recorded for each image.

### 3. Clustering Analysis
- **Clustering**: KMeans clustering is applied to the bounding box data to group objects based on their coordinates and sizes.
- **Visualization**: The clustering results are visualized using a scatter plot showing the distribution of objects in 2D space.

### 4. Data Storage
- **CSV File**: A CSV file (`bounding_boxes_file.csv`) is created to store the data, including image paths, bounding box coordinates, sizes, and cluster labels.
- **Annotated Images**: Processed images with bounding boxes are saved in the `output_images` directory.

## Conclusion
This project successfully demonstrates how to process images, mark objects, apply clustering, and store the results for future analysis.
