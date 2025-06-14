import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
model = pickle.load(open(r'C:\Users\samua\linear_regression_model.pk1', 'rb'))

# Set the title of the app
st.title("Salary Prediction App")

# Add a brief description
st.write("This app predicts the salary based on years of experience using a simple linear regression model.")

# Add input widget for user to enter years of experience
years_of_experience = st.number_input("Enter Years of Experience:", min_value=0.0, max_value=50.0, value=1.0, step=0.5)

# when the button is clicked predictions

if st.button("Predict Salary"):
    # make a prediction using the trained model
    experience_input = np.array([[years_of_experience]])
    prediction = model.predict(experience_input)
    
    # Display the prediction
    st.success(f"The predicted salary for {years_of_experience} years of experience is: ${prediction[0]:,.2f}")
    
# Display information about the model
st.write("The model was trained using a dataset of salaries and yours of experience.built model by using linear regression.")

