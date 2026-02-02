import streamlit as st
import pandas as pd

# 1. Judul & Tema Dasar (Tanpa CSS Rumit agar Anti-Error)
st.set_page_config(page_title="Ruang Miniatur", page_icon="✂️")

st.title("✂️ Ruang Miniatur")
st.write("Temukan panduan eksklusif pembuatan miniatur di sini.")
st.divider()

# 2. LINK GOOGLE SHEETS (Ganti teks di bawah ini dengan link kamu)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1UHXQlYs8jYe-DKYIW4CxXAs4ww_vlQLK8XBeqUQGnIo/edit?usp=sharing"

try:
    # Mengambil data dari Google Sheets
    csv_url = SHEET_URL.split('/edit')[0] + '/export?format=csv'
    df = pd.read_csv(csv_url)

    # Menampilkan Produk satu per satu ke bawah
    for index, row in df.iterrows():
        # Membuat kotak informasi untuk setiap produk
        with st.container(border=True):
            st.subheader(row['Produk'])
            st.write(f"💰 **Harga: Rp {row['Harga']}**")
            st.write(row['Deskripsi'])
            st.link_button(f"Beli {row['Produk']}", row['Link_Beli'], use_container_width=True)
            st.write("") 

except Exception as e:
    st.info("Satu langkah lagi! Masukkan link Google Sheets kamu di kode baris 13 agar produk muncul di sini.")
