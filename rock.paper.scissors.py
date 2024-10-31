import streamlit as st
import random

# Set the title
st.title("Rock, Paper, Scissors Game")

# Define the choices
choices = ["Rock", "Paper", "Scissors"]

# User selection
user_choice = st.selectbox("Choose Rock, Paper, or Scissors:", choices)

# Button to play
if st.button("Play"):
    # Computer choice
    computer_choice = random.choice(choices)
    
    # Display the choices
    st.write(f"You chose: {user_choice}")
    st.write(f"The computer chose: {computer_choice}")

    # Determine the result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    # Display the result
    st.write(result)
