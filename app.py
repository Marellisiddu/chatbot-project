import streamlit as st
from groq import Groq

# Title
st.title("AI Chatbot")

# Groq API
client = Groq(api_key="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")

# User input
user_input = st.text_input("")

# Generate response
if user_input:
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": user_input}
        ],
        temperature=1,
        max_tokens=1024
    )

    response = completion.choices[0].message.content

    st.write("🤖 Bot:", response)
