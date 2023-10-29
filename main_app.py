#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 01:09:33 2023

@author: dastanyelubayev
"""
import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_excel('https://github.com/sc-katu/cropprotection/raw/main/ZIKR_vrediteli.xlsx')
data_gorhcak = pd.read_excel('https://github.com/sc-katu/cropprotection/raw/main/ZIKR_vrediteli.xlsx',sheet_name='Горчак')
data_mol = pd.read_excel('https://github.com/sc-katu/cropprotection/raw/main/ZIKR_vrediteli.xlsx',sheet_name='Капустная_моль')
data_pochvoobit = pd.read_excel('https://github.com/sc-katu/cropprotection/raw/main/ZIKR_vrediteli.xlsx',sheet_name='Почвообитающие')
st.set_page_config(page_title="Прогнозирование численности/развития вредных с/х организмов")
def main_page():     
    
    
    # Create a Streamlit app
    st.title("Прогнозирование. Септориоз")
    # Create a Markdown table
    markdown_table = """
    | Наименование предиктора                | Описание                                       |
    |-----------------------|----------------------------------------------------|
    | DegreeDays            | Общая накопленная теплота, Градусо-дни            |
    | Precipitation         | Общие накопленные осадки, Количество осадков мм                       |
    | Modelled Data         | Смоделированное значение развития септориоза       |
    | Field data            | Полевые значения развития септориоза               |
    | Уравнение регрессии   | Y= 117,27 + 0,1475*Precipitation-0,0934*DegreeDays            |
    """
    
    # Display the Markdown table
    st.markdown(markdown_table)
    
    # Create an animated 3D mesh plot using Plotly Express
    fig = px.scatter_3d(
        data,
        x='Градусо-дни',
        y='Количество осадков',
        z='Смоделированные значения',
        color='Имитационная модель',
        title='Развитие септориоза на основе модели регрессионного анализа',
        size_max=5,
    )
    
    # Customize the legend
    fig.update_traces(mode='markers', marker=dict(size=5), selector=dict(mode='markers'))
    
    # Display the animated 3D mesh plot
    st.plotly_chart(fig)
    
    intercept = 117.27
    coeff_precipitation = 0.1475
    coeff_degree_days = -0.0934
    
    # Create sliders for Precipitation and DegreeDays
    precipitation = st.slider(" Укажите количество предполагаемх осадков  на июль месяц Precipitation (mm)", min_value=0.0, max_value=80.0, step=5.0, value=10.0)
    degree_days = st.slider("Укажите предполагаемую общую накопленную влагу DegreeDays", min_value=1050.0, max_value=1300.0, step=10.0, value=1050.0)
    
    # Calculate Y based on the regression equation
    Y = intercept + coeff_precipitation * precipitation + coeff_degree_days * degree_days
    
    # Display the calculated Y
    st.write(f"Количественная модель септориоза = {intercept} + {coeff_precipitation} * {precipitation} + {coeff_degree_days} * {degree_days} = {Y:.2f}")
    predictions = coeff_degree_days * degree_days+coeff_precipitation*precipitation + intercept  #
    st.write("Исходные данные имитационного моделирования")
    st.write(data)  
# Define your second page content

def second_page():
    st.title("Прогнозирование. Горчак ползучий")
    # Create a Markdown table
    markdown_table = """
    | Наименование предиктора               | Описание                                        |
    |-----------------------|----------------------------------------------------|
    | DegreeDays            | Общая накопленная теплота, Градусо-дни            |
    | Precipitation10d         | Накопленные осадки за предшествующие 10 дней, мм                       |
    | Modelled Data         | Смоделированное значение развития горчака       |
    | Field data            | Полевые значения                |
    | Уравнение регрессии   | Y= -2,782 + 0,0021313*Precipitation-0,02886*DegreeDays            |
    """
    
    # Display the Markdown table
    st.markdown(markdown_table)
    
    # Create an animated 3D mesh plot using Plotly Express
    fig = px.scatter_3d(
        data_gorhcak,
        x='Градусо-дни',
        y='Количество осадков_10',
        z='Смоделированные значения',
        color='Имитационная модель',
        title='Развитие горчака на основе модели регрессионного анализа',
        size_max=5,
    )
    
    # Customize the legend
    fig.update_traces(mode='markers', marker=dict(size=5), selector=dict(mode='markers'))
    st.plotly_chart(fig)
    
    fig2 = px.scatter(data_gorhcak, x="Градусо-дни", y="Смоделированные значения", color="Имитационная модель", 
               title='Animated Line Chart with Legend',
              labels={"Градусо-дни": "X-axis", "Смоделированные значения": "Y-axis"}, size_max=5,
              template="plotly_dark", log_x=True)

# Show the plot in Streamlit
    st.plotly_chart(fig2)
    intercept = -2.782
    coeff_precipitation = -0.021313
    coeff_degree_days =  0.002886
    
    # Create sliders for Precipitation and DegreeDays
    precipitation = st.slider(" Укажите количество предполагаемх осадков за предшествующие 10 дней на июль месяц Precipitation (mm)", min_value=0.0, max_value=15.0, step=1.0, value=5.0)
    degree_days = st.slider("Укажите предполагаемую общую накопленную влагу DegreeDays", min_value=1400.0, max_value=1700.0, step=10.0, value=1450.0)
    
    # Calculate Y based on the regression equation
    Y = intercept + coeff_precipitation * precipitation + coeff_degree_days * degree_days
    
    # Display the calculated Y
    st.write(f"Модель развития горчака = {intercept} + {coeff_precipitation} * {precipitation} + {coeff_degree_days} * {degree_days} = {Y:.2f}")
    predictions = coeff_degree_days * data_gorhcak['Градусо-дни']+coeff_precipitation*data_gorhcak['Количество осадков_10'] + intercept  #
    st.write("Исходные данные имитационного моделирования")
    st.write(data_gorhcak)  





    
def third_page():
    st.title("Прогнозирование. Капустная моль")
    # Create a Markdown table
    markdown_table = """
    | Наименование предиктора               | Описание                                    |
    |-----------------------|----------------------------------------------------|
    | Precavr           | Среднемесячное значение осадков, мм           |
    | Tmax         | Максимальная суточная температура, С                      |
    | Modelled Data         | Смоделированное значение развития капустной моли       |
    | Field data            | Полевые значения развития капустной моли              |
    | Уравнение регрессии   | Y= 254 + 5,27*Precavr -3,027*Tmax          |
    """
    st.markdown(markdown_table)
    fig = px.scatter_3d(
        data_mol,
        x='Среднемесячное значение осадков_мм',
        y='Максимальная суточная температура',
        z='Смоделированные значения',
        color='Имитационная модель',
        title='Развитие капустной моли на основе модели регрессионного анализа',
        size_max=5,
    )
    
    # Customize the legend
    fig.update_traces(mode='markers', marker=dict(size=5), selector=dict(mode='markers'))
    st.plotly_chart(fig)
    intercept = 254
    coeff_prec = 5.27
    coeff_tmax =  -3.027
    x1_precavr = st.number_input('Введите предполагаемое среднемесячное значение осадков на июль месяц в мм', value=4)
    x2_tmax = st.number_input('Введите максимальное значение суточной температуры на июль месяц в С', value=10)
    Y = intercept + coeff_prec * x1_precavr + coeff_tmax * x2_tmax
    st.write(f"Модель развития капустной моли = {Y:.2f}")
def fourth_page():
    st.title("Прогнозирование. Почвообитающие вредители")
    # Create a Markdown table
    markdown_table = """
    | Наименование предиктора               | Описание                                    |
    |-----------------------|----------------------------------------------------|
    | DD30d          | Накопленная теплота за 30 дней, градусо-дни           |
    | Prec7d          | Накопленные осадки за предшествующие 7 дней, мм         |
    | Tavr30d       | Средняя температура за 30 дней, С                    |
    | Modelled Data         | Смоделированное значение развития почвообитающих       |
    | Field data            | Полевые значения развития почвообитающих              |
    | Уравнение регрессии   | Y= -13,5563 -0,4252*DD30D +0.2041*Prec7d +13.4265*Tavr30d          |
    """
    st.markdown(markdown_table)
    st.write("Исходные данные имитационного моделирования")
    st.write(data_pochvoobit)
    fig2 = px.scatter(data_pochvoobit, x="DD30d", y="Modelled data", color="Prec7d", 
               title='Модель почвообитающих',
              labels={"Накопленная теплота за 30 дней, градусо-дни": "X-axis", "Смоделированные значения": "Y-axis"}, size_max=5,
              template="plotly_dark", log_x=True)

# Show the plot in Streamlit
    st.plotly_chart(fig2)
    intercept = -13.56
    coeff_dd30 = -0.4252
    coeff_prec7d =  0.2041
    coeff_tavr= 13.4265
    x1_dd30d = st.number_input('Введите предполагаемое Накопленная теплота за 30 дней июль месяц', value=4)
    x2_prec7d = st.number_input('Введите Накопленные осадки за предшествующие 7 дней в мм', value=10)
    x3_tavr = st.number_input('редняя температура за 30 дней, С', value=10)
    Y = intercept + coeff_dd30 * x1_dd30d + coeff_prec7d * x2_prec7d+coeff_tavr*x3_tavr
    st.write(f"Модель развития почвообитающих = {Y:.2f}")
    
page = st.sidebar.selectbox("Вредители", ("Септориоз", "Горчак ползучий","Капустная моль", "Почвообитающие вредители (щелкуны, чернотелки)"))
content = st.container()
if page == "Септориоз":
    main_page()
elif page == "Горчак ползучий":
    second_page()
elif page == "Капустная моль":
    third_page()
elif page == "Почвообитающие вредители (щелкуны, чернотелки)":
    fourth_page()


    



