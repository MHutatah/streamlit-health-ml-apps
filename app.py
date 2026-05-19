import streamlit as st
import pickle
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    with open("iris_model.pkl", "rb") as f:
        return pickle.load(f)

# Page configuration
st.set_page_config(page_title="Health & ML Apps", layout="centered")

# Sidebar navigation
page = st.sidebar.selectbox("Select an App", ["BMI Calculator", "Iris Classifier"])

if page == "BMI Calculator":
    st.title("BMI Calculator 🏋️")
    st.write("Enter your height and weight to calculate your Body Mass Index (BMI).")

    # Input fields
    height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.5)
    weight_kg = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, value=70.0, step=0.5)

    # Calculate BMI on button click
    if st.button("Calculate BMI"):
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        st.subheader(f"Your BMI: {bmi:.1f}")

        # Display category message
        if bmi < 18.5:
            st.warning("⚠️ Underweight — Consider consulting a healthcare provider.")
        elif 18.5 <= bmi < 25:
            st.success("✅ Normal weight — Great job maintaining a healthy BMI!")
        elif 25 <= bmi < 30:
            st.warning("⚠️ Overweight — A balanced diet and regular exercise may help.")
        else:
            st.error("🚨 Obese — Please consider speaking with a healthcare professional.")

elif page == "Iris Classifier":
    model = load_model()
    species_names = ["Setosa 🌸", "Versicolor 🌺", "Virginica 🌼"]

    st.title("Iris Flower Classifier 🌷")
    st.write("Adjust the sliders below and click **Predict Species** to classify the Iris flower.")

    st.subheader("Input Features (cm)")

    sepal_length = st.slider("Sepal Length (cm)", min_value=4.0, max_value=8.0, value=5.8, step=0.1)
    sepal_width = st.slider("Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.0, step=0.1)
    petal_length = st.slider("Petal Length (cm)", min_value=1.0, max_value=7.0, value=4.0, step=0.1)
    petal_width = st.slider("Petal Width (cm)", min_value=0.1, max_value=2.5, value=1.2, step=0.1)

    # Predict on button click
    if st.button("Predict Species"):
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]

        st.subheader(f"Predicted Species: {species_names[prediction]}")

        st.write("**Prediction Probabilities:**")
        for name, prob in zip(species_names, probability):
            st.progress(float(prob), text=f"{name}: {prob:.1%}")
