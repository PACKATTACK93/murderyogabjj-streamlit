import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Murder Yoga BJJ Club",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS for fonts, colors, and spacing
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        color: #1f2937;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        color: #4b5563;
        font-size: 24px;
        text-align: center;
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and subtitle
st.markdown('<div class="title">🥋 Murder Yoga Jiu-Jitsu Club</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Interactive BJJ + Yoga experience!</div>', unsafe_allow_html=True)

st.markdown("---")  # horizontal line

# Columns for sessions
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Morning Yoga")
    st.write("Start your day with energy and flexibility.")
    st.button("Join Morning Yoga")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Evening Jiu-Jitsu")
    st.write("End your day with strength and technique.")
    st.button("Join Evening Jiu-Jitsu")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Mixed Flow")
    st.write("Combine yoga and jiu-jitsu for balance.")
    st.button("Join Mixed Flow")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Example interactive widget
name = st.text_input("What's your name?")
if name:
    st.success(f"Welcome to the mats, {name}! 💪")

# Example info card for AI placeholder
st.markdown('<div class="card">', unsafe_allow_html=True)
st.info("AI features (Google/OpenAI) can be added here later via API keys.")
st.markdown('</div>', unsafe_allow_html=True)
