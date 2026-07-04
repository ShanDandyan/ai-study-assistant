# AI Study Assistant

An AI-powered web app that helps students prepare for competitive exams like GATE, JEE, and UPSC by generating structured answers to any question.

## Features
- Ask any exam-related question and get a detailed AI-generated answer
- Download the answer as a formatted PDF
- Clean and simple web interface

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
