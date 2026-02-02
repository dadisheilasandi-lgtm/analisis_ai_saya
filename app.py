import streamlit as st
import pandas as pd

# 1. Setting Halaman
st.set_page_config(page_title="Ruang Miniatur", page_icon="✂️", layout="centered")

# 2. Header Tanpa HTML (Aman dari Error)
st.title("Ruang Miniatur")
st.caption("Dunia dalam Genggaman: Tutorial & Kerajinan Miniatur Eksklusif")
st.divider()

# 3. LINK GOOGLE SHEETS (Ganti link di bawah ini dengan link kamu)
LINK_SHEETS = "https://docs.google.com/spreadsheets/d/1UHXQlYs8jYe-DKYIW4CxXAs4ww_vlQLK8XBeqUQGnIo/edit?usp=sharing"

try:
    # Memproses link Sheets
    base_url = LINK_SHEETS.split('/edit')[0]
    csv_url = f"{base_url}/export?format=csv"
    df = pd.read_csv(csv_url)

    # Menampilkan Katalog dengan Desain Box
    for index, row in df.iterrows():
        # Membuat box dengan warna border yang rapi
        with st.container(border=True):
            # Baris Judul & Harga
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown(f"### {row['Produk']}")
            with col_b:
                # Harga dengan warna oranye agar menonjol
                st.subheader(f":orange[Rp {row['Harga']}]")
            
            # Deskripsi
            st.write(f"📝 {row['Deskripsi']}")
            
            # Tombol Beli dengan desain Full Width
            st.link_button(f"✨ Ambil Tutorial Ini", row['Link_Beli'], use_container_width=True)

except Exception as e:
    st.warning("Silakan masukkan link Google Sheets kamu pada kode baris 14.")

# 4. Footer
st.divider()
st.center_text = st.caption("© 2026 Ruang Miniatur | Teman Kreatif Kamu")
