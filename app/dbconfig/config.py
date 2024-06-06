# Import the Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize the Firebase Admin SDK
# Make sure to download the Service Account JSON file from Firebase Console
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

# Your Firebase project configuration
firebaseConfig = {
  "apiKey": "AIzaSyBs0fs5pqOYX4utw90_ljBmFczH7SupqqA",
  "authDomain": "scrape-it-e224d.firebaseapp.com",
  "projectId": "scrape-it-e224d",
  "storageBucket": "scrape-it-e224d.appspot.com",
  "messagingSenderId": "567538365439",
  "appId": "1:567538365439:web:8723a42902fcbe9e9c2dca",
  "measurementId": "G-1PJ4Y7M9SZ"
}

# Initialize Firebase (this step is optional in Firebase Admin SDK)
app = firebase_admin.initialize_app()

# In Firebase Admin SDK, there is no separate method for Analytics like in Firebase Web SDK
# You can interact with other Firebase services directly as needed

# Example of accessing Firestore:
# ref = db.collection('users').document('alovelace')
# doc = ref.get()
# if doc.exists:
#     print(f'Document data: {doc.to_dict()}')
# else:
#     print('No such document!')

# Note: Unlike the Firebase JavaScript SDK, the Firebase Admin SDK does not have a separate method for Analytics.
# You would interact with other Firebase services like Firestore directly as shown above.
