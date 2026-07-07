# AI Study Assistant

An AI-powered web app that helps students prepare for competitive exams like GATE, JEE, and UPSC by generating structured answers to any question.

## Features
- Ask any exam-related question and get a detailed AI-generated answer
- Download the answer as a formatted PDF
- Clean and simple web interface

- ## screenshot

- <img width="1691" height="737" alt="image" src="https://github.com/user-attachments/assets/26072488-4968-4b0e-8c40-58334be8d9c6" />

<img width="1692" height="891" alt="image" src="https://github.com/user-attachments/assets/9d7cf097-c04a-4f56-a5fe-472a9adf4410" />

<img width="1483" height="912" alt="image" src="https://github.com/user-attachments/assets/9402877e-6b78-42e2-a8ce-5f48973735b5" />


## Tech Stack
- Python
- Streamlit
- Groq API (Llama 3)
- FPDF2
- python-dotenv

## How to Run
1. Clone the repo
2. Install dependencies: `pip install streamlit groq fpdf2 python-dotenv`
3. Create a `.env` file and add your Groq API key: `GROQ_API_KEY=your_key_here`
4. Run: `streamlit run application.py`
