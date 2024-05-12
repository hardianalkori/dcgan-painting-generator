import streamlit as st
from PIL import Image
st.set_page_config(
    	page_title = "Lucky Eights | Tentang", layout="wide", page_icon="asset/LE.ico")
logo_image = Image.open('asset/LE.png')
st.sidebar.image(logo_image, use_column_width=True)
st.markdown('<div style="font-family:Poppins; text-align: center; font-size:50px">We Are Lucky Eights</div>', unsafe_allow_html=True)

kiri, tengah, kanan = st.columns([1,1,1])



with kiri:
	st.markdown('<div class="column-border"></div>', unsafe_allow_html=True)
	st.image("asset/putri.png", use_column_width=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Putri Regita Saptaningtias</div>', unsafe_allow_html=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Universitas Jember</div>', unsafe_allow_html=True)

	st.markdown('<div class="column-border"></div>', unsafe_allow_html=True)
	st.image("asset/sahrul.png", use_column_width=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Sahrul Apriliansah</div>', unsafe_allow_html=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Universitas Siliwangi</div>', unsafe_allow_html=True)

with tengah:
	st.markdown('<div class="column-border"></div>', unsafe_allow_html=True)
	st.image("asset/lulu.png", use_column_width=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Lulu Anna Fajriandari</div>', unsafe_allow_html=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Universitas Gadjah Mada</div>', unsafe_allow_html=True)

	st.markdown('<div class="column-border"></div>', unsafe_allow_html=True)
	st.image("asset/firda.png", use_column_width=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Firda Kamal</div>', unsafe_allow_html=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Institut Teknologi Telkom Purwokerto</div>', unsafe_allow_html=True)

with kanan:
	st.markdown('<div class="column-border"></div>', unsafe_allow_html=True)
	st.image("asset/devi.png", use_column_width=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Puspadevi Anggotra</div>', unsafe_allow_html=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Universitas Udayana</div>', unsafe_allow_html=True)


	st.markdown('<div class="column-border"></div>', unsafe_allow_html=True)
	st.image("asset/hardian.png", use_column_width=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Hardian Alkori</div>', unsafe_allow_html=True)
	st.markdown('<div style="font-family:Poppins; text-align: center;">Institut Teknologi Telkom Purwokerto</div>', unsafe_allow_html=True)

with tengah:
	st.markdown("<br>", unsafe_allow_html=True)
	st.markdown("<br>", unsafe_allow_html=True)
	st.markdown('<div style="font-family:Poppins; text-align: left; font-size:50px">Startup Campus</div>', unsafe_allow_html=True)
	st.markdown("<br>", unsafe_allow_html=True)
	st.image("asset/sc.png", use_column_width=True)
	st.markdown("<br>", unsafe_allow_html=True)
	st.markdown("<br>", unsafe_allow_html=True)

st.write("""Startup Campus adalah bootcamp persiapan kerja terbaik dalam bidang digital dan teknologi. Terpilih sebagai "One Of The Most Innovative Edtechs in Asia Pasific" menurut penilaian AWS EdTech di 2022, Startup Campus juga berhasil menjadi tempat belajar bagi lebih dari 1.500 peserta di tahun yang sama. Di tahun 2023, Startup Campus kembali dengan kemitraan bersama Google Career Indonesia serta Kampus Merdeka. Startup Campus berhasil menjadi salah satu mitra terbaik dalam program Studi Independen Kampus Merdeka.""")

st.markdown('<div style="font-family:Poppins; text-align: center; font-size:50px">Kampus Merdeka</div>', unsafe_allow_html=True)
k,t,ka = st.columns([1,1,1])
with t:
	st.markdown("<br>", unsafe_allow_html=True)
	st.markdown("<br>", unsafe_allow_html=True)
	st.image("asset/km.png", use_column_width=True)
	st.markdown("<br>", unsafe_allow_html=True)
	st.markdown("<br>", unsafe_allow_html=True)

st.write("Kampus Merdeka adalah kebijakan yang dikeluarkan oleh Kemendikbudristek dengan memberikan hak kepada Mahasiswa untuk mengambil mata kuliah di luar program studi selama 1 semester dan berkegiatan di luar perguruan tinggi selama 2 semester. Perguruan tinggi diberikan kebebasan untuk menyediakan kegiatan Kampus Merdeka yang sesuai dengan kebutuhan dan minat mahasiswanya.")
