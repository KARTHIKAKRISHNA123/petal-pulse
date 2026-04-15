import streamlit as st
import pandas as pd
import joblib

# Set the page configuration
st.set_page_config(page_title="Iris Predictor", page_icon="🌺", layout="centered")

# --- CUSTOM CSS FOR DARK FLORAL THEME ---
st.markdown("""
<style>
/* Moody dark background with a subtle dark pink radial glow */
.stApp {
    background-color: #0a0a0a;
    background-image: radial-gradient(circle at 50% 0%, #2e0014 0%, #0a0a0a 70%);
}

/* Force all standard text to be a readable light pink/white */
h1, h2, h3, p, label, .stMarkdown {
    color: #ffe6f2 !important;
}

/* Pulsing animation for the main title flowers */
@keyframes pulse {
    0% { transform: scale(1); text-shadow: 0 0 10px #ff66b2; }
    50% { transform: scale(1.2); text-shadow: 0 0 20px #ffb3d9; }
    100% { transform: scale(1); text-shadow: 0 0 10px #ff66b2; }
}

.floral-title {
    font-size: 2.8rem;
    font-weight: bold;
    color: #ff66b2;
    text-align: center;
    margin-bottom: 10px;
    font-family: 'Georgia', serif;
    text-shadow: 2px 2px 4px #000000;
}

.animated-flower {
    display: inline-block;
    animation: pulse 2.5s infinite ease-in-out;
}

/* Style the predict button with a neon pink glow */
div.stButton > button:first-child {
    background-color: #ff3399;
    color: white !important;
    border-radius: 30px;
    border: 1px solid #ffb3d9;
    padding: 10px 30px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.3s ease;
    display: block;
    margin: 0 auto;
    box-shadow: 0 4px 15px rgba(255, 51, 153, 0.4);
}

div.stButton > button:first-child:hover {
    background-color: #e60073;
    box-shadow: 0 6px 20px rgba(255, 51, 153, 0.8);
    transform: translateY(-2px);
}

/* Custom Result Box to GUARANTEE visibility against the black background */
.result-box {
    background-color: rgba(20, 0, 10, 0.8);
    border: 2px solid #ff66b2;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 0 20px rgba(255, 102, 178, 0.3);
    margin-top: 20px;
}

.result-text {
    color: #ffb3d9;
    font-size: 1.2rem;
}

.species-highlight {
    color: #ffffff;
    font-size: 2.2rem;
    font-weight: bold;
    text-shadow: 0 0 15px #ff66b2;
    display: block;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)


# 1. Load the exported models
@st.cache_resource
def load_models():
    knn = joblib.load('knn_model.pkl')
    log = joblib.load('log_model.pkl')
    nb = joblib.load('nb_model.pkl')
    return knn, log, nb

knn_model, log_model, nb_model = load_models()

# 2. Build the App UI with Custom HTML
st.markdown('<p class="floral-title"><span class="animated-flower">🌺</span> Iris Species Predictor <span class="animated-flower">🌸</span></p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ffb3d9; font-size: 1.1rem; margin-bottom: 2rem;'>Adjust the sliders, choose a model, and let the magic happen!</p>", unsafe_allow_html=True)


# 3. Create the Sidebar for User Inputs
st.sidebar.markdown("<h2 style='color: #ff66b2;'>🌿 Input Features</h2>", unsafe_allow_html=True)
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.8)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 4.3)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 1.3)

st.sidebar.markdown("---")

# 4. Create Model Selection Dropdown
st.sidebar.markdown("<h2 style='color: #ff66b2;'>⚙️ Choose Model</h2>", unsafe_allow_html=True)
model_choice = st.sidebar.selectbox(
    "Select the machine learning algorithm:",
    ("K-Nearest Neighbours", "Logistic Regression", "Naive Bayes")
)

# 5. Format the inputs into a pandas DataFrame
input_data = pd.DataFrame({
    'SepalLengthCm': [sepal_length],
    'SepalWidthCm': [sepal_width],
    'PetalLengthCm': [petal_length],
    'PetalWidthCm': [petal_width]
})

st.subheader("Your Input Measurements:")
st.dataframe(input_data, use_container_width=True)

st.write("") 

# 6. Make Predictions when the user clicks the button
if st.button("Predict Species 🌿"):
    # Pick the correct model based on the dropdown choice
    if model_choice == "K-Nearest Neighbours":
        model = knn_model
    elif model_choice == "Logistic Regression":
        model = log_model
    else:
        model = nb_model
    
    # Generate the prediction
    prediction = model.predict(input_data)
    
    # Display the result using our custom high-visibility dark theme box
    st.markdown("---")
    st.markdown(f"""
        <div class="result-box">
            <span class="result-text">Based on <b>{model_choice}</b>, the predicted species is:</span>
            <span class="species-highlight">🌸 {prediction[0]} 🌸</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons()