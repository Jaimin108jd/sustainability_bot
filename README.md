🌱 EcoBot – Your Sustainability Assistant
EcoBot is an AI-powered Sustainability Advisor Chatbot built using Streamlit and Google Gemini API.


✅ Features
Eco-Friendly Alternatives – Suggests sustainable swaps for common items.
Recycling & Waste Management – Guides proper disposal, recycling, and composting.
Creative Reuse & Upcycling – Ideas to repurpose household items.
Sustainable Lifestyle Tips – Minimalist and waste-reducing practices.
Interactive UI – Built with Streamlit, includes clean design, custom CSS, and animations.

🛠️ Tech Stack
Python 3.10+
Streamlit – Interactive web UI
Google Gemini API – AI-powered responses
dotenv – Environment variable management

📂 Project Structure
bash
Copy
Edit
Sustainability_bot/
│── sustainability_chatbot_app.py      # Main Streamlit application
│── .env                               # Environment variables (API Key)
│── requirements.txt                   # Dependencies
│── README.md                          # Project documentation

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/ecobot.git
cd ecobot

3. Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

5. Install Dependencies
pip install -r requirements.txt

7. Set Up API Key
Create a .env file in the project root and add:
GEMINI_API_KEY=your_google_gemini_api_key

▶️ Run the App
streamlit run sustainability_chatbot_app.py
The app will open in your browser at:
http://localhost:8501

✅ Example Questions
"What are alternatives to plastic water bottles?"
"How can I recycle old electronics?"
"Ways to reduce food waste at home"
"Eco-friendly cleaning products I can make"

📸 UI Preview:

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3697ad64-ca23-499c-9af4-073bd9687546" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/50dcff6c-54c1-4af5-8fc2-7f0db52ace4a" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6a95330d-5f79-4363-8ee7-a64744ed2cf0" />



