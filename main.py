import streamlit as st
from streamlit_option_menu import option_menu

# navigasi sidebar
with st.sidebar :
  selected = option_menu ('Hitung Luas Bangun made by zio', 
  ['hitung luas persegi panjang',
   'hitung luas segitiga'],                        
  default_index=0)

#halaman hitung luas persegi panjang
if (selected == 'hitung luas persegi panjang') :
    st.title('hitung luas persegi panjang')

    panjang = st.number_input ("masukan nilai panjang")
    lebar = st.number_input ("masukan nilai lebar", 0)
    hitung = st.button ("hitung luas")

    if hitung :
        luas = panjang * lebar
        st.write ("luas persegi panjang adalah = ", luas)
        st.success (f"luas persegi panjang adalah = {luas}")

if (selected == 'hitung luas segitiga') :
  st.title('hitung luas segitiga')

  alas = st.slider ("masukan nilai alas", 0, 1000)
  tinggi = st.slider ("masukan tinggi", 0, 1000)
  hitung = st.button ("hitung luas")

  if hitung :
    luas = 0,5 * alas * tinggi
    st.write ("luas segitiga adalah =", luas)
    st.success (f"luas segitiga adalah = {luas}")


