import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman & CSS
st.set_page_config(page_title="Ruang Miniatur", page_icon="✂️", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #e67e22;
        color: white;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_all_html=True)

# 2. Header
st.title("✂️ Ruang Miniatur")
st.write("Dapatkan tutorial kerajinan tangan miniatur terbaik di sini.")

# 3. Link Google Sheets (PASTIKAN LINK KAMU ADA DI SINI)
SHEET_URL = "MASUKKAN_LINK_GOOGLE_SHEETS_KAMU_DISINI"

try:
    csv_url = SHEET_URL.split('/edit')[0] + '/export?format=csv'
    df = pd.read_csv(csv_url)

    col1, col2 = st.columns(2)
    for index, row in df.iterrows():
        target_col = col1 if index % 2 == 0 else col2
        with target_col:
            st.markdown(f"""
            <div class="card">
                <h3 style='margin:0;'>{row['Produk']}</h3>
                <p style='color: #e67e22; font-weight: bold; font-size: 20px;'>Rp {row['Harga']}</p>
                <p style='color: #555;'>{row['Deskripsi']}</p>
            </div>
            """, unsafe_allow_all_html=True)
            st.link_button(f"Beli Tutorial", row['Link_Beli'])
            st.write("")

except Exception as e:
    st.info("💡 Hubungkan Google Sheets kamu pada baris 31 agar produk muncul.")
