import streamlit as st
import random

# Title
st.title("Number Guessing Game -  by  Hamza Rehmani")

# Initialize session state for game variables
if 'number' not in st.session_state:
    st.session_state.number = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = 5  # Default max attempts
if 'min_range' not in st.session_state:
    st.session_state.min_range = 1
if 'max_range' not in st.session_state:
    st.session_state.max_range = 100

# Sidebar for custom range and difficulty
with st.sidebar:
    st.subheader("Game Settings")
    min_range = st.number_input("Minimum Range", value=1, step=1)
    max_range = st.number_input("Maximum Range", value=100, step=1)
    difficulty = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"])
    if st.button("Update Settings"):
        st.session_state.min_range = min_range
        st.session_state.max_range = max_range
        if difficulty == "Easy":
            st.session_state.max_attempts = 10
        elif difficulty == "Medium":
            st.session_state.max_attempts = 5
        elif difficulty == "Hard":
            st.session_state.max_attempts = 3
        st.session_state.attempts = 0
        st.session_state.number = random.randint(st.session_state.min_range, st.session_state.max_range)
        st.success("Settings updated! New game started.")

# Start or reset game
if st.button("Start/Reset Game"):
    st.session_state.number = random.randint(st.session_state.min_range, st.session_state.max_range)
    st.session_state.attempts = 0
    st.success("New game started! Guess a number between {} and {}.".format(st.session_state.min_range, st.session_state.max_range))

# User input for guess
if st.session_state.number is not None:
    st.subheader("Make Your Guess")
    guess = st.number_input("Enter your guess:", min_value=st.session_state.min_range, max_value=st.session_state.max_range, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == st.session_state.number:
            st.success(f"Congratulations! You guessed the number {st.session_state.number} in {st.session_state.attempts} attempts!")
            st.session_state.number = None
        elif guess < st.session_state.number:
            st.write("Too low! Try a higher number.")
            if st.session_state.attempts >= st.session_state.max_attempts:
                st.error(f"Game Over! The number was {st.session_state.number}. Attempts exceeded.")
                st.session_state.number = None
        else:
            st.write("Too high! Try a lower number.")
            if st.session_state.attempts >= st.session_state.max_attempts:
                st.error(f"Game Over! The number was {st.session_state.number}. Attempts exceeded.")
                st.session_state.number = None

    # Display attempts
    st.write(f"Attempts: {st.session_state.attempts} / {st.session_state.max_attempts}")

# Footer
st.write("Developed for Hamza Rehmani - March 2025")