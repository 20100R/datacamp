import streamlit as st
from tensorflow.keras.models import load_model

from PIL import Image
import numpy as np

from util import classify, set_background


set_background('./fondecran/fe.png')

# set title
st.title('Disease detection')

st.header('Please upload an image of your eyes')

set_background('./fondecran/fe.png')
# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('./model/detectmaladie.h5')

# load class names
with open('./model/labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write("## {}".format(class_name))
    st.write("### score: {}%".format(int(conf_score * 1000) / 10))
