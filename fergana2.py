import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

st.subheader('Daromad xavfini prognoz qilish tizimi')

pickle_in = open("Home_price.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_note_authentication(plant_type, Organic_matter, Salt_content,
                                Climatic_conditions, Elevation_level_above_sea_level,
                                Temperature):
    prediction = classifier.predict([[plant_type, Organic_matter, Salt_content,
                                      Climatic_conditions, Elevation_level_above_sea_level,
                                      Temperature]])
    print(prediction)
    return prediction

def main():
    st.title("Daromad xavfini prognoz qilish tizimi")
    
    
    pl_type = st.radio('Sizda qanday o\'simlik bor?', ('sabzi', 'kartoshka'))
if pl_type == 'sabzi':
    plant_type = 0
else:
    plant_type = 1
Organic_matter = st.number_input('sizning organik moddalar indeksingiz qanday?(faqat raqamlarni kiriting 0.5 - 5.0)', step=0.1, value=0.0)
Salt_content = st.number_input('sizning tuzingiz qanday?(faqat raqamlarni kiriting 0.0 - 2.0)', step=0.1, value=0.0)
climatic_cond = st.radio('sizda qanday o simlik bor?', ('тропический', 'субтропический', 'северный'))
if climatic_cond=='тропический':
    Climatic_conditions=0
else:
    Climatic_conditions=1
else:
    Climatic_conditions=2                             
Elevation_level_above_sea_level = st.number_input('dengiz sathidagi balandligingiz?(faqat raqamlarni kiriting 1000 - 8000)', step=1, value=0)
Temperature = st.number_input('harorat ko rsatkichi)(faqat raqamlarni kiriting 15-35)', step=1, value=0)

    result = ""
    if st.button("Bashorat qilish"):
        result = int(predict_note_authentication(plant_type, Organic_matter, Salt_content,
                                                Climatic_conditions, Elevation_level_above_sea_level,
                                                Temperature))
        if result == 0:
            st.success('Ajoyib yangilik, siz bu hosilni ekishingiz mumkin')
        else:
            st.success('Yomon xabar, siz siz bu hosilni ekolmaysiz')

if __name__ == '__main__':
    main()