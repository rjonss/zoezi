#!/bin/bash
url=https://validus.gymsystem.se
header='Authorization: Zoezi 48390b97731921c491c40837076154e4eeb3cd19faab7ad7aa0a359333f9db64'
cookie=cookie.txt

workout_id='5357' #Open Gym 2021-07-08 05-07

curl -X POST --cookie $cookie --cookie-jar $cookie -H '$header' -d '{"login": "email@emample.com","password": "mypassword"}' "$url/api/v8.0/memberapi/login"
curl -X POST --cookie $cookie --cookie-jar $cookie -H '$header' "$url/api/v8.0/memberapi/workoutBooking/add?workout=$workout_id&method=trainingcard" | json_pp
