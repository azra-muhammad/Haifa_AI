import streamlit as st
import google.generativeai as genai

# --- PAGE SETUP ---
st.set_page_config(page_title="Haifa AI", page_icon="🤖")

st.title("🤖 Haifa AI: Evidence Finder")
st.write("Paste a story below, ask a question, and I will find the evidence for you!")

# --- AUTOMATIC KEY LOADING ---
try:
    api_key = st.secrets["GEMINI_KEY"]
except:
    st.error("⚠️ I couldn't find the API Key! Make sure you added it to the 'Secrets' in settings.")
    st.stop()

genai.configure(api_key=api_key)

# --- THE APP ---
story = st.text_area("Paste the Story Here:", height=200)
question = st.text_input("What is your question about the story?")

if st.button("Find Evidence"):
    if story and question:
        with st.spinner("Reading the story and looking for clues..."):
            try:
                # 1. Select the model (UPDATED NAME)
                model = genai.GenerativeModel('gemini-1.5-flash')

                # 2. Create the prompt
                my_prompt = f"""
                Here is a story:
                {story}

                Here is a question about the story:
                {question}

                Please answer the question. After the answer, provide direct quotes 
                from the text that support your answer. Label the quotes as 'Evidence'.
                """

                # 3. Get the response
                response = model.generate_content(my_prompt)
                
                # 4. Show the result
                st.success("Analysis Complete!")
                st.write(response.text)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter both a story and a question first!")