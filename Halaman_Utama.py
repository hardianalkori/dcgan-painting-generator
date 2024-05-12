
import streamlit as st
from PIL import Image
st.set_page_config(
    page_title = "Lucky Eights | Art Generator",page_icon = "asset/LE.png")

logo_image = Image.open('asset/LE.png')
st.sidebar.image(logo_image, use_column_width=True)

st.markdown("<h1 style='font-size: 36px;'>  Lucky Eights | Painting Generator   </h1>", unsafe_allow_html=True)
st.write("Dengan menggabungkan dua hal berbeda yaitu seni dan ilmu pengetahuan, kami membuat sebuah model kecerdasan buatan yang dapat menghasilkan sebuah lukisan dalam berbagai tema.")
st.header("Lukisan apa saja yang bisa digenerate?")
st.subheader("Abstrak")
st.image("asset/abstrak.jpg", use_column_width = True)
st.write("Lukisan abstrak adalah gaya seni yang tidak mewakili penggambaran realitas visual yang akurat. Alih-alih, lukisan ini berfokus pada pengungkapan ide, emosi, atau konsep melalui penggunaan warna, bentuk, garis, dan tekstur. Dalam lukisan abstrak, penekanannya adalah pada interpretasi subyektif seniman daripada representasi langsung dari objek atau pemandangan yang dapat dikenali.")
st.subheader("Landscape")
st.image("asset/landscape.png")
st.write("Lukisan landscape adalah genre seni yang berfokus pada penggambaran pemandangan alam, seperti pegunungan, lembah, sungai, hutan, atau elemen lingkungan alam lainnya. Lukisan ini menampilkan keindahan, atmosfer, dan esensi dunia luar. Tujuan dibuatnya lukisan landscape adalah untuk menyampaikan pengalaman visual dan emosional saat berada di lokasi tertentu atau menangkap keseluruhan suasana landscape.")
st.subheader("Portrait")
st.image("asset/portrait.png")
st.write("Lukisan portrait adalah bentuk seni di mana seorang seniman menciptakan representasi visual dalam bentuk lukisan dari seseorang. Fokus utama dari lukisan portrait adalah menangkap kemiripan, kepribadian, dan karakteristik unik dari subjek yang digambarkan. Singkatnya, lukisan portrait adalah bentuk seni menawan yang memungkinkan seniman menjelajahi kompleksitas identitas manusia dan menciptakan representasi visual individu yang indah.")
