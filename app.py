import streamlit as st
import pandas as pd
import random

st.title("🎮 League of Legends Party Tools")
st.subheader("🕵️‍♂️ Spy Drawer")

st.markdown("Upload a CSV file with player names, and a spy will be randomly assigned.")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    players = df['player_name'].tolist()

    if st.button("🎲 Draw Spy"):
        spy = random.choice(players)
        st.markdown("## ✅ Spy Assigned:")
        st.markdown(f"### 🕵️‍♂️ **{spy}**")
