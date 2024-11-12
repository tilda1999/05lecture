import streamlit as st
from decode_qrcode_page import decode_qrcode_page
from generate_qrcode_page import generate_qrcode_page

st.set_page_config(
    page_title=("QR Code Generator v2"),
    page_icon=("❤️")
)

options= ['Generate QR Code', 'Decode QR code', 'About Me']
page_selection= st.sidebar.selectbox ("Menu", options)

if page_selection == "Generate QR Code":
    st.title("GenerateGR Code")
    generate_qrcode_page ()
elif page_selection == "Decode QR code":
    decode_qrcode_page()
elif  page_selection== "About Me":
    st.write ("hi! My name is Tilda!")

