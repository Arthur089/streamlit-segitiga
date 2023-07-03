import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# Web Menghitung Luas Segitiga
Ini adalah aplikasi menghitung luas segitiga sederhana menggunakan bahasa pemrograman Python.
""")

alas = st.number_input("Masukkan Alas Segitiga", 0)
tinggi = st.number_input("Masukkan Tinggi Segitiga", 0)
hitung = st.button("Hitung Luas Segitiga")

if hitung:
    luas = (alas*tinggi)/2
    st.success("Luas Segitiganya Adalah: {:.1f}".format(luas))
    st.balloons()