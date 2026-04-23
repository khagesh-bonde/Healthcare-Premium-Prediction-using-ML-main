import streamlit as st
from prediction_helper import predict

# Define the page layout
st.title('Health Insurance Cost Predictor')

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Button to make prediction
if st.button('Predict'):

    prediction = predict(input_dict)

    # Handle both array and single value
    if isinstance(prediction, (list, tuple)):
        amount = prediction[0]
    else:
        amount = prediction

    st.markdown(
        f"""
        <div class="prediction-box">
            Annual Health Insurance Cost is 
            <span class="prediction-amount"> Rs. {round(float(amount), 2)} </span>
        </div>
        """,
        unsafe_allow_html=True
    )




st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #1f4037, #99f2c8);
    background-attachment: fixed;
}

/* Title */
h1 {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    color: #ffffff !important;
}

/* Form Glass Effect */
div[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.15);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
}

/* Labels */
label {
    font-weight: 600 !important;
    color: white !important;
}

/* Predict Button */
div.stButton > button {
    background: linear-gradient(90deg, #ff9966, #ff5e62);
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 0.6rem 2rem;
    border: none;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

/* Prediction Highlight Box */
.prediction-box {
    margin-top: 1px;
    padding: 15px;
    border-radius: 15px;
    background: linear-gradient(90deg, #36d1dc, #5b86e5);
    text-align: center;
    color: white;
    font-size: 1.5rem;
    font-weight: 600;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}

.prediction-amount {
    font-size: 1.8rem;
    font-weight: 800;
    margin-left: 8px;
}


</style>
""", unsafe_allow_html=True)

