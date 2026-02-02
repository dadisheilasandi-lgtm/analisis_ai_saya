import streamlit as st
import pandas as pd

# 1. Judul & Konfigurasi
st.set_page_config(page_title="Ruang Miniatur", page_icon="✂️")
st.markdown("<h1 style='text-align: center;'>✂️ Ruang Miniatur</h1>", unsafe_allow_all_html=True)
st.markdown("<p style='text-align: center;'>Belajar Membuat Dunia dalam Genggaman</p>", unsafe_allow_all_html=True)
st.divider()

# 2. LINK GOOGLE SHEETS (Ganti teks di bawah ini)
LINK_SHEETS = "https://docs.google.com/spreadsheets/d/1UHXQlYs8jYe-DKYIW4CxXAs4ww_vlQLK8XBeqUQGnIo/edit?usp=sharing"

try:
    base_url = LINK_SHEETS.split('/edit')[0]
    csv_url = f"{base_url}/export?format=csv"
    df = pd.read_csv(csv_url)

    # List Warna Pastel (Aman & Cantik)
    # 0=Biru, 1=Hijau, 2=Kuning, 3=Merah Muda
    warna_box = ["#E3F2FD", "#E8F5E9", "#FFFDE7", "#FCE4EC"]
    warna_garis = ["#2196F3", "#4CAF50", "#FBC02D", "#E91E63"]

    for index, row in df.iterrows():
        pilih = index % 4
        
        # Kotak Berwarna menggunakan HTML sederhana
        st.markdown(f"""
            <div style="background-color: {warna_box[pilih]}; 
                        padding: 20px; 
                        border-radius: 15px; 
                        border-left: 10px solid {warna_garis[pilih]}; 
                        margin-bottom: 10px;">
                <h3 style="margin: 0; color: #333;">{row['Produk']}</h3>
                <h4 style="color: #D35400; margin: 5px 0;">Rp {row['Harga']}</h4>
                <p style="color: #555; margin-bottom: 0;">{row['Deskripsi']}</p>
            </div>
        """, unsafe_allow_all_html=True)
        
        # Tombol Beli (Gunakan tombol asli Streamlit agar lancar)
        st.link_button(f"🛒 Pesan {row['Produk']}", row['Link_Beli'], use_container_width=True)
        st.write("")

except Exception as e:
    st.info("💡 Hubungkan Google Sheets di baris 12 agar katalog muncul.")

st.divider()
st.caption("© 2026 Ruang Miniatur | Teman Kreatif Kamu")
