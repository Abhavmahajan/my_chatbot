import streamlit as st  
import google.generativeai as genai 
import webbrowser    

if "chat_data" not in st.session_state:
    st.session_state.chat_data = []


genai.configure(api_key="AIzaSyBTS7aw5BS5AUewYJ7OrkhN_r0YceihUHY")


model = genai.GenerativeModel("gemini-2.5-flash")

st.header("🤖 My Personal AI Bot 🤖")
st.subheader("❔ Ask me anything")

user_input = st.chat_input("Write your question here...")

if user_input:
    st.session_state.chat_data.append(("Me", user_input))

    lower_input = user_input.lower()

    if ("who built you" in lower_input or 
        "who made you" in lower_input or 
        "who created you" in lower_input):
        
        response_text = "I was built by Google using the Gemini AI model."

    elif "open youtube" in lower_input:
        webbrowser.open("https://www.youtube.com")
        response_text = "Sure! Here's the link: [YouTube](https://www.youtube.com)"
    elif "open google" in user_input:
        webbrowser.open("https://www.google.com")
    else:
        response = model.generate_content(user_input)
        response_text = response.text

    st.session_state.chat_data.append(("AI", response_text))

for sender, message in st.session_state.chat_data:
    with st.chat_message(sender):
        if sender == "AI":
            st.warning(message)
        else:
            st.success(message)
