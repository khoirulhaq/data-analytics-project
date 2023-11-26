import streamlit as st
import pandas as pd
import plotly.express as px

# Fungsi untuk membuat visualisasi dan menemukan jam dengan frekuensi tertinggi
def visualize_purchase_frequency(df):
    # Konversi kolom order_purchase_timestamp ke tipe data datetime
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

    # Ekstrak jam dari timestamp
    df['purchase_hour'] = df['order_purchase_timestamp'].dt.hour

    # Hitung frekuensi pembelian di setiap jam
    purchase_hour_counts = df['purchase_hour'].value_counts().sort_index()

    # Temukan jam dengan frekuensi tertinggi
    jam_tertinggi = purchase_hour_counts.idxmax()
    frekuensi_tertinggi = purchase_hour_counts.max()

    # Tampilkan jam dengan frekuensi tertinggi
    st.write(f"Jam dengan frekuensi tertinggi: {jam_tertinggi}, Frekuensi: {frekuensi_tertinggi}")

    # Plot histogram menggunakan Plotly Express
    fig = px.bar(x=purchase_hour_counts.index, y=purchase_hour_counts.values,
                 labels={'x': 'Hour of the Day', 'y': 'Number of Purchases'},
                 title='Purchase Frequency by Hour',
                 color_discrete_sequence=['skyblue'])

    # Tampilkan plot di aplikasi Streamlit
    st.plotly_chart(fig)

# Baca DataFrame dari file CSV
file_path = "orders_dataset.csv"  # Ganti dengan path ke file CSV Anda
df = pd.read_csv(file_path)

# Tampilkan judul aplikasi
st.title('Purchase Frequency Analysis')

# Tampilkan visualisasi dan informasi jam dengan frekuensi tertinggi
visualize_purchase_frequency(df)
