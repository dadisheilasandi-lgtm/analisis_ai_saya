import streamlit as st
import pandas as pd
import google.generativeai as genai

# GANTI DENGAN DATA KAMU
API_KEY = "AIzaSyC8uOdQJ2S24M8q34tWRfBu6a--9lJVLIw"
SHEET_URL = "https://docs.google.com/spreadsheets/d/1DCGSVQ0f1eM0t4sXZWY5S4Ruvzf2hgOU/edit?usp=sharing&ouid=109759809706529099005&rtpof=true&sd=true"

st.title("🤖 Asisten Analis Data Pro")

if API_KEY and SHEET_URL:
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        
        # Proses Link Sheets ke CSV
        csv_url = SHEET_URL.split('/edit')[0] + '/export?format=csv'
        df = pd.read_csv(csv_url)
        
        st.write("### Data Analisis:", df.head())

        user_ask = st.text_input("Tanya apa saja tentang data ini (Contoh: 'Tampilkan grafik batang')")
        
        if user_ask:
            if "grafik" in user_ask.lower():
                st.bar_chart(df.set_index(df.columns[0]))
            else:
                response = model.generate_content(f"Data: {df.to_string()}. Pertanyaan: {user_ask}")
                st.write(response.text)
    except Exception as e:
        st.error(f"Ada masalah: {e}")
