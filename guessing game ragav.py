import streamlit as st
import random

if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0

st.title("Number Guessing Game")
guess = st.number_input("Guess a number between 1 and 100", 1, 100)

if st.button("Submit"):
    st.session_state.attempts += 1
    if guess < st.session_state.target:
        st.write("Too low!")
    elif guess > st.session_state.target:
        st.write("Too high!")
    else:
        st.write(f"Correct! {st.session_state.attempts} attempts.")
        if st.button("Play Again"):
            st.session_state.target = random.randint(1, 100)
            st.session_state.atte
