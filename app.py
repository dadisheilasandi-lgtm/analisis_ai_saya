import streamlit as st
import pandas as pd

# Judul Utama
st.title("✂️ Ruang Miniatur")
st.write("Katalog Tutorial Miniatur")

# GANTI LINK DI BAWAH INI
LINK_SHEETS = "MASUKKAN_LINK_GOOGLE_SHEETS_DI_SINI"

try:
    # Membaca Data
    csv_url = LINK_SHEETS.split('/edit')[0] + '/export?format=csv'
    df = pd.read_csv(csv_url)

    # Loop Produk dengan Kotak Berwarna Bawaan
    for index, row in df.iterrows():
        # Kotak akan berganti warna otomatis: Biru, Hijau, Abu-abu
        if index % 3 == 0:
            with st.info(f"### {row['Produk']}"):
                st.write(f"Harga: **Rp {row['Harga']}**")
                st.write(row['Deskripsi'])
                st.link_button("Pesan Sekarang", row['Link_Beli'])
        elif index % 3 == 1:
            with st.success(f"### {row['Produk']}"):
                st.write(f"Harga: **Rp {row['Harga']}**")
                st.write(row['Deskripsi'])
                st.link_button("Pesan Sekarang", row['Link_Beli'])
        else:
            with st.container(border=True):
                st.markdown(f"### {row['Produk']}")
                st.write(f"Harga: **Rp {row['Harga']}**")
                st.write(row['Deskripsi'])
                st.link_button("Pesan Sekarang", row['Link_Beli'])
        st.write("")

except Exception as e:
    st.error("Ada masalah pada Link Google Sheets atau Nama Kolom.")
