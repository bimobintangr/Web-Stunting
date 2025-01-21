import streamlit as st
import os


# Homepage
st.markdown(
    """
    <style>

        .header { text-align: center; 
        color: white; 
        background-color: #004d00; 
        padding: 50px 10px; 
        }

        .section-title { text-align: center; 
        margin-top: 50px; 
        font-size: 28px; 
        }

        .footer { text-align: center; 
        margin-top: 50px; 
        font-size: 14px; 
        color: white; 
        background-color: #004d00; 
        padding: 10px; 
        }

        .footer_1 { text-align: left; 
        margin-top: 50px; 
        font-size: 14px; 
        color: white; 
        background-color: #004d00; 
        padding: 10px; 
        }

    </style>
    """,
    unsafe_allow_html=True
)

#st.markdown('<div class="footer_1">NutriPlus</div>', unsafe_allow_html=True)

# Home Page

#def home_page():
# Header
st.markdown('<div class="header"><h1>NutriPlus</h1><p>Stunting adalah kondisi yang dapat dicegah dengan memberikan makanan bergizi sejak dini. Pastikan anak mendapatkan asupan lengkap seperti Protein, Zat Besi, Kalsium, Vit D, Vit C.</p><a href="#learn-more" style="color: white;"><button>Learn More</button></a></div>', unsafe_allow_html=True)

# Knowledge Section
st.markdown('<div id="learn-more" class="section-title"><h2>Tentang Stunting</h2></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; margin: 20px;">
        Stunting tidak hanya berdampak pada kesehatan fisik anak, tetapi juga berimplikasi pada produktivitas, kualitas hidup, serta kemajuan bangsa.<br><br>
        Berdasarkan data pada tahun 2016 sebanyak 22,9% (154,8 juta) anak di bawah usia 5 tahun menderita stunting dan Indonesia berada pada urutan ke-5 negara yang paling banyak menderita stunting. Penyebab utama terjadinya stunting adalah faktor gizi yang tidak seimbang baik kuantitas maupun kualitasnya selama masa hidup periode pertumbuhan. (Julius Anzar 2020)
    </div>
    """,
    unsafe_allow_html=True
)


# Meal Categories
st.markdown('<div class="section-title"><h2>Kategori Makanan Sesuai Umur</h2></div>', unsafe_allow_html=True)


# Fungsi untuk memuat gambar dengan proporsi asli
def load_image(image_file, caption):
    if os.path.exists(image_file):
        st.image(image_file, caption=caption, use_column_width=True)
    else:
        st.warning(f"Gambar tidak ditemukan: {image_file}")

# Folder gambar
image_folder = "images"




# Fungsi navigasi
def navigate(page):
    st.session_state.page = page

# Data kategori makanan
meal_categories = {
    "6 - 8 Months": [
        {"name": "Bubur Ayam Telur Puyuh", "kandungan": ["Energi: 150 kkal", "Protein: 8 gr", "Lemak: 3 gr", "Karbohidrat: 40 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Chicken Pumpkin Soup", "kandungan": ["Energi: 152 kkal", "Protein: 16 gr", "Lemak: 15 gr", "Karbohidrat: 250 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Bubur Kanji Rumbi Ayam dan Udang", "kandungan": ["Energi: 187 kkal", "Protein: 15 gr", "Lemak: 5 gr", "Karbohidrat: 5 gr"],"image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Pisang Cheese Cream", "kandungan": ["Energi: 50 kkal", "Protein: 6 gr", "Lemak:  15 gr", "Karbohidrat: 130 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Ubi Ungu Smash", "kandungan": ["Energi: 160 kkal", "Protein: 4 gr", "Lemak: 2 gr", "Karbohidrat: 45 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
    ],
    "9 - 11 Months": [
        {"name": "Nasi Tim Ikan Telur Sayur", "kandungan": ["Energi: 186.525 kkal", "Protein: 7.955 gr", "Lemak: 6.6 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Mie Kukus Telur Puyuh", "kandungan": ["Energi: 135 kkal", "Protein: 5.1 gr", "Lemak: 7.6 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Nasi Tim Ayam Lele Cincang", "kandungan": ["Energi: 125 kkal", "Protein: 4.5 gr", "Lemak: 4.9 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Agar-agar buah", "kandungan": ["Energi: 135 kkal", "Protein: 5.1 gr", "Lemak: 7.6 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Kue Bolu Jagung Manis", "kandungan": ["Energi: 125 kkal", "Protein: 4.5 gr", "Lemak: 4.9 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
    ],
    "12 - 23 Months": [
        {"name": "Nasi Sup Telur Puyuh Bola Tahu Ayam", "kandungan": ["Energi: 260 kkal", "Protein: 10. 4 gr", "Lemak: 10.7 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Nasi Soto Ayam Kuah Kuning", "kandungan": ["Energi: 263 kkal", "Protein: 9.5 gr", "Lemak: 10.9 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Nasi Sup Telur Puyuh Ikan Air Tawar Labu Kuning", "kandungan": ["Energi: 261 kkal", "Protein: 13.6 gr", "Lemak: 9.1 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Sempol Beger", "kandungan": ["Energi: 156.4 kkal", "Protein: 9 gr", "Lemak: 7.6 gr", "Karbohidrat: 12.4 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Bubur Kacang Hijau", "kandungan": ["Energi: 170 kkal", "Protein: 7 gr", "Lemak: 25 gr"],"image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
    ],
    "24 - 60 Months": [
        {"name": "Pepes Ikan Patin dan Sayuran", "kandungan": ["Energi: 180 kkal", "Protein: 15 gr", "Lemak: 8 gr", "Karbohidrat: 10 gr"],"image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Sup Kacang Polong dan Ayam", "kandungan": ["Energi: 180 kkal", "Protein: 14 gr", "Lemak: 6 gr", "Karbohidrat: 18 gr"],"image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Tumis Ayam Sayuran", "kandungan": ["Energi: 210 kkal", "Protein: 18 gr", "Lemak: 8 gr", "Karbohidrat: 10 gr"],"image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Bola-Bola Singkong Isi Telur Puyuh", "kandungan": ["Energi: 220 kkal", "Protein: 8 gr", "Lemak: 10 gr", "Karbohidrat: 25 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
        {"name": "Puding Ubi Ungu", "kandungan": ["Energi: 150 kkal", "Protein: 2 gr", "Lemak: 4 gr", "Karbohidrat: 430 gr"], "image": os.path.join(image_folder, "bubur_ayam_telur_puyuh.jpg"),},
    ],
}

# Halaman utama
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    
    # Tampilkan gambar kategori
    col1, col2, col3, col4 = st.columns(4)
    categories = list(meal_categories.keys())
    if col1.button(categories[0]):
        navigate(categories[0])
    if col2.button(categories[1]):
        navigate(categories[1])
    if col3.button(categories[2]):
        navigate(categories[2])
    if col4.button(categories[3]):
        navigate(categories[3])

# Halaman kategori makanan
else:
    category = st.session_state.page
    st.title(f"Makanan untuk Kategori Umur: {category}")
    
    for meal in meal_categories[category]:
        st.subheader(meal["name"])
        st.write("Nilai Gizi:")
        for ingredient in meal["kandungan"]:
            st.write(f"- {ingredient}")
    
    if st.button("Kembali ke Home"):
        navigate("home")

# Footer
st.markdown('<div class="footer">© 2024 NutriPlus<br>Terms of Service | Contact Us | Privacy Policy</div>', unsafe_allow_html=True)
