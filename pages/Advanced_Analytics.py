# pages/2_Advanced_Analytics.py
import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(page_title="Advanced Analytics", layout="wide", page_icon="🔬")

# --- Custom CSS for Tabung Haji Theme ---
def apply_custom_theme():
    """Applies a custom CSS theme to the Streamlit app."""
    custom_css = """
    <style>
        /* Main colors */
        :root {
            --primary-color: #014034; /* Dark Green from TH */
            --secondary-color: #04d61d; /* Lighter Green for buttons */
            --background-color: #F0F2F6; /* Light gray background */
            --text-color: #262730;
            --secondary-text-color: #FFFFFF;
        }

        /* General app styling */
        .stApp {
            background-color: var(--background-color);
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: var(--secondary-color);
        }
        
        /* CORRECTED: This targets all text and links within the sidebar nav items */
        [data-testid="stSidebar"] .st-emotion-cache-16txtl3 a,
        [data-testid="stSidebar"] .st-emotion-cache-16txtl3 {
            color: var(--secondary-text-color);
        }


        /* Button styling */
        .stButton>button {
            color: var(--secondary-text-color);
            background-color: var(--secondary-color);
            border: none;
            border-radius: 4px;
        }
        .stButton>button:hover {
            background-color: #27AE60; /* Slightly lighter green on hover */
            color: var(--secondary-text-color);
        }

        /* Metric styling */
        [data-testid="stMetric"] {
            background-color: #FFFFFF;
            border-radius: 8px;
            padding: 15px;
            border: 1px solid #E0E0E0;
        }

        /* Alert boxes */
        [data-testid="stAlert"] {
            border-radius: 8px;
        }

        /* Progress bar styling */
        [data-testid="stProgressBar"] > div > div > div > div {
            background-color: var(--secondary-color);
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

apply_custom_theme()

# --- Sidebar ---
with st.sidebar:
    # --- Add Tabung Haji Logo ---
    # Make sure you have a 'logo.png' file in the main app directory
    try:
        st.image("logo.png", use_container_width=True)
    except Exception as e:
        st.write("Place your logo.png file in the main app directory")

st.title("🔬 Advanced Analytics & ML Models")

# --- Age Distribution & ML Performance ---
with st.container(border=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Age Distribution Analysis")
        # Data for Age Distribution Area Chart
        age_data = {
            'Age Group': ['40-45', '45-50', '50-55', '55-60', '60-65', '65-70'],
            'Depositors (in thousands)': [320, 700, 920, 750, 600, 450]
        }
        df_age = pd.DataFrame(age_data)
        fig_age = px.area(df_age, x='Age Group', y='Depositors (in thousands)',
                          labels={'Depositors (in thousands)': 'Number of Depositors (K)'},
                          color_discrete_sequence=['#1D8348'])
        fig_age.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_age, use_container_width=True)

    with col2:
        st.subheader("ML Model Performance")
        ml_data = {
            "Model": ["Neural Network", "ARIMA Forecast", "Random Forest"],
            "Accuracy": ["94% Accurate", "92% Accurate", "89% Accurate"],
            "R² Score": [0.91, 0.87, 0.84],
            "MAE": [2.8, 3.2, 4.1]
        }
        df_ml = pd.DataFrame(ml_data)
        st.dataframe(df_ml, hide_index=True, use_container_width=True)

        st.subheader("Correlation Analysis")
        st.markdown("""
        - **Age**: Strong (0.89)
        - **Geography**: Moderate (0.72)
        - **Health Status**: Moderate (0.68)
        - **Income**: Weak (0.45)
        """)

st.divider()

# --- Interactive Data Exploration ---
st.header("Interactive Data Exploration")
df_interactive = pd.DataFrame([
    {"ID": "HAJ-2024-001", "Region": "Central", "Age": 65, "Wait Years": 12, "Status": "Active", "Priority": "High"},
    {"ID": "HAJ-2024-002", "Region": "Eastern", "Age": 45, "Wait Years": 25, "Status": "Active", "Priority": "Standard"},
    {"ID": "HAJ-2024-003", "Region": "Western", "Age": 72, "Wait Years": 8, "Status": "Priority", "Priority": "Critical"},
    {"ID": "HAJ-2024-004", "Region": "Northern", "Age": 58, "Wait Years": 18, "Status": "Active", "Priority": "Standard"},
    {"ID": "HAJ-2024-005", "Region": "Southern", "Age": 78, "Wait Years": 5, "Status": "Priority", "Priority": "Critical"},
])

with st.container(border=True):
    filter_col1, filter_col2, filter_col3 = st.columns([1,1,2])
    with filter_col1:
        region = st.selectbox("Filter by Region", ["All Regions"] + df_interactive['Region'].unique().tolist())
    with filter_col2:
        age_group = st.selectbox("Filter by Age Group", ["All Ages", "40-60", "60-70", "70+"])

    if region != "All Regions":
        df_interactive = df_interactive[df_interactive['Region'] == region]

    st.dataframe(df_interactive, hide_index=True, use_container_width=True)
    st.caption("Showing 5 of 5 records")

st.divider()

# --- Statistical Deep Dive ---
st.header("Statistical Deep Dive")
with st.container(border=True):
    st.subheader("Outlier Detection")
    outlier_col1, outlier_col2, outlier_col3 = st.columns(3)
    outlier_col1.metric("Wait Time Outliers", "127 cases", "Depositors with 200+ year projections")
    outlier_col2.metric("Age Anomalies", "43 cases", "Registrations under legal age")
    outlier_col3.metric("Geographic Clusters", "12 regions", "Areas with unusual concentration")