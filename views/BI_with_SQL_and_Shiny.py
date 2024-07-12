import streamlit as st
from utils import *
#from streamlit_player import st_player

#  Afficher l'image de la formation
img_formation1 = "assets/formation1.png"
st.image(str(img_formation1), width = 1400)

st.write(" ")

# Afficher la vidéo de présentation de la formation
#html_video = '''<iframe width="560" height="315" src="https://www.youtube.com/embed/SpXPIb6Jkfo?si=u9tajJf7jeHJVj6m" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'''
# Affichage de la vidéo
#st_player(html_video)

st.write(" ")

# Ajouter un bouton pour télécharger le programme au format PDF
pdf_link = "https://drive.google.com/file/d/1RgIwSptlp0iiwhmALUis3_PupNPmKOBt/view?usp=sharing"
if st.button('Téléchargez le Programme de Formation en PDF'):
    st.markdown(f'<a href="{pdf_link}" download>Cliquez ici pour télécharger le Programme de la Formation</a>', unsafe_allow_html=True)

st.write(" ")

# Registration Form
st.subheader("Inscription à la formation")
registration_link = "https://forms.gle/oZsH5Er8923jHShWA"
if st.button("S'inscrire", key='inscription'):
    new_tab = f'<a href="{registration_link}" target="_blank">Cliquez ici pour vous inscrire à la Formation</a>'
    st.markdown(new_tab, unsafe_allow_html=True)


st.write(" ")

# Payment Button
st.subheader("Paiement des Frais de Formation")
payment_link = "https://buy.stripe.com/fZeaIGaVw4EG80w28u"
if st.button("Payez", key='payment'):
    new_tab = f'<a href="{payment_link}" target="_blank">Cliquez ici pour payer votre participation</a>'
    st.markdown(new_tab, unsafe_allow_html=True)

# Afficher le contenu de la formation
programme_formation1 = read_description("assets/formation1.md")
st.markdown(programme_formation1)


