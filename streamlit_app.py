import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image


favicon = Image.open('logo.jfif')
st.set_page_config(page_title='Calculadora de Taxa Metabólica',page_icon=favicon,layout="wide", initial_sidebar_state="collapsed")
st.title('Calculadora de Taxa Metabólica')

def calculo(sexo,peso,altura,idade,ativ):
    dict_ativ={'Sedentário – pouco ou nenhum exercício':1.2,
               'Pouco ativo – exercício/esporte leve 1-3 dias/semana':1.375,
               'Moderadamente ativo – exercício/esporte moderado 3-5 dias/semana':1.55,
               'Muito ativo – exercício/esporte pesado 6-7 dias/semana':1.725}

    if sexo == 'Masculino':
        TMB=66.4730 + (13.7516 * peso) + (5.0033 * altura*100) - (6.7550 * idade) 
    else:
        TMB= 655.0955 + (9.5634 * peso) + (1.8496 * altura*100) - (4.6756 * idade) 
    
    calculo_final=TMB*dict_ativ[ativ]
    return calculo_final
    

with st.form("my_form"):
    sexo=st.selectbox( 'Sexo:',('Masculino', 'Feminino'))
    peso = st.number_input('Insira seu peso (em kg):',min_value=0.0)
    altura = st.number_input('Insira sua altura (em metros):',min_value=0.0)
    idade = st.number_input('Insira sua idade (em anos):',min_value=0)
    ativ=st.selectbox( 'Como você se considera?',('Sedentário – pouco ou nenhum exercício', 'Pouco ativo – exercício/esporte leve 1-3 dias/semana','Moderadamente ativo – exercício/esporte moderado 3-5 dias/semana','Muito ativo – exercício/esporte pesado 6-7 dias/semana'))
    calcular=st.form_submit_button(label="Calcular Taxa Metabólica")

    if calcular:
        resultado=calculo(sexo,peso,altura,idade,ativ)
        st.write(f'O total de calorias gastas é: {resultado:.2f}')


hide_st_style="""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .css-1pmktlq{visibility: visible;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
