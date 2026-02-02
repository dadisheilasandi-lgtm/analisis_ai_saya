import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman & CSS Custom
st.set_page_config(page_title="Ruang Miniatur - Toko Tutorial", page_icon="✂️", layout="wide")

st.markdown("""
    <style>
    /* Mengubah warna background halaman */
    .main {
        background-color: #f8f9fa;
    }
    /* Mendesain kartu produk */
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border: 1px solid #e9ecef;
        transition: transform 0.3s;
    }
    .product-card:hover {
        transform: translateY(-5px);
    }
    /* Judul Produk */
    .product-title {
        color: #2c3e50;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    /* Harga */
    .product-price {
        color: #e67e22;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_all_html=True)

# 2. Header Website
st.title("✂️ Ruang Miniatur")
st.markdown("#### *Belajar Membuat Dunia dalam Genggaman*")
st.write("Temukan panduan eksklusif pembuatan miniatur yang detail dan mudah diikuti.")
st.divider()

# 3. Link Google Sheets (Pastikan sudah diganti dengan link milikmu)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1UHXQlYs8jYe-DKYIW4CxXAs4ww_vlQLK8XBeqUQGnIo/edit?usp=sharing"

try:
    csv_url = SHEET_URL.split('/edit')[0] + '/export?format=csv'
    df = pd.read_csv(csv_url)

    # Tampilan Produk dalam Grid
    col1, col2 = st.columns(2)

    for index, row in df.iterrows():
        current_col = col1 if index % 2 == 0 else col2
        
        with current_col:
            # Menggunakan HTML untuk styling kartu
            st.markdown(f"""
                <div class="product-card">
                    <div class="product-title">📦 {row['Produk']}</div>
                    <div class="product-price">Rp {row['Harga']:,}</div>
                    <p style="color: #7f8c8d; margin-top: 10px;">{row['Deskripsi']}</p>
                </div>
            """, unsafe_allow_all_html=True)
            
            # Tombol Beli menggunakan tombol bawaan Streamlit agar fungsional
            st.link_button(f"Ambil Tutorial {row['Produk']}", row['Link_Beli'], use_container_width=True)
            st.write("") # Jarak antar produk

except Exception as e:
    st.info("💡 **Tips:** Segera masukkan link Google Sheets kamu di kode baris 42 dan pastikan kolomnya bernama: Produk, Harga, Deskripsi, Link_Beli")

# 4. Footer
st.divider()
st.caption("© 2026 Ruang Miniatur | Kembangkan Kreativitasmu")
