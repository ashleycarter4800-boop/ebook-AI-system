import streamlit as st
import pandas as pd
from openai import OpenAI

st.set_page_config(page_title="Ultimate AI Studio", layout="wide")

st.title("🚀 Ultimate AI Studio")
st.subheader("Upload eBooks → Generate Content Automatically")

api_key = st.text_input("Enter OpenAI API Key", type="password")

uploaded_file = st.file_uploader(
    "Upload Your eBook",
    type=["txt", "pdf", "docx"]
)

content_type = st.selectbox(
    "Choose What To Generate",
    [
        "Instagram Captions",
        "TikTok Hooks",
        "Skool Classroom Content",
        "Email Campaign",
        "Sales Funnel Copy",
        "Website Copy",
        "Course Outline"
    ]
)

if st.button("Generate Content"):

    if not api_key:
        st.error("Please enter your OpenAI API key.")

    elif not uploaded_file:
        st.error("Please upload a file.")

    else:

        client = OpenAI(api_key=api_key)

        try:
            text = uploaded_file.read().decode("utf-8")
        except:
            text = str(uploaded_file.read())

        prompt = f"""
        You are an elite AI marketing assistant.

        Analyze this eBook content:

        {text}

        Generate:
        {content_type}

        Make it high-converting, luxury, viral,
        emotionally persuasive, and professionally formatted.
        """

        with st.spinner("Generating..."):

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            result = response.choices[0].message.content

        st.success("Done!")

        st.text_area(
            "Generated Content",
            result,
            height=500
        )

        st.download_button(
            "Download Result",
            result,
            file_name="generated_content.txt"
        )
