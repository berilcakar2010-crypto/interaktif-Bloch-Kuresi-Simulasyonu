import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector

# Sayfa Ayarları
st.set_page_config(page_title="Kuantum Bloch Simülasyonu", layout="centered")

# Arayüz (CSS)
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stSlider { color: #00FF00; }
    div[data-testid="stMarkdownContainer"] { color: #00FF00; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00FF00; text-shadow: 0 0 10px #00FF00;'>🌐 BLOCH KÜRESİ ANALİZİ</h1>", unsafe_allow_html=True)

# Kontrol Paneli (Sliderlar)
col1, col2 = st.columns(2)
with col1:
    theta = st.slider('[ANGLE_Θ] (Eğim)', 0.0, float(np.pi), 0.0, step=0.01)
with col2:
    phi = st.slider('[PHASE_Φ] (Faz)', 0.0, float(2*np.pi), 0.0, step=0.01)

# Kuantum Hesaplama
initial_state = Statevector([1, 0])
c0 = np.cos(theta/2)
c1 = np.exp(1j*phi) * np.sin(theta/2)
user_state = Statevector([c0, c1])

# Bloch Küresi Çizimi
fig = plot_bloch_multivector([initial_state, user_state])
fig.patch.set_facecolor('black')
st.pyplot(fig)

# Bilgi Panelleri
st.markdown(f"""
<div style="border: 2px solid #00FF00; padding: 15px; border-radius: 10px;">
    <p><b>[SYSTEM_STATUS]:</b> Aktif</p>
    <p><b>[COORDINATES]:</b> θ: {theta:.4f} | φ: {phi:.4f}</p>
    <hr style="border: 0.5px solid #00FF00;">
    <p style="color: #FF0000;">● Kırmızı Ok: Temel Durum (|0⟩)</p>
    <p style="color: #00FF00;">● Yeşil/Mavi Ok: Senin Durumun</p>
</div>
""", unsafe_allow_html=True)

st.write("---")
st.markdown("** GÖZLEMCİ NOTU:** Vektör ekvator düzlemine yaklaştıkça sistem **Süperpozisyon** evresine girer.")
