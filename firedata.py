from firebase import Firebase

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = Firebase(config)

storage = firebase.storage()

# as admin
storage.child("images/example.jpg").put("example2.jpg")

# as user
storage.child("images/example.jpg").put("example2.jpg", user['idToken'])

storage.child("images/example.jpg").download("downloaded.jpg")

storage.child("images/example.jpg").get_url()

#download
storage.child("images/example.jpg").get_url()

#get url
storage.child("images/example.jpg").get_url()

