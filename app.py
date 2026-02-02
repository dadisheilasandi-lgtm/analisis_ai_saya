import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ruang Miniatur", page_icon="✂️")

st.title("✂️ Ruang Miniatur")
st.write("Katalog Tutorial Kerajinan Tangan")

# BARIS 10: PASTIKAN LINK INI BENAR
LINK_SHEETS = "https://docs.google.com/spreadsheets/d/1UHXQlYs8jYe-DKYIW4CxXAs4ww_vlQLK8XBeqUQGnIo/edit?usp=sharing"

try:
    # Rumus sakti baca Google Sheets
    base_url = LINK_SHEETS.split('/edit')[0]
    csv_url = f"{base_url}/export?format=csv"
    df = pd.read_csv(csv_url)

    for index, row in df.iterrows():
        # Pakai fitur 'status' untuk kasih warna kotak secara otomatis
        # Ada warna Biru (info), Hijau (success), dan Oranye (warning)
        warna = ["info", "success", "warning"]
        pilih_warna = warna[index % len(warna)]
        
        if pilih_warna == "info":
            with st.info(f"### {row['Produk']}"):
                st.write(f"💰 **Harga: Rp {row['Harga']}**")
                st.write(row['Deskripsi'])
                st.link_button("Beli Sekarang", row['Link_Beli'])
        elif pilih_warna == "success":
            with st.success(f"### {row['Produk']}"):
                st.write(f"💰 **Harga: Rp {row['Harga']}**")
                st.write(row['Deskripsi'])
                st.link_button("Beli Sekarang", row['Link_Beli'])
        else:
            with st.container(border=True):
                st.markdown(f"### :orange[{row['Produk']}]")
                st.write(f"💰 **Harga: Rp {row['Harga']}**")
                st.write(row['Deskripsi'])
                st.link_button("Beli Sekarang", row['Link_Beli'])
        st.write("")

except Exception as e:
    st.error(f"Gagal baca data: {e}")
