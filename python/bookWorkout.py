#!/usr/bin/python3

import requests
import json
import datetime

url = 'https://validus.gymsystem.se'
login_data = '{"login": "mymail@example.com", "password": "mypass"}'
headers = {'Authorization': 'Zoezi 48390b97731921c491c40837076154e4eeb3cd19faab7ad7aa0a359333f9db64'}
days=5
today = datetime.datetime.now()
fromDate=(today + datetime.timedelta(days=days)).strftime("%Y-%m-%d")
toDate=(today + datetime.timedelta(days=days)).strftime("%Y-%m-%d")
searchString = 'Olympiska lyft'


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
bookWorkout = s.post(url + '/api/v8.0/memberapi/workoutBooking/add?workout=' + str(data_set['workout_id']) + '&method=trainingcard', headers=headers)
print(bookWorkout.text)
