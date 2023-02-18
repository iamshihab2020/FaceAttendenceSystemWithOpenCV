import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")

# database reference URL
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendence-536e4-default-rtdb.firebaseio.com/"
})

# path reference path of our database
ref = db.reference('Students')
# adding data

data = {
    # key
    "401":
    # value
        {
            "name": "Sheikh Shihab Hossain",
            "major": "CSE",
            "starting_year": 2019,
            "total_attendence": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-1-8 00:54:34"
        },

    "402":
    # value
        {
            "name": "Emily Blunt",
            "major": "Actress",
            "starting_year": 2019,
            "total_attendence": 8,
            "standing": "VG",
            "year": 3,
            "last_attendance_time": "2023-1-9 00:54:34"
        },

    "403":
    # value
        {
            "name": "Jeff Bezos",
            "major": "CEO, Amazon",
            "starting_year": 1998,
            "total_attendence": 10,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-1-11 00:54:34"
        },

    "404":
    # value
        {
            "name": "Kazi Asif Ahmed",
            "major": "CSE",
            "starting_year": 2015,
            "total_attendence": 11,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-1-5 00:54:34"
        },

    "405":
    # value
        {
            "name": "Mohammad Jabbir",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendence": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-1-5 00:54:34"
        },

    "410":
    # value
        {
            "name": "Elon Musk",
            "major": "CEO, SpaceX",
            "starting_year": 1998,
            "total_attendence": 2,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-1-8 00:54:34"
        },

}

# sending the data to database
for key, value in data.items():
    ref.child(key).set(value)