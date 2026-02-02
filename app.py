import streamlit as st
import pandas as pd

# Judul Website & Icon
st.set_page_config(page_title="Ruang Miniatur - Tutorial Kerajinan", page_icon="✂️", layout="wide")

# Header
st.title("✂️ Ruang Miniatur")
st.subheader("Belajar Membuat Dunia dalam Genggaman")
st.write("Dapatkan panduan lengkap langkah demi langkah membuat miniatur berkualitas tinggi.")
st.divider()

# LINK GOOGLE SHEETS KAMU
# Pastikan link ini adalah link Google Sheets yang aksesnya sudah "Anyone with the link"
SHEET_URL = "https://docs.google.com/spreadsheets/d/1UHXQlYs8jYe-DKYIW4CxXAs4ww_vlQLK8XBeqUQGnIo/edit?usp=sharing"

try:
    # Proses ambil data dari Google Sheets
    csv_url = SHEET_URL.split('/edit')[0] + '/export?format=csv'
    df = pd.read_csv(csv_url)

    # Tampilan Produk dalam bentuk Grid
    col1, col2 = st.columns(2)

    for index, row in df.iterrows():
        current_col = col1 if index % 2 == 0 else col2
        
        with current_col:
            # Menampilkan info produk tutorial
            st.markdown(f"### 📦 {row['Produk']}")
            st.write(f"💰 **Harga: Rp {row['Harga']}**")
            
            # Box Informasi Deskripsi
            st.info(f"**Tentang Tutorial:** \n\n {row['Deskripsi']}")
            
            # Tombol Beli via WA
            st.link_button(f"Pesan Tutorial {row['Produk']}", row['Link_Beli'], use_container_width=True)
            st.write("---")

except Exception as e:
    st.warning("Menunggu data dari Google Sheets... Pastikan link sudah benar dan kolom sesuai (Produk, Harga, Deskripsi, Link_Beli).")

# Footer
st.caption("© 2026 Ruang Miniatur - Dibuat dengan Streamlit")
