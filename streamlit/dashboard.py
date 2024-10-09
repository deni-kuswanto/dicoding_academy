import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set gaya seaborn
sns.set(style='dark')

# Membaca data dari CSV
all_df = pd.read_csv("./streamlit/all_data.csv")

# Menampilkan nama kolom
print("Nama kolom dalam DataFrame:", all_df.columns)

# Mengisi nilai kosong di kolom 'Peak Usage Time' dan 'Hour'
all_df['Peak Usage Time'].fillna(method='ffill', inplace=True)
all_df['Hour'].fillna(method='ffill', inplace=True)

# Mengonversi 'Peak Usage Time' ke tipe datetime
all_df['Peak Usage Time'] = pd.to_datetime(all_df['Peak Usage Time'], format='%H:%M', errors='coerce')

# Mengurutkan berdasarkan waktu
all_df.sort_values(by='Peak Usage Time', inplace=True)

# Menentukan informasi analisis
total_rides = all_df['Total Rides'].sum()

# Menampilkan dashboard
st.header('Dashboard Bike Sharing Analysis')

st.subheader('Total Rides')
st.metric("Total Rides", value=total_rides)

# Visualisasi jumlah total rides per jam
plt.figure(figsize=(12, 6))
sns.barplot(x='Hour', y='Total Rides', data=all_df, palette='viridis')
plt.title('Total Rides per Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Total Rides')
plt.xticks(rotation=45)
st.pyplot(plt)

# Visualisasi berdasarkan kondisi cuaca
plt.figure(figsize=(12, 6))
sns.countplot(data=all_df, x='Weather Condition', palette='coolwarm')
plt.title('Total Rides by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Total Rides')
st.pyplot(plt)
