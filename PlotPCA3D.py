import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Replace 'your_data_file.txt' with the actual filename
data_file = 'PCOinput.txt'

# Read the data into a pandas DataFrame
df = pd.read_csv(data_file, sep='\t')

# Extract PCA columns
pca_columns = df.columns[2:5]  # Use the first three PCA components for 3D plot

# Define a color dictionary for each group
group_colors = {'CompositeCore': 'red', 'MiniCore': 'blue'}  # Add more groups as needed

# Create a 3D scatter plot with color-coded points based on groups
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each group separately
for group, color in group_colors.items():
    group_data = df[df['Group'] == group]
    ax.scatter(group_data[pca_columns[0]], group_data[pca_columns[1]], group_data[pca_columns[2]], label=group, color=color, s=80)

# Add labels and title
ax.set_xlabel(f'PCA1')
ax.set_ylabel(f'PCA2')
ax.set_zlabel(f'PCA3')
ax.set_title('3D PCA Plot with Group Colors')

# Add legend
ax.legend(title='Group', bbox_to_anchor=(1.05, 1), loc='upper center')

# Save the plot as a high-resolution image (adjust the filename and dpi as needed)
plt.savefig('testIndels_PCA_3d_plot.png', dpi=300)

# Adjust layout to avoid overlapping titles
plt.tight_layout()

# Show the plot
plt.show()

