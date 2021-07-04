#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import requests
import json

url = 'https://validus.gymsystem.se'
login_data = '{"login": "email@example.com", "password": "mypassword"}'
headers = {'Authorization': 'Zoezi 48390b97731921c491c40837076154e4eeb3cd19faab7ad7aa0a359333f9db64'}
workout_id = '8894'
fromDate='2021-07-06'
toDate='2021-07-15'
searchString = 'FUN SATURDAY'


# Create Session and Login
s = requests.Session()

session = s.post(url + '/api/v8.0/memberapi/login', data=login_data, headers=headers)

# Get available Workouts based on name
list_workouts = s.get(url + '/api/v8.0/public/workout/get/all?fromDate=' + fromDate + '&toDate=' + toDate, headers=headers)
workouts = json.loads(list_workouts.text)
for wrk in workouts['workouts']:
    if wrk['workoutType']['name'] == searchString:
        data_set = {
                        'name': wrk['workoutType']['name'],
                        'start': wrk['startTime'],
                        'end': wrk['endTime'],
                        'workout_id': wrk['id']
        }

print(data_set)

# Book Workout
#bookWorkout = s.post(url + '/api/v8.0/memberapi/workoutBooking/add?workout=' + workout_id + '&method=trainingcard', headers=headers)
#print(bookWorkout.text)
