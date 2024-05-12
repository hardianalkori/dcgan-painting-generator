import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2, io
from keras.models import load_model
from keras_preprocessing.image import array_to_img

landscape = load_model("model/landscape_final.h5")

st.set_page_config(
    page_title = "Lucky Eights | Landscape",page_icon="asset/LE.ico")

logo_image = Image.open('asset/LE.png')
st.sidebar.image(logo_image, use_column_width=True)

st.title("CIPTAKAN LUKISAN LANDSCAPE SEKARANG !")
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
k, t, ka = st.columns([2.5,2.5,2.5])

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


st.subheader("Tentang lukisan landscape🏜️")
st.image("asset/landscape.png")
st.write("""Lukisan landscape adalah jenis lukisan yang menggambarkan pemandangan alam seperti gunung, sungai, dan lapangan dengan fokus utama pada elemen-elemen alam seperti langit, tanah, air, pepohonan, dan formasi geografis lainnya. Lukisan landscape sering kali menggambarkan keindahan alam dan mengekspresikan perasaan harmoni, kedamaian, keagungan, atau keindahan alam yang luas""")
st.write("Tujuan utama dari lukisan pemandangan adalah untuk merekam keindahan alam dan menciptakan pengalaman estetik yang membangkitkan perasaan damai, kekaguman, dan inspirasi pada penontonnya. Pelukis pemandangan mencoba menangkap keindahan alam dengan menggambarkan elemen-elemen seperti cahaya, warna, tekstur, dan komposisi secara detail dan realistis atau dalam gaya yang lebih ekspresif dan interpretatif")




















# import streamlit as st
# import tensorflow as tf
# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image
# import cv2
# from keras.models import load_model
# from keras_preprocessing.image import array_to_img

# landscape = load_model("C:/Users/User/Documents/deploy/landscape_final.h5")

# st.set_page_config(
#     page_title = "Lucky Eights | Art Generator")

# st.title("ART GENERATOR")

# # col1, col2 = st.columns([2,1])  # Memisahkan halaman menjadi dua kolom

# def demo(lukisan):
# 	wall = Image.open("C:/Users/User/Documents/deploy/wall.png")
# 	wall = wall.convert("RGB")

# 	frame = Image.open("a.png")
# 	frame = frame.resize((150,150))

# 	lukisan = lukisan.convert("RGBA")
# 	lukisan = lukisan.resize((132,132))

# 	frame.paste(lukisan,(10,10),lukisan)
# 	wall.paste(frame,(386,186))

# 	return st.image(wall)
		
# if st.button(label='Generate!'):
# 	noise = tf.random.normal([1, 100])
# 	output = landscape.predict(noise)
# 	img = (output * 127.5) + 127.5
# 	img = array_to_img(img[0])

# 	demo(img)
# 	# Menambahkan tombol download
#     # st.markdown(
#     #     f'<a href="data:image/png;base64,{img_to_base64(img)}" download="generated_image.png">Download Gambar</a>',
#     #     unsafe_allow_html=True
#     # )

# # st.download_button(
# # 		label="Download image",
# # 		data=output,
# # 		file_name="lukisan.png",
# # 		mime="image/png"
# # 	)

# 	# st.write ("")
	

	