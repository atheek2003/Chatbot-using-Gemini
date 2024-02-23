import streamlit as st 
import os
import google.generativeai as genai 

# Configure Generative AI API key
genai.configure(api_key='Your_api_key ')

# Function to load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get response from Gemini
def get_gemini_response(question):
    try:
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Initialize Streamlit app
st.set_page_config(page_title="Chat-bot ")
st.header("Chat-bot with Gemini ")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input
input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Send")

if submit_button and input_text:
    # Get Gemini response
    response = get_gemini_response(input_text)

    # Add user query and response to chat history
    st.session_state['chat_history'].append(("You", input_text))
    
    st.subheader("The response is")
    
    # Display Gemini response
    if response:
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))

# Display chat history in the sidebar
st.sidebar.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    st.sidebar.write(f"{role}: {text}")
