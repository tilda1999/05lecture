import streamlit as st
import numpy as np
import cv2

def decode_qrcode_page ():
    st.header("Decode QR Code")

    qrcode= st.file_uploader("Upload your QR Code",
                     type=['jpg', 'png', 'jpeg','gif'])

    #check you can place a qr code
    if qrcode:
        #code to convert the image
        file_bytes= np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        st.image(qrcode)

        detector= cv2.QRCodeDetector()
        decoded_info, point, straight_qr, = detector.detectAndDecode(opencv_image)
        st.write(f"Your Code Contained {decoded_info}")
