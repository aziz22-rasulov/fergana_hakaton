import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

st.subheader('Daromad xavfini prognoz qilish tizimi')

model_selected = st.radio('Qanday tahlildan foydalanmoqchisiz?', ('LogisticRegression', 'RandomForestClassifier', 'CatBoostClassifier', 'AdaBoostClassifier', 'Default'))

if model_selected == 'LogisticRegression':
    pickle_in = open("risk_of_plant_LogReg.pkl", "rb")
    classifier = pickle.load(pickle_in)
elif model_selected == 'RandomForestClassifier':
    pickle_in = open("risk_of_plant_RandomForest.pkl", "rb")
    classifier = pickle.load(pickle_in)
elif model_selected == 'CatBoostClassifier':
    pickle_in = open("risk_of_plant_Catboost.pkl", "rb")
    classifier = pickle.load(pickle_in)
elif model_selected == 'AdaBoostClassifier':
    pickle_in = open("risk_of_plant_Adaboost.pkl", "rb")
    classifier = pickle.load(pickle_in)

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
    plant_type = st.radio('Ekmoqchi bolgan sabzavotingizni tanlang?', (sabzi, kartoshka))
    Organic_matter = st.number_input('organik moddalaringiz?(faqat raqamlarni kiriting 0.5 - 5.0)', step=0.1, value=0.0)
    Salt_content = st.number_input('tuzingiz miqdori?(faqat raqamlarni kiriting 0.0 - 2.0)', step=0.1, value=0.0)
    Climatic_conditions = st.radio('iqlim sharoitingiz?(0 - тропический , 1 - субтропический, 2 - северный)', (тропический, субтропический, северный))
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