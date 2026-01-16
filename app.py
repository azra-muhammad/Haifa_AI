import streamlit as st
import google.generativeai as genai

# 1. Title and Setup
st.set_page_config(page_title="Gemini Evidence Finder", page_icon="✨")
st.title("✨ Gemini Evidence Finder")
st.write("Paste a story, tell me your theory, and I'll find the proof!")

# 2. Sidebar for the Gemini Key
with st.sidebar:
    api_key = st.text_input("Paste Gemini API Key:", type="password")
    st.info("Get your free key at aistudio.google.com")

# 3. Input Boxes
story_text = st.text_area("📖 Paste the Story here:", height=200)
student_claim = st.text_input("🤔 What is your theory?")

# 4. The Button
if st.button("Find Evidence"):
    if not api_key:
        st.error("Please enter the Gemini Key in the sidebar.")
    elif not story_text:
        st.warning("Please paste a story first.")
    else:
        try:
            # Configure the Google Brain
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')

            # The Instructions
            my_prompt = f"""
            Read this story: "{story_text}"
            
            The student believes: "{student_claim}"
            
            Task: Find 2 direct quotes from the story that support the student's belief.
            Explain why.
            """

            # Ask Gemini
            with st.spinner("Gemini is thinking..."):
                response = model.generate_content(my_prompt)
                st.success("Found it! Here is the evidence:")
                st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")