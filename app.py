import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/300408947/outputs/predictions.csv")

ticker= st.selectbox("Select Company",df["name"].unique())

data=df[df["name"]==ticker]

st.title("Stock Prediction Dashboard")

plt.plot(data["close"].values, label="Actual")
plt.plot(data["Prediction"].values, label="Predicted")
plt.legend()
st.pyplot(plt)