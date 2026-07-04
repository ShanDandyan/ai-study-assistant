import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from fpdf import FPDF
def Generate_pdf(question,answer):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12) 
    pdf.multi_cell(0,10,f" Question : {question} \n\n Answer : {answer}") 
    return bytes(pdf.output())      
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
client=Groq(api_key=api_key)
st.title("AI Study Assistant")
question=st.text_area("Enter your question here")
clicked=st.button(" Get response")
if clicked:
    with st.spinner(" Generating response. . ."):
        response=client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": question},
                {"role":"system","content":"You are an expert teacher helping Indian students prepare for competitive exams like GATE, JEE, and UPSC. Answer questions clearly and concisely with structured explanations. Use examples where helpful. Keep answers exam-focused. "}

            ]
        )
        answer=response.choices[0].message.content
        st.write(answer)
        pdf_bytes=Generate_pdf( question,answer)
        st.download_button("Download PDF",data=pdf_bytes,file_name="Answers.pdf",mime="application/pdf")

