import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    # Correctly specify the file path
    data_path = r'C:\Users\wilda\OneDrive\WILDAN FADHIL NAZARUDDIN\PROJECK\latihan data scientis\submission\notebook.ipynb'
    data = pd.read_csv(data_path)
    return data

# Data processing functions
def process_data(data):
    # Add your data processing code here
    return data

# Visualization functions
def plot_pm25(data):
    fig, ax = plt.subplots()
    ax.plot(data['date_time'], data['PM2.5'], marker='o', linewidth=2, color="#39064B")
    ax.set_ylabel("PM2.5")
    ax.set_title("PM2.5 Trend")
    st.pyplot(fig)

def plot_pm10(data):
    fig, ax = plt.subplots()
    ax.plot(data['date_time'], data['PM10'], marker='o', linewidth=2, color="#39064B")
    ax.set_ylabel("PM10")
    ax.set_title("PM10 Trend")
    st.pyplot(fig)

# Main function
def main():
    st.title("Air Quality Analysis in Dingling")
    st.sidebar.title("Options")
    
    # Load and process data
    data = load_data()
    processed_data = process_data(data)
    
    # Sidebar options
    option = st.sidebar.selectbox("Choose a visualization", ("PM2.5 Trend", "PM10 Trend"))
    
    # Plot based on the selected option
    if option == "PM2.5 Trend":
        plot_pm25(processed_data)
    elif option == "PM10 Trend":
        plot_pm10(processed_data)

if __name__ == "__main__":
    main()
