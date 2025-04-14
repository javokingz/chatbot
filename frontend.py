import streamlit as st
import backend as lc

# Page title
st.set_page_config(page_title='Knowledge Bases for Amazon Bedrock and LangChain 🦜️🔗')

# Clear Chat History fuction
def clear_screen():
    st.session_state.messages = [{"role": "assistant", "content": "¿Cómo puedo ayudarte el día de hoy?"}]

with st.sidebar:
    st.title('Knowledge Bases for Amazon Bedrock 🦜️🔗')
    streaming_on = st.toggle('Streaming')
    st.button('Clear Screen', on_click=clear_screen)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "¿Cómo puedo ayudarte el día de hoy?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat Input - User Prompt 
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    if streaming_on:
        # Chain - Stream
        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_response = ''
            # Chain Stream
            for chunk in lc.chain.stream(prompt):
                if 'response' in chunk:
                    full_response += chunk['response']
                    placeholder.markdown(full_response)
                else:
                    full_context = chunk
            placeholder.markdown(full_response)
            with st.expander("Show source details >"):
                st.write(full_context)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
    else:
        # Chain - Invoke
        with st.chat_message("assistant"):
            response = lc.chain.invoke(prompt)
            st.write(response['response'])
            with st.expander("Show source details >"):
                st.write(response['context'])
            st.session_state.messages.append({"role": "assistant", "content": response['response']})