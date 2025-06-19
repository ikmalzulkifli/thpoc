# pages/3_Classification_Engine.py
import streamlit as st
import pandas as pd
import time
import numpy as np

# --- Page Configuration ---
st.set_page_config(page_title="Classification Engine", layout="wide", page_icon="🤖")

# --- Custom CSS for Tabung Haji Theme (for consistency) ---
def apply_custom_theme():
    """Applies a custom CSS theme to the Streamlit app."""
    custom_css = """
    <style>
        /* Main colors */
        :root {
            --primary-color: #014034; /* Dark Green from TH */
            --secondary-color: #04d61d; /* Lighter Green */
            --background-color: #F0F2F6; /* Light gray background */
            --text-color: #FFFFFF; /* White text */
        }

        /* General app styling */
        .stApp {
            background-color: var(--background-color);
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: var(--secondary-color); /* Light green sidebar */
        }
        
        [data-testid="stSidebar"] .st-emotion-cache-16txtl3 a,
        [data-testid="stSidebar"] .st-emotion-cache-16txtl3 {
            color: var(--text-color); /* White text for contrast */
        }

        /* Button styling */
        .stButton>button {
            color: var(--text-color);
            background-color: var(--primary-color); /* Dark green for buttons */
            border: none;
            border-radius: 4px;
        }
        .stButton>button:hover {
            background-color: #02594A; /* Slightly lighter dark green on hover */
            color: var(--text-color);
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

apply_custom_theme()

# --- Sidebar ---
with st.sidebar:
    try:
        st.image("logo.png", use_container_width=True)
    except Exception as e:
        st.write("Place your logo.png file in the main app directory")

# --- Page Title ---
st.title("🤖 Hajj Offer Acceptance Predictor")
st.markdown("This engine predicts the likelihood of a candidate accepting their Hajj offer based on their profile.")
st.markdown("---")


# --- Mock Prediction Function ---
def predict_acceptance(features):
    """
    A mock prediction function that returns a prediction, confidence score,
    and a list of factors based on simple rules.
    """
    score = 50  # Start with a neutral score
    factors = []

    # Age-based logic
    if 40 <= features['age'] <= 60:
        score += 15
        factors.append("✅ **Positive Factor**: Candidate is within the prime age range for performing Hajj.")
    elif features['age'] > 70:
        score -= 10
        factors.append("⚠️ **Negative Factor**: Advanced age might pose health challenges.")

    # Salary-based logic
    if features['salary'] >= 5000:
        score += 20
        factors.append("✅ **Positive Factor**: Strong financial capacity indicated by salary.")
    elif features['salary'] < 3000:
        score -= 15
        factors.append("⚠️ **Negative Factor**: Lower salary might indicate financial constraints.")

    # Health Status logic
    if features['health'] == "Excellent" or features['health'] == "Good":
        score += 25
        factors.append("✅ **Positive Factor**: Good health status is crucial for Hajj.")
    else:
        score -= 25
        factors.append("⚠️ **Negative Factor**: Fair or Poor health is a significant barrier.")
        
    # Previous Deferments logic
    if features['deferments'] > 0:
        score -= (features['deferments'] * 10)
        factors.append(f"⚠️ **Negative Factor**: Candidate has deferred {features['deferments']} time(s) before.")
    else:
        score += 10
        factors.append("✅ **Positive Factor**: No previous deferments suggests strong intention.")

    # Number of Dependents logic
    if features['dependents'] > 3:
        score -= 10
        factors.append("⚠️ **Negative Factor**: High number of dependents may impact readiness.")

    # Clamp score between 0 and 100
    confidence = max(0, min(100, score))

    if confidence >= 50:
        prediction = "Likely to Accept"
    else:
        prediction = "Likely to Decline"
        
    return prediction, confidence, factors


# --- Input Form ---
st.header("Individual Candidate Prediction")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Age", 20, 90, 45)
        salary = st.number_input("Monthly Salary (MYR)", min_value=1000, max_value=30000, value=5000, step=500)
        dependents = st.number_input("Number of Dependents", min_value=0, max_value=15, value=2)

    with col2:
        health = st.selectbox("Health Status", ["Excellent", "Good", "Fair", "Poor"])
        occupation = st.selectbox("Occupation Sector", ["Government", "Private", "Self-Employed", "Retired", "Other"])
        deferments = st.number_input("Number of Previous Deferments", min_value=0, max_value=10, value=0)

    # Submit button
    submitted = st.form_submit_button("Predict Acceptance Likelihood")


# --- Display Prediction ---
if submitted:
    with st.spinner('Analyzing profile and running prediction...'):
        time.sleep(1) # Simulate processing time
        
        features = {
            'age': age,
            'salary': salary,
            'dependents': dependents,
            'health': health,
            'occupation': occupation,
            'deferments': deferments,
        }
        
        prediction, confidence, factors = predict_acceptance(features)

        st.subheader("Prediction Result")
        
        if prediction == "Likely to Accept":
            st.success(f"**Prediction: {prediction}**")
        else:
            st.error(f"**Prediction: {prediction}**")
            
        st.metric(label="Confidence Score", value=f"{confidence}%")
        st.progress(confidence)

        with st.expander("View Factors Influencing this Prediction"):
            for factor in factors:
                st.markdown(factor)

st.markdown("---")

# --- NEW: Batch Prediction Table ---
st.header("Batch Prediction on Sample Data")
st.markdown("This table demonstrates how the engine can be applied to multiple candidates at once.")

@st.cache_data
def generate_sample_data():
    """Generates a sample DataFrame and runs predictions on it."""
    data = {
        'accountID': np.random.randint(1000000, 9999999, size=200),
        'region': np.random.choice(["KUL", "SEL", "KED", "NSN", "MEL", "PEN", "JHR", "KTN", "TRG", "SBH", "SWK", "PHG", "PRK", "PLS", "PJY", "SGR"], size=200),
        'age': np.random.randint(30, 80, size=200),
        'salary': np.random.randint(2500, 15000, size=200),
        'dependents': np.random.randint(0, 5, size=200),
        'health': np.random.choice(["Excellent", "Good", "Fair", "Poor"], size=200, p=[0.4, 0.4, 0.1, 0.1]),
        'occupation': np.random.choice(["Government", "Private", "Self-Employed", "Retired"], size=200),
        'deferments': np.random.choice([0, 1, 2], size=200, p=[0.7, 0.2, 0.1])
    }
    sample_df = pd.DataFrame(data)

    predictions = []
    for _, row in sample_df.iterrows():
        # The predict_acceptance function returns a tuple (prediction, confidence, factors)
        # We only need the first item, which is the prediction text.
        prediction_result, _, _ = predict_acceptance(row)
        predictions.append(prediction_result)

    sample_df['Prediction'] = predictions
    return sample_df

# Generate and display the data
prediction_df = generate_sample_data()
st.dataframe(prediction_df, use_container_width=True)

if st.button("Generate New Sample"):
    st.cache_data.clear()
    st.rerun()