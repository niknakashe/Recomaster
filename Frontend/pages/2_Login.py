import streamlit as st
import mysql.connector
import hashlib
import os

# Load environment variables
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
ssl_ca = './Frontend/ca_certificate.pem'

print(host, port, user, password, database)

# Function to connect to the MySQL database
def init_db_connection():
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        ssl_ca=ssl_ca           
    )
    return connection


# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to validate user login and get user data
def login_user(username, password):
    conn = init_db_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute('''
        SELECT id FROM users WHERE username = %s AND password = %s
    ''', (username, hashed_password))
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return data  # Return the fetched data (None if not found)

# Streamlit UI for Log In
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Log In")

    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")

    if st.button("Log In"):
        if username and password:
            user_data = login_user(username, password)
            if user_data:
                st.session_state.logged_in = True
                st.session_state['id'] = user_data[0]  # Store user ID in session state
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
