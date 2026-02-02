import streamlit as st
import pandas as pd

# 1. Judul & Ikon
st.set_page_config(page_title="Ruang Miniatur", page_icon="✂️")

# 2. Header dengan Gaya
st.markdown("<h1 style='text-align: center;'>✂️ Ruang Miniatur</h1>", unsafe_allow_all_html=True)
st.markdown("<p style='text-align: center; color: gray;'><i>Dunia dalam Genggaman: Tutorial & Kerajinan Miniatur Eksklusif</i></p>", unsafe_allow_all_html=True)
st.divider()

# 3. LINK GOOGLE SHEETS (Ganti teks di bawah ini)
LINK_SHEETS = "https://docs.google.com/spreadsheets/d/1UHXQlYs8jYe-DKYIW4CxXAs4ww_vlQLK8XBeqUQGnIo/edit?usp=sharing"

try:
    base_url = LINK_SHEETS.split('/edit')[0]
    csv_url = f"{base_url}/export?format=csv"
    df = pd.read_csv(csv_url)

    # Membuat 2 kolom agar tidak terlalu memanjang ke bawah
    col1, col2 = st.columns(2)

    for index, row in df.iterrows():
        # Membagi produk ke kolom kiri dan kanan secara otomatis
        target_col = col1 if index % 2 == 0 else col2
        
        with target_col:
            with st.container(border=True):
                st.markdown(f"### 📦 {row['Produk']}")
                st.markdown(f"<h4 style='color: #E67E22;'>Rp {row['Harga']:,}</h4>", unsafe_allow_all_html=True)
                st.write(f"📝 {row['Deskripsi']}")
                
                # Tombol Beli yang Full Width dan Mencolok
                st.link_button(f"✨ Pesan Sekarang", row['Link_Beli'], use_container_width=True)

except Exception as e:
    st.info("💡 Hubungkan Google Sheets kamu agar katalog muncul.")

st.divider()
st.caption("© 2026 Ruang Miniatur | Teman Kreatif Kamu")
