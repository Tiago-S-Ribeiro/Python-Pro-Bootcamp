from data import API_KEY, APP_ID, ENDPOINT, GENDER, WEIGHT, HEIGHT, AGE, WORKOUT_ENDPOINT, AUTH
import requests
import datetime as dt

workout_headers = {
    "Authorization": AUTH
}

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

current_date = dt.datetime.now()
user_input = input("What exercises have you done today? ")

user_headers = {
 "query": user_input,
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}

response = requests.post(url=ENDPOINT, json=user_headers, headers=nutri_headers)
response_data = response.json()

for workout in response_data["exercises"]:
    workout_data = {
        "workout": {
            "date": current_date.strftime('%d/%m/%Y'),
            "time": current_date.strftime('%H:%M:%S'),
            "exercise": workout["name"].title(),
            "duration": round(workout["duration_min"]),
            "calories" : round(workout["nf_calories"])
        }
    }
    response_workout = requests.post(url=WORKOUT_ENDPOINT, json=workout_data, headers=workout_headers)
    print(response_workout.text)