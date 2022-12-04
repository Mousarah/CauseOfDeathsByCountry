# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:57:23 2022

@author: mousarah
"""

import pandas as pd
import streamlit as st
import plotly.express as px

dados = pd.read_csv('cause_of_deaths.csv', encoding='latin-1')
paises = list(dados['País/Território'].unique())
pais = st.selectbox('Selecione o país', ['Todos'] + paises)

if (pais != 'Todos'):
    dados = dados[dados['País/Território'] == pais]
    
dshow = dados.groupby(by = ['Ano']).sum()    
causasMortes = dados.columns.tolist()[2:]

fig = px.line(dshow, x = dshow.index, y = causasMortes, markers=True)
fig.update_layout(title='Causas de morte por ano',
                  xaxis_title='Ano',
                  yaxis_title='Mortes',
                  legend_title_text = 'Causas')

st.plotly_chart(fig, use_container_width=True)