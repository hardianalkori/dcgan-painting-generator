
import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2, io
from keras.models import load_model
from tensorflow.keras.preprocessing.image import array_to_img

landscape = load_model("model/portrait_final.h5")

st.set_page_config(
    page_title = "Lucky Eights | Portrait",page_icon="asset/LE.ico")

logo_image = Image.open('asset/LE.png')
st.sidebar.image(logo_image, use_column_width=True)

st.title("CIPTAKAN LUKISAN PORTRAIT SEKARANG !")
st.write("Ciptakan karya seni lukisan unik dengan cepat dan mudah menggunakan teknologi Generative Adversarial Networks (GAN) hanya dengan satu klik👇🏻")

st.markdown(
    """
    <style>
    .column-border {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 5px;		
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        background-color: #F5F5F5;

    }
    </style>
    """,
    unsafe_allow_html=True
)

kiri, tengah, kanan = st.columns([10,1,2.5])

def demo(lukisan):
	wall = Image.open("asset/wall.png")
	wall = wall.convert("RGB")

	frame = Image.open("asset/frame.png")
	frame = frame.resize((150,150))

	lukisan = lukisan.convert("RGBA")
	lukisan = lukisan.resize((132,132))

	frame.paste(lukisan,(10,10),lukisan)
	wall.paste(frame,(386,186))

	return wall, lukisan

if st.button(label='Generate!'):
	noise = tf.random.normal([1, 100])
	output = landscape.predict(noise)
	img = (output * 127.5) + 127.5
	img = array_to_img(img[0])
	wallpaper, painting = demo(img)

	with kiri:
		st.markdown('<div class="column-border">DEMO</div>', unsafe_allow_html=True)
		st.image(wallpaper)

	with kanan:
		st.markdown('<div class="column-border">PREVIEW</div>', unsafe_allow_html=True)
		st.image(img)
		img_byte_arr = io.BytesIO()
		img.save(img_byte_arr, format='JPEG')
		img_bytes = img_byte_arr.getvalue()
		st.download_button(label='Download', data=img_bytes, file_name='generated_image.jpeg', mime='image/jpeg')


st.subheader("APA ITU LUKISAN PORTRAIT?")
st.image("asset/portrait.png")
st.markdown('<div style="text-align: justify;">Lukisan Portrait merupakan tipe lukisan yang mengedepankan model sebagai focal point yang artinya pusat perhatian atau interest. Lukisan portrait menangkap esensi, kepribadian, ekspresi dan perasaan seseorang dengan memanfaatkan latar belakang, pencahayaan, dan pose.</div>', unsafe_allow_html=True)
