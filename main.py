import streamlit as st
import random
import time
import backend

st.set_page_config(page_title="Talkie Ai", page_icon="icon.png")

def response_generator(prompt):
    response = backend.GenerateResponse(prompt)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Talkie AI – Always For U")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can i help you today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})