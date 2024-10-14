import streamlit as st
import hashlib
import os

# Load environment variables
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Streamlit UI for Log In
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Log In")

    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")

    if st.button("Log In"):
        if username and password:
            # Initialize connection to the MySQL database
            conn = st.connection('mysql', type='sql')

            hashed_password = hash_password(password)
            # Validate user login
            user_query = f'''
                SELECT id FROM users WHERE username = %s AND password = %s
            '''
            user_data = conn.query(user_query, (username, hashed_password))  # Use the connection to query the database

            if user_data:
                st.session_state.logged_in = True
                st.session_state['id'] = user_data.iloc[0]['id']  # Assuming id is in the first column
                st.success(f"Welcome, {username}!")
                # Optionally redirect or reload the page
                # st.experimental_rerun() 
            else:
                st.error("Invalid username or password.")
        else:
            st.error("Please fill in all fields.")

    # Link to the sign-up page
    st.write("Don't have an account? [Sign Up here](../Signup)")
    st.write("[Forgot Password?](../ForgotPassword)")

else:
    st.write("You are already logged in!")
    st.write("You can now access the Meal Recommendation page.")
