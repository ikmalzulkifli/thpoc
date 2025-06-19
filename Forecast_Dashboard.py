# 1_Strategic_Dashboard.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(
    page_title="Strategic Management Dashboard",
    layout="wide",
    page_icon="🕋"
)

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
    # Make sure you have a 'logo.png' file in the same directory
    try:
        st.image("logo.png", use_container_width=True)
    except Exception as e:
        st.write("Place your logo.png file in this directory")

# --- Title ---
st.title("Hajj Analytics System: Strategic Management Dashboard")

# --- Alerts ---
st.header("Key Alerts")
col1, col2, col3 = st.columns(3)
with col1:
    st.error("**A Critical Wait Time Alert**")
    st.write("Current projection exceeds 140 years - immediate action required.")
    st.metric(label="Current Projection", value="142 years", delta="+12% this year", delta_color="inverse")

with col2:
    st.warning("**High Risk Population Warning**")
    st.write("35% of depositors are age 70+ requiring priority consideration.")
    st.metric(label="Population Age 70+", value="1.33M people", delta="+3% increase")

with col3:
    st.info("**Appeals Trend Alert**")
    st.write("23% increase in appeals processing - system capacity review needed.")
    st.metric(label="Pending Appeals", value="85,000 appeals", delta="+23% increase")

st.divider()

# --- Summary Metrics ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Depositors", "3.8M", help="Current waitlist size")
col2.metric("Wait Time Projection", "142 Years", "Current trajectory")
col3.metric("Annual Quota", "31,600", "Fixed allocation")
col4.metric("High Risk Population (Age 70+)", "35%", "+3%")

st.divider()

# --- Charts ---
st.header("Visual Insights")
chart_col1, chart_col2 = st.columns([2, 1])

with chart_col1:
    st.subheader("Wait Time Projections (Years)")
    # Data for the line chart
    years = list(range(2024, 2036))
    current_trajectory = [142 + i*2.8 for i in range(12)]
    moderate = [140 - i*3.5 for i in range(12)]
    significant = [140 - i*6.1 for i in range(12)]
    optimal = [140 - i*8 for i in range(12)]
    df_projections = pd.DataFrame({
        'Year': years,
        'Current Trajectory': current_trajectory,
        'Moderate (+5K Quota)': moderate,
        'Significant (+10K Quota)': significant,
        'Optimal (+15K Quota)': optimal
    }).set_index('Year')

    st.line_chart(df_projections, height=400)

with chart_col2:
    st.subheader("Demographics Breakdown")
    # Data for the pie chart
    df_demographics = pd.DataFrame({
        'Age Group': ['Age 70+', 'Age 50-60', 'Age 40-50', 'Age 60-70'],
        'Percentage': [35, 28, 25, 12],
        'Population': ['1.33M', '1.06M', '950K', '456K']
    })
    fig_pie = px.pie(df_demographics, names='Age Group', values='Percentage',
                     hole=0.3, color_discrete_sequence=['#1D8348', '#27AE60', '#58D68D', '#A9DFBF'])
    fig_pie.update_traces(textinfo='percent', textfont_size=14)
    fig_pie.update_layout(showlegend=True, height=400, margin=dict(t=20, b=20, l=20, r=20), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_pie, use_container_width=True)

st.divider()

# --- Scenario Planning ---
st.header("Scenario Planning & Policy Recommendations")
st.info("Key Insight: Increasing the annual quota by 10,000 slots could reduce wait times from 150+ years to approximately 67 years by 2035.")
st.warning("Priority Alert: 35% of depositors are aged 70+, requiring urgent consideration for health and mobility factors.")

scenarios = st.columns(4)
scenarios_data = [
    {"title": "Current Trajectory", "status": "Critical", "quota": "31,600", "wait_time": "150+ years", "desc": "Waitlist continues to grow exponentially with current demographics."},
    {"title": "Moderate Improvement", "status": "Moderate", "quota": "36,600", "wait_time": "98 years", "desc": "Modest reduction but still challenging timeline."},
    {"title": "Significant Change", "status": "Improvement", "quota": "41,600", "wait_time": "67 years", "desc": "Substantial improvement in wait times."},
    {"title": "Optimal Solution", "status": "Optimal", "quota": "45,600", "wait_time": "45 years", "desc": "Best case scenario with manageable wait times."}
]

for i, scenario in enumerate(scenarios_data):
    with scenarios[i]:
        with st.container(border=True):
            st.subheader(scenario['title'])
            st.write(f"**Status:** {scenario['status']}")
            st.write(f"**Quota:** {scenario['quota']}")
            st.write(f"**Wait Time by 2035:** {scenario['wait_time']}")
            st.caption(scenario['desc'])

# --- Strategic Recommendations ---
st.subheader("→ Strategic Recommendations")
with st.container(border=True):
    rec_col1, rec_col2 = st.columns(2)
    with rec_col1:
        st.markdown("- **Quota Negotiation**: Advocate for +10K additional slots minimum.")
        st.markdown("- **Process Optimization**: Streamline appeals system (85K pending).")
    with rec_col2:
        st.markdown("- **Priority Systems**: Implement age-based allocation for 70+ depositors.")
        st.markdown("- **Resource Planning**: Coordinate flights, accommodation, medical services.")