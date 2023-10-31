import streamlit as st
from tensorflow.keras.models import load_model

from PIL import Image
import numpy as np

from util import classify, set_background


set_background('./fondecran/fe.png') #fond d'écran
st.title('Eagle Eye 🦅')
st.write("")
st.title('Disease detection')
st.header('Please upload an image of your eyes')   #display texte

# charge l'image
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# charge le modele
model = load_model('./model/detectmaladie.h5')

# charge le nom des deux classes
with open('./model/labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

#affiche l'image chargé et si elle est malade ou pas 
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write("## {}".format(class_name))
    st.write("### score: {}%".format(int(conf_score * 1000) / 10))
    if class_name== "Normale":
        emoji = "😄"
        st.write(f"{emoji}")
