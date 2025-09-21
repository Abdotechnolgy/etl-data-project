import pandas as pd
import matplotlib.pyplot as plt

try:
    # Load Nora's data
    df = pd.read_csv('nora_data_transformed.csv')

    # Count the number of images for each project
    image_counts = df['project_name'].value_counts()

    # Create the plot
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots()
    
    image_counts.plot(kind='bar', ax=ax, color='#5E8ACF')
    
    ax.set_title('Number of Images Per Project', fontsize=14)
    ax.set_ylabel('Total Images', fontsize=10)
    plt.xticks(rotation=0) # Make the project name horizontal
    
    # Add the number label above the bar
    for index, value in enumerate(image_counts):
        ax.text(index, value + 0.5, str(value), ha='center', va='bottom')

    plt.tight_layout()

    # Save the plot as an image
    output_filename = 'nora_project_plot.png'
    plt.savefig(output_filename, dpi=200)
    
    print(f"Plot saved successfully as '{output_filename}'")

except Exception as e:
    print(f"An error occurred: {e}")