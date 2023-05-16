import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.title("Map")
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, - 122.4],columns=['lat','lon'])
st.map(df)
