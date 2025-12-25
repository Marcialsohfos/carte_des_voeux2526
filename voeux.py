import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# --- CONFIGURATION ---
st.set_page_config(page_title="Meilleurs Voeux 2026", page_icon="🎄", layout="centered")

# Fonction pour charger les animations Lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# CSS pour le style (Carte dorée et fond festif)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        background-image: radial-gradient(#1c2331 15%, transparent 16%), radial-gradient(#1c2331 15%, transparent 16%);
        background-size: 60px 60px;
        background-position: 0 0, 30px 30px;
    }
    .message-box {
        padding: 30px;
        border-radius: 15px;
        background: linear-gradient(135deg, #fff 0%, #f8f9fa 100%);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        text-align: center;
        border: 4px solid #d4af37; /* Bordure Or */
        color: #2c3e50;
    }
    .highlight {
        color: #d35400;
        font-weight: bold;
        font-size: 1.3em;
    }
    .footer {
        margin-top: 40px;
        color: #bdc3c7;
        font-size: 0.8em;
        text-align: center;
        font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# Chargement d'une animation Lottie (Exemple: Feux d'artifice festifs)
# Vous pouvez en trouver d'autres sur lottiefiles.com
lottie_new_year = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_2302wki8.json")

# --- INTERFACE ---

st.title("🎁 Une surprise vous attend...")

if 'valid' not in st.session_state:
    st.session_state.valid = False

# Champ de saisie
nom = st.text_input("Entrez votre nom pour déverrouiller le message :", placeholder="Votre nom ici...")

if nom:
    # 1. Effet immédiat : La Neige (Ambiance Noël)
    st.snow()
    
    # Petit temps d'attente pour la mise en scène
    with st.spinner('Génération de la magie en cours...'):
        time.sleep(1.5)

    # 2. Effet Pluie d'Emojis (Cadeaux et Sapins)
    rain(
        emoji="🎄",
        font_size=30,
        falling_speed=4,
        animation_length=3, # Dure 3 secondes
    )

    st.markdown("---")
    
    # Affichage de l'animation Lottie au centre
    if lottie_new_year:
        st_lottie(lottie_new_year, height=200, key="fireworks")

    # Le Message Personnalisé
    st.markdown(f"""
    <div class="message-box">
        <h1 style='color:#c0392b; font-family: "Arial Black", sans-serif;'>✨ JOYEUX NOËL & 2026 ✨</h1>
        <br>
        <p style='font-size:1.3em; line-height:1.6;'>
            <span class="highlight">{nom}</span>, je te souhaite un joyeux Noël et mes vœux les meilleurs pour le nouvel an.
            <br><br>
            Puisse le <b>SEIGNEUR</b> vous fortifier et vous garder.
            <br>
            Que du bonheur au centuple pour le nouvel an.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 3. Effet Final : Les Ballons (Célébration)
    time.sleep(0.5)
    st.balloons()

    # Footer Signature
    st.markdown("""
    <div class="footer">
        Ce message vous a été envoyé avec le concours de<br>
        RMT, Lab_Math & CIE et <b>SCSM SARL</b>
    </div>
    """, unsafe_allow_html=True)

    # Bouton pour relancer (si on veut montrer à quelqu'un d'autre)
    if st.button("Recommencer la magie 🔄"):
        st.experimental_rerun()

else:
    st.info("👋 Écrivez votre nom ci-dessus et validez avec 'Entrée'.")