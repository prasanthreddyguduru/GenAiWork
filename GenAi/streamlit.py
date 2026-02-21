import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
)

st.title("Career Growth Advisor for IT Professionals")

skillset = st.text_input("Enter your current skillset (e.g., Python, Java, Cloud, Testing):")

experience_input = st.text_input("Enter your years of experience:")

domain = st.selectbox(
    "Select your domain / interest area:",
    ["Web Development", "Data Engineering", "AI / Machine Learning", "DevOps / Cloud", "Cybersecurity", "Mobile Development", "General Software Development"]
)

if st.button("Get Answer"):

    if not skillset or not experience_input:
        st.warning("Please fill in all fields.")
    else:
        try:
            experience = float(experience_input)

            if experience < 0:
                st.error("Experience cannot be negative.")
            else:
                messages = [
                    {
                        "role": "system",
                        "content": "You are an expert IT career advisor helping experienced professionals choose high-value skills."
                    },
                    {
                        "role": "user",
                        "content": f"I am an IT professional with {experience} years of experience. "
                                   f"My current skills include {skillset}. "
                                   f"I am interested in {domain}. "
                                   f"What technologies, tools, or skills should I learn next to stay competitive and grow my career?"
                    }
                ]

                with st.spinner("Analyzing career path..."):
                    response = llm.invoke(messages)

                st.write("**Answer:**")
                st.write(response.content)

        except ValueError:
            st.error("Please enter a valid number for experience (example: 3 or 5.5).")