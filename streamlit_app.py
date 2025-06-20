import streamlit as st
import requests

st.set_page_config(page_title="AI Medical Diagnosis", layout="centered")

st.title("🩺 AI-Powered Medical Diagnosis")
st.markdown("Upload an **X-ray/MRI image** and enter a **medical report** to predict possible diseases.")

# Upload image
image_file = st.file_uploader("Upload X-ray/MRI Image", type=["jpg", "jpeg", "png"])

# Medical report text
report_text = st.text_area("Enter Medical Report")

if st.button("Predict Diagnosis"):
    if image_file and report_text:
        files = {"image": image_file.getvalue()}
        data = {"report": report_text}
        with st.spinner("Analyzing..."):
            try:
                res = requests.post("http://localhost:8000/predict/", files={"image": image_file}, data={"report": report_text})
                res.raise_for_status()  # Raise an error for 4xx/5xx
                prediction = res.json()['prediction']
                st.success(f"🧬 Prediction: **{prediction}**")
            except requests.exceptions.RequestException as req_err:
                st.error("Prediction failed due to a network or server error.")
                st.exception(req_err)
            except Exception as e:
                st.error("An unexpected error occurred.")
                st.exception(e)

    else:
        st.warning("Please upload an image and enter a report.")

