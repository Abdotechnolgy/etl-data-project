import streamlit as st
import pandas as pd

# ----- Page Configuration -----
st.set_page_config(page_title="ArchDaily Dashboard", layout="wide")

# ----- Dashboard Title -----
st.title("🖼️ ArchDaily Project Dashboard")

# ----- Load Data -----
try:
    # Load the data from the CSV file
    df = pd.read_csv('nora_data_transformed.csv')

    # ----- KPIs -----
    st.header("Project Summary")
    # Create two columns for the metrics
    col1, col2 = st.columns(2)
    col1.metric("Project Name", df['project_name'].iloc[0])
    col2.metric("Total Images", df.shape[0])

    st.markdown("---") # Separator

    # ----- Full Image Gallery -----
    st.header("Full Image Gallery")
    
    # Define the number of columns for the image grid (e.g., 3)
    num_columns = 3
    cols = st.columns(num_columns)
    
    # Distribute images across the columns
    for index, row in df.iterrows():
        col_index = index % num_columns
        with cols[col_index]:
            st.image(row['image_url'], caption=row['caption'], use_column_width=True)

except FileNotFoundError:
    st.error("Error: 'nora_data_transformed.csv' file not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")