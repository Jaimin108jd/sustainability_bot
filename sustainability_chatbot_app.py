import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define the system prompt
system_prompt = """
You are a friendly and knowledgeable sustainability advisor chatbot.
Your job is to help users make eco-friendly purchasing decisions, reduce waste,
and recycle or repurpose items effectively.

Use simple and clear language. Include real-world product examples, creative ideas,
and tips that are practical. Do not use technical jargon. Avoid recommending expensive or luxury items.

Topics you handle include:
- Eco-friendly alternatives for common products
- How to recycle specific household items
- Tips for reducing food, plastic, or electronic waste
- Creative reuse ideas for clothes, bottles, boxes, etc.
- Advice on sustainable shopping and minimalism

If asked about unrelated topics, gently redirect back to sustainability.
"""

# Load Gemini model
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Categorize query
def classify_query(user_input):
    input_lower = user_input.lower()
    if any(word in input_lower for word in ["instead", "alternative", "replace", "swap", "substitute", "eco-friendly option"]):
        return "Sustainable Alternatives"
    elif any(word in input_lower for word in ["recycle", "disposal", "dispose", "trash", "reuse", "upcycle", "compost", "segregate"]):
        return "Recycling & Waste Management"
    else:
        return "Waste Reduction & Lifestyle Tips"

# Get response
def ask_sustainability_bot(user_input):
    try:
        category = classify_query(user_input)
        full_prompt = f"{system_prompt}\n\nUser: {user_input}\nBot:"
        response = model.generate_content(full_prompt)
        return category, response.text.strip()
    except Exception as e:
        return "Unknown", f"Error: {str(e)}"

# Streamlit App
st.set_page_config(page_title="Sustainability Chatbot", layout="centered")
st.title("Sustainable Lifestyle Chatbot")
st.write("Ask a question about eco-friendly living, recycling, or reducing waste.")

user_input = st.text_input("Enter your question:")

if user_input:
    with st.spinner("Thinking..."):
        category, reply = ask_sustainability_bot(user_input)
        st.subheader("Category")
        st.write(category)
        st.subheader("Response")
        st.write(reply)
