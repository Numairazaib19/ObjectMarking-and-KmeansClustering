import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data = {
    'x': [199, 308, 130, 213, 211, 107, 156, 122, 252, 167, 291, 144, 86, 67, 20, 61, 194, 43, 59, 160, 183, 127],
    'y': [18, 97, 28, 6, 146, 182, 186, 113, 80, 51, 14, 62, 114, 167, 150, 198, 240, 165, 180, 14, 4, 22],
    'width': [172, 154, 98, 129, 165, 336, 303, 151, 74, 113, 105, 83, 271, 395, 312, 434, 363, 285, 410, 77, 118, 86],
    'height': [368, 287, 264, 342, 104, 254, 244, 106, 147, 315, 338, 146, 138, 217, 151, 238, 206, 143, 198, 223, 324, 264]
}

df = pd.DataFrame(data)

# Step 2: Preprocess the data (scaling)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Step 3: Apply KMeans clustering
kmeans = KMeans(n_clusters=2, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_data)

# Step 4: Visualize the clusters (optional)
plt.scatter(df['x'], df['y'], c=df['cluster'], cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
plt.title('KMeans Clustering of Cycle and Person Data')
plt.show()

# Print the data with clusters
print(df)
