import streamlit as st

# Page configuration
st.set_page_config(page_title="Murder Yoga BJJ Club", layout="wide")

# Title and header
st.title("🥋 Murder Yoga Jiu-Jitsu Club")
st.subheader("Welcome to the interactive BJJ + Yoga app!")

# Example interactive widget
name = st.text_input("What's your name?")
if name:
    st.success(f"Welcome to the mats, {name}!")

# Example selection
session = st.selectbox(
    "Choose your session:",
    ["Morning Yoga", "Evening Jiu-Jitsu", "Mixed Flow"]
)
st.write(f"You selected: **{session}**")

# Example AI integration placeholder
st.info("AI features (Google/OpenAI) can be added here later via API keys.")
