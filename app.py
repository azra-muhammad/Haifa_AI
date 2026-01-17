import streamlit as st
import google.generativeai as genai
import importlib.metadata

st.title("🛠 Haifa AI: Diagnostic Mode")

# 1. Check the Library Version
try:
    version = importlib.metadata.version("google-generativeai")
    st.write(f"**Installed Library Version:** `{version}`")
except:
    st.error("Library not found!")

# 2. Check the API Key & Connection
try:
    api_key = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=api_key)
    st.success("✅ API Key found and configured.")
    
    # 3. Ask Google: "What models do you have?"
    st.write("### 📋 List of Available Models:")
    st.write("The app sees these models as valid:")
    
    models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            models.append(m.name)
            st.code(f"{m.name}")
            
except Exception as e:
    st.error(f"❌ Connection Error: {e}")