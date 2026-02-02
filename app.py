import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Ruang Miniatur", page_icon="✂️", layout="centered")

# 2. CSS Aman untuk Warna-Warni Kotak
st.markdown("""
<style>
    .card-biru { background-color: #e3f2fd; padding: 20px; border-radius: 15px; border-left: 10px solid #2196f3; margin-bottom: 20px; }
    .card-hijau { background-color: #e8f5e9; padding: 20px; border-radius: 15px; border-left: 10px solid #4caf50; margin-bottom: 20px; }
    .card-kuning { background-color: #fffde7; padding: 20px; border-radius: 15px; border-left: 10px solid #fbc02d; margin-bottom: 20px; }
    .card-pink { background-color: #fce4ec; padding: 20px; border-radius: 15px; border-left: 10px solid #e91e63; margin-bottom: 20px; }
    h3 { margin-top: 0; color: #333; }
</style>
""", unsafe_allow_all_html=True)

# 3. Header
st.title("✂️ Ruang Miniatur")
st.write("Pilih tutorial miniatur favoritmu dan mulailah berkreasi!")
st.divider()

# 4. LINK GOOGLE SHEETS
LINK_SHEETS = "MASUKKAN_LINK_GOOGLE_SHEETS_KAMU_DISINI"

try:
    base_url = LINK_SHEETS.split('/edit')[0]
    csv_url = f"{base_url}/export?format=csv"
    df = pd.read_csv(csv_url)

    # Daftar pilihan desain warna
    warna_list = ["card-biru", "card-hijau", "card-kuning", "card-pink"]

    for index, row in df.iterrows():
        # Pilih warna berdasarkan urutan produk
        warna_pilihan = warna_list[index % len(warna_list)]
        
        # Tampilkan Kotak Berwarna
        st.markdown(f"""
        <div class="{warna_pilihan}">
            <h3>{row['Produk']}</h3>
            <p style='font-size: 20px; font-weight: bold; color: #d35400;'>Rp {row['Harga']}</p>
            <p>{row['Deskripsi']}</p>
        </div>
        """, unsafe_allow_all_html=True)
        
        # Tombol Beli
        st.link_button(f"✨ Pesan {row['Produk']}", row['Link_Beli'], use_container_width=True)
        st.write("")

except Exception as e:
    st.info("💡 Link Google Sheets belum terpasang di baris 24.")

st.divider()
st.caption("© 2026 Ruang Miniatur | Teman Kreatif Kamu")
