import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

st.title("Simple Streamlit App with Firebase")

# Form to add data to Firestore
form = st.form(key='my-form')
name = form.text_input('Enter your name:')
submit = form.form_submit_button('Submit')

if submit:
    doc_ref = db.collection('users').document(name)
    doc_ref.set({
        'name': name
    })
    st.write(f"Data for {name} added to Firestore!")

# Display all users
st.write("Users in Firestore:")
users_ref = db.collection('users')
users = users_ref.stream()
for user in users:
    st.write(f"- {user.id}: {user.to_dict()}")
