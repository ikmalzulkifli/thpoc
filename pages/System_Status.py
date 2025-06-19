# pages/3_System_Status.py
import streamlit as st
import pandas as pd
import time

# --- Page Configuration ---
st.set_page_config(page_title="System Status & Implementation", layout="wide", page_icon="⚙️")


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

st.title("⚙️ System Status & Implementation")

# --- Statistical Significance & Real-time Data ---
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.subheader("Statistical Significance Tests")
        st.info("Key Insight: Peak registration age is 50-55 years, representing 23.4% of all depositors. ")
        df_stats = pd.DataFrame({
            "Test": ["Kolmogorov-Smirnov", "Mann-Whitney U", "Chi-Square"],
            "Description": ["Normal Distribution", "Significant Difference", "Regional Independence"],
            "p-value": ["0.032", "0.001", "0.156"],
            "Result": ["Significant", "Significant", "Not Significant"]
        })
        st.dataframe(df_stats, hide_index=True, use_container_width=True)
        st.caption("Statistical Summary: Analysis reveals significant age-based patterns and regional variations in registration behavior (α=0.05). ")

with col2:
    with st.container(border=True):
        st.subheader("Real-time Data Integration")
        st.caption(f"Last updated: {time.strftime('%H:%M:%S')}")

        # System Health Monitor
        st.markdown("""
            | System             | Status    | Data Quality | Latency |
            |--------------------|-----------|--------------|---------|
            | **Registration DB** | 🟢 Healthy | 98%          | 23ms    |
            | **Demographics API**| 🟠 Warning  | 94%          | 156ms   |
            | **Quota System** | 🟢 Healthy | 99%          | 12ms    |
            | **Appeals DB** | 🔴 Error   | 87%          | timeout |
        """, unsafe_allow_html=True)

        # Real-time Stats
        stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
        stat_col1.metric("Active Sessions", "1,247", "+23")
        stat_col2.metric("Processing Queue", "156", "-12")
        stat_col3.metric("Data Refresh Rate", "30s", "Normal")
        stat_col4.metric("Memory Usage", "67%", "+2%")

st.divider()

# --- Implementation & Success ---
st.header("Success Metrics")
col4 = st.columns(1)[0]  # Single column for success metrics
# with col3:
#     with st.container(border=True):
#         st.subheader("Implementation Timeline")
#         st.markdown("**Phase 1: Data Integration (3 Months)**")
#         st.progress(85, text="85% Complete")
#         st.markdown("**Phase 2: Model Development (6 Months)**")
#         st.progress(60, text="60% Complete")
#         st.markdown("**Phase 3: Dashboard Launch (9 Months)**")
#         st.progress(25, text="25% Complete")
#         st.markdown("**Phase 4: Policy Integration (12 Months)**")
#         st.progress(0, text="0% Complete")

with col4:
    with st.container(border=True):
        st.subheader("Success Measurements")
        st.markdown("**Forecast Accuracy** (Target: >90%)")
        st.progress(92, text="✅ 92% Achieved")
        st.markdown("**Decision Time Reduction** (Target: 50%)")
        st.progress(47, text="⏳ 47% In Progress")
        st.markdown("**Policy Effectiveness** (Target: +25%)")
        st.progress(92, text="⏳ +23% In Progress") # 23/25 = 92%
        st.markdown("**Resource Optimization** (Target: 30%)")
        st.progress(93, text="⏳ 28% In Progress") # 28/30 = 93.3%