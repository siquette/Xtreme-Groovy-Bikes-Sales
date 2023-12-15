import pandas as pd
import numpy as np
import streamlit as st
from scr.extraction import load_data

st.set_page_config(layout-'wide')

def load_data():
    return pd.read_csv('/home/siquette/ds/git/Xtreme-Groovy-Bikes-Sales/data/processed/bikes_completed.csv')

def main(): 
    df = load_data()
    
    st.dataframe(df)
    
if __name__ --'__main__':
    main()