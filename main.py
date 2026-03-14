import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Loan Default Predictor", page_icon="💳")

st.title("💳 Loan Default Prediction")
st.write("Enter applicant and loan details to estimate default probability and credit risk score.")

st.markdown("---")

# ---------------- Row 1 ----------------
st.markdown('<p class="subheader">Applicant Details</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)

with col2:
    income = st.number_input("Income", min_value=0, step=1000, value=40000)

with col3:
    loan_amount = st.number_input("Loan Amount", min_value=0, step=1000, value=100000)


# ---------------- Row 2 ----------------
st.markdown('<p class="subheader">Financial Profile</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

loan_to_income_ratio = loan_amount / income if income > 0 else 0

with col1:
    st.text("Loan to Income Ratio")
    st.text(f"{loan_to_income_ratio:.2f}")

with col2:
    total_Loan_months = st.number_input(
        "Loan Tenure Months (Credit History)",
        min_value=0,
        step=1,
        value=20
    )

with col3:
    avg_Dpd = st.number_input(
        "Avg DPD",
        min_value=0,
        max_value=100,
        step=1,
        value=35
    )


# ---------------- Row 3 ----------------
st.markdown('<p class="subheader">Credit Behaviour</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    delinquent_ratio = st.number_input(
        "Delinquent Ratio (%)",
        min_value=0,
        max_value=100,
        step=1,
        value=30
    )

with col2:
    credit_util_ratio = st.number_input(
        "Credit Utilization Ratio (%)",
        min_value=0,
        max_value=100,
        step=1,
        value=35
    )

with col3:
    open_accounts = st.number_input(
        "Number of Open Loan Accounts",
        min_value=0,
        step=1
    )


# ---------------- Row 4 ----------------
st.markdown('<p class="subheader">Loan Information</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    residence_type = st.selectbox(
        "Residence Type",
        ['Mortgage', 'Owned', 'Rented']
    )

with col2:
    loan_purpose = st.selectbox(
        "Loan Purpose",
        ['Home', 'Personal', 'Auto', 'Education']
    )

with col3:
    loan_type = st.selectbox(
        "Loan Type",
        ['Secured', 'Unsecured']
    )


st.markdown("---")

# ---------------- Prediction ----------------
if st.button("Predict Risk"):

    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_to_income_ratio,
        total_Loan_months, avg_Dpd,
        delinquent_ratio, credit_util_ratio,
        open_accounts, residence_type,
        loan_purpose, loan_type
    )

    st.markdown('<p class="subheader">Prediction Results</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Default Probability", f"{probability:.2%}")

    with col2:
        st.metric("Credit Score", credit_score)

    with col3:
        st.metric("Rating", rating)