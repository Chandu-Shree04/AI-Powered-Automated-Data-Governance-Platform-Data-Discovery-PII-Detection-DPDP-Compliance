import matplotlib.pyplot as plt
import streamlit as st

def plot_histogram(df, column):

    fig, ax = plt.subplots()

    ax.hist(df[column])

    ax.set_title(f"{column} Distribution")

    st.pyplot(fig)