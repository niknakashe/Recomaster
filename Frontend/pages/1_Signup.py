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

# Function to connect to the MySQL database
def init_db_connection():
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    return connection

# Function to create the table if it doesn't exist
def create_table():
    conn = init_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if a user already exists
def user_exists(username):
    conn = init_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return data is not None

# Function to add a new user
def add_user(username, email, password):
    conn = init_db_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute('''
        INSERT INTO users (username, email, password) 
        VALUES (%s, %s, %s)
    ''', (username, email, hashed_password))
    conn.commit()
    cursor.close()
    conn.close()

# Create the table if not exists
create_table()

# Streamlit UI for Sign Up
st.title("Sign Up")

username = st.text_input("Enter your username")
email = st.text_input("Enter your email")
password = st.text_input("Enter your password", type="password")

if st.button("Sign Up"):
    if username and email and password:
        if not user_exists(username):
            add_user(username, email, password)
            st.success("Sign up successful! You can now log in.")
        else:
            st.error("Username already exists.")
    else:
        st.error("Please fill in all fields.")

# Link to the login page
st.write("Already have an account? [Log In here](../Login)")
