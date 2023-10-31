import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import base64
from PIL import ImageOps, Image


def application(image, model, labels):
    #image: Photo de l'oeil , model: Le modèle,
    
    #on mets l'image à la bonne taille
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    # transforme l'image en tableau numpy
    image_array = np.asarray(image)

    #adapte pour le moele
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # dataset
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    #  ml
    prediction = model.predict(data)
    index = 0 if prediction[0][0] > 0.95 else 1
    label = labels[index]
    score_result  = prediction[0][index]

    return label, score_result 


def fond_ecran(image_file): #image_file: le chemin d'acces de l'image.
       
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

# Main 
fond_ecran('./fondecran/fe.png') #fond d'écran
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
    labels = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

#affiche l'image chargé et si elle est malade ou pas 
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    label, conf_score = application(image, model, labels)

    # ecrit les résultats
    st.write("## {}".format(label))
    st.write("### score: {}%".format(int(conf_score * 1000) / 10))
    if label== "Healthy":
        emoji = "😄"
        st.title(f"{emoji}")
