import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set gaya seaborn
sns.set(style='dark')

# Membaca data dari CSV
hour_dataframe = pd.read_csv("./streamlit/hour.csv")

st.header("Dashboard Bike Sharing Analysis")

#Pertanyaan 1:
# - Kapan waktu puncak penggunaan layanan penyewaan sepeda berdasarkan hari atau bulan?

st.subheader("Pertanyaan 1")
st.markdown("""
Kesimpulan untuk pertanyaan 1 yakni Kapan waktu puncak penggunaan layanan penyewaan sepeda berdasarkan hari atau bulan?

Berdasarkan analisis data dari kedua dataset, yaitu dataset harian dan dataset jam. Berdasarkan visualisasi dan analisis
yang dilakukan, terlihat bahwa penggunaan layanan bike sharing cenderung meningkat pada hari tertentu dalam seminggu.

Pada hari-hari akhir pekan, khususnya pada hari Sabtu dan Minggu, ketika lebih banyak orang memiliki waktu luang untuk
bersepeda, data menunjukkan bahwa penggunaan layanan ini juga mengalami lonjakan. Dari hasil temuan ini menunjukkan bahwa
faktor waktu memiliki peran penting dalam menentukan pola penggunaan penyewaan sepeda, sehingga  untuk memenuhi permintaan
pengguna secara optimal, perusahaan dapat mempertimbangkan penyesuaian jadwal operasional atau penambahan unit sepeda di
waktu-waktu puncak tersebut.
""")

# Mengonversi kolom 'dteday' ke tipe datetime
hour_dataframe['dteday'] = pd.to_datetime(hour_dataframe['dteday'])

# Menambahkan kolom untuk hari dan bulan
hour_dataframe['day'] = hour_dataframe['dteday'].dt.day_name()
hour_dataframe['month'] = hour_dataframe['dteday'].dt.month_name()

# Analisis berdasarkan hari
plt.figure(figsize=(12, 6))
sns.barplot(x='day', y='cnt', data=hour_dataframe, estimator=sum, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Jumlah Penyewaan Sepeda Berdasarkan Hari')
plt.xlabel('Hari')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(rotation=45)
st.pyplot(plt)

# Analisis berdasarkan bulan
plt.figure(figsize=(12, 6))
sns.barplot(x='month', y='cnt', data=hour_dataframe, estimator=sum, order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
plt.title('Jumlah Penyewaan Sepeda Berdasarkan Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(rotation=45)
st.pyplot(plt)

# Pertanyaan 2:
# - Bagaimana pengaruh kelembaban udara (hum) terhadap jumlah pengguna penyewaan sepeda?
st.subheader("Pertanyaan 2")
st.markdown("""
Kesimpulan untuk pertanyaan 2 yakni Bagaimana pengaruh kelembaban udara (hum) terhadap jumlah pengguna penyewaan sepeda?

Berdasarkan analisis yang dilakukan terhadap dua dataset yakni harian dan jam. Dari analisis yang menunjukkan hubungan
antara kelembapan dengan jumlah pengguna penyewaan sepeda, dapat dilihat bahwa kelembapan yang tinggi mengurangi minat
orang untuk menggunakan layanan penyewaan sepeda, karena kondisi tersebut mungkin dianggap tidak nyaman untuk bersepeda.
Temuan ini mengindikasikan bahwa penyedia layanan penyewaan sepeda harus mempertimbangkan faktor kelembaban udara (hum)
dalam strategi pemasaran dan operasional mereka, termasuk mengembangkan kampanye promosi khusus pada hari-hari dengan
kelembaban udara (hum) yang mendukung, untuk meningkatkan penggunaan layanan secara keseluruhan.
""")

# Mengonversi kolom 'dteday' ke tipe datetime
hour_dataframe['dteday'] = pd.to_datetime(hour_dataframe['dteday'])

# Analisis pengaruh kelembapan terhadap jumlah penyewaan
plt.figure(figsize=(12, 6))
sns.scatterplot(x='hum', y='cnt', data=hour_dataframe, alpha=0.6)
plt.title('Pengaruh Kelembaban udara (hum) terhadap Jumlah Penyewaan Sepeda')
plt.xlabel('Kelembaban (Normalisasi)')
plt.ylabel('Jumlah Penyewaan')
plt.grid()
st.pyplot(plt)