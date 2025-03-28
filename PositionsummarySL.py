# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 06:12:53 2020

@author: Administrator
"""


import streamlit as st
import numpy as np
import pandas as pd
import datetime

st. cache_data. clear()
st.title('Position Size BankNifty')
#st.write("Here's my first attempt at writing some text")

path_string_1='./'

file_string_1=path_string_1+'strategyposition.csv'
df_position=pd.read_csv(file_string_1)
file_string_2=path_string_1+'strategypositionmc.csv'
df_position_mc=pd.read_csv(file_string_2)
file_string_3=path_string_1+'positionsummary.csv'
#print(df_position_mc.head())
file_string_4=path_string_1+'strategy.csv'
file_string_5=path_string_1+'current_time.csv'
df_current_time=pd.read_csv(file_string_5)
df_strategy=pd.read_csv(file_string_4)
df_position=pd.merge(df_position,df_strategy,on='Strategy')
df_position_mc=pd.merge(df_position_mc,df_strategy,on='Strategy')
cols=cols=['ID','Strategy', 'Position', 'Trade Price', 'Trade Time', 'Eval Time', 'Status']
df_position=df_position[cols]
df_position_mc=df_position_mc[cols]
df_position=df_position.sort_values('ID')
df_position_mc=df_position_mc.sort_values('ID')

total_position=df_position['Position'].sum()
total_position_mc=df_position_mc['Position'].sum()
add_selectbox = st.sidebar.selectbox(
    'Position in Account?',
    ('HUF', 'Samrup', 'Star','Galaxy','Neptune','SMS','RSS','Total')
)
if add_selectbox=='HUF':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[-1]== 'H']
    df_filter_mc=df_position_mc[df_position_mc['Strategy'].str[-1]=='H']
elif add_selectbox=='Samrup':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[-1]== 'S']
    df_filter_mc=df_position_mc[(df_position_mc['Strategy'].str[-1]== 'S') & (df_position_mc['Strategy'].str[-2:-1]!='R')]
    df_filter_mc=df_filter_mc[df_filter_mc['Strategy'].str[-2:-1]!='S']
elif add_selectbox=='Star':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[-1]== 'M']
    df_filter_mc=df_position_mc[df_position_mc['Strategy'].str[-1]== 'M']
elif add_selectbox=='Galaxy':
    st.write(add_selectbox)
    df_filter=df_position[(df_position['Strategy'].str[-1]== 'G') & (df_position['Strategy'].str[0]=='N')]
    df_filter_mc=df_position_mc[df_position_mc['Strategy'].str[-1]== 'G']
elif add_selectbox=='Neptune':
    st.write(add_selectbox)
    df_filter=df_position[(df_position['Strategy'].str[0]== 'N') & (df_position['Strategy'].str[-1]=='N')]
    df_filter_mc=df_position_mc[df_position_mc['Strategy'].str[-1]== 'N']
elif add_selectbox=='SMS':
    st.write(add_selectbox)
    df_filter=df_position[(df_position['Strategy'].str[0:2]== 'P5') & (df_position['Strategy'].str[-1]=='G')]
    df_filter_mc=df_position_mc[df_position_mc['Strategy'].str[-2:]== 'SS']
elif add_selectbox=='RSS':
    st.write(add_selectbox)
    df_filter=df_position[(df_position['Strategy'].str[0:2]== 'P5') & (df_position['Strategy'].str[-1]=='N')]
    df_filter_mc=df_position_mc[df_position_mc['Strategy'].str[-2:]== 'RS']
elif add_selectbox=='Total':
    df_filter=df_position.copy()
    df_filter_mc=df_position_mc.copy()
position_account=df_filter['Position'].sum()
position_account_mc=df_filter_mc['Position'].sum()
st.write('Total Bank Nifty Position Size is '+str(position_account))
st.write('Total Midcap Nifty Position Size is '+str(position_account_mc))
st.write(df_filter)
st.write(df_filter_mc)
df_position_summary=pd.read_csv(file_string_3)
total_m2m=df_position_summary['M2M'].sum()
total_margin_available=df_position_summary['Margin Available'].sum()
total_bn_futures=df_position_summary['BN Futures'].sum()
total_mc_futures=df_position_summary['MC Futures'].sum()
st.write(df_position_summary)
st.write('Total M2M for day: '+str(total_m2m))
st.write('Total Margin Available: '+str(total_margin_available))
st.write('Actual BN Futures: '+str(total_bn_futures))
st.write('Actual MC Futures: '+str(total_mc_futures))
st.write('Time Updated Till: '+str(df_current_time['Time'].iloc[0]))

# st.write('Theoretical BN Position(Total): '+str(total_position))
# st.write('Theoretical MC Position(Total): '+str(total_position_mc))
