import streamlit as st
import pandas as pd
import joblib

# Muat model
model = joblib.load("model.pkl")

# Judul
st.title("Prediksi Cuaca Hari Ini 🌦️")
st.write("Masukkan data suhu, kelembaban, dan kecepatan angin untuk memprediksi apakah hari ini hujan atau tidak.")

# Input manual user
suhu = st.slider("Suhu (°C)", 20.0, 40.0, 30.0)
kelembaban = st.slider("Kelembaban (%)", 50, 100, 80)
angin = st.slider("Kecepatan Angin (m/s)", 0.0, 10.0, 2.0)

# Prediksi
if st.button("Prediksi"):
    data = pd.DataFrame([[suhu, kelembaban, angin]], columns=['suhu', 'kelembaban', 'kecepatan_angin'])
    prediksi = model.predict(data)[0]

    st.subheader("Hasil Prediksi:")
    if prediksi == "Hujan Lebat":
        st.error("🌧️ Hujan Lebat")
    elif prediksi == "Hujan Ringan":
        st.warning("🌦️ Hujan Ringan")
    else:
        st.success("☀️ Tidak Hujan")