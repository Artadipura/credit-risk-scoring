import streamlit as st
import pandas as pd
import pickle

# 1. LOAD OTAK AI YANG UDAH DISIMPAN TADI
with open('model_kredit_baru.pkl', 'rb') as file:
    model = pickle.load(file)

# 2. BIKIN JUDUL & TEKS DI WEBSITE
st.title("Aplikasi Prediksi Risiko Kredit 🏦")
st.write("Masukkan data calon nasabah untuk mengecek apakah pinjamannya aman atau berpotensi macet.")

# 3. Bikin Kolom Inputan Formulir (Sekarang pakai Rupiah!)
umur = st.number_input("Umur Nasabah", min_value=18, max_value=100, value=30)

# Pakai step=1000000 biar kalau tombol panahnya diklik, nambahnya sejuta-sejuta
gaji_rp = st.number_input("Pendapatan Tahunan (Rp)", min_value=0, value=150000000, step=1000000)
pinjaman_rp = st.number_input("Jumlah Pinjaman (Rp)", min_value=0, value=50000000, step=1000000)
bunga = st.number_input("Suku Bunga (%)", min_value=0.0, value=10.5)

# 4. Tombol Eksekusi
if st.button("Cek Risiko Kredit"):
    
    # TRIK SULAP: Konversi diam-diam Rupiah ke "skala Dollar" biar AI nggak kaget
    gaji = gaji_rp / 15000
    pinjaman = pinjaman_rp / 15000
    
    # Hitung rasio beban pinjaman otomatis
    beban = pinjaman / gaji if gaji > 0 else 0
    
    # Bungkus data inputan dari web jadi format tabel Pandas
    data_baru = pd.DataFrame({
        'person_age': [umur],
        'person_income': [gaji],
        'loan_amnt': [pinjaman],
        'loan_int_rate': [bunga],
        'beban_pinjaman': [beban]
    })
    
    # Suruh AI menebak
    hasil = model.predict(data_baru)
    
    # Tampilkan hasilnya
    if hasil[0] == 1:
        st.error("🚨 RISIKO TINGGI: Nasabah ini berpotensi GAGAL BAYAR!")
    else:
        st.success("✅ AMAN: Nasabah ini berpotensi LANCAR membayar.")