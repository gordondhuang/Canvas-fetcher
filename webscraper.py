import time
import requests
import json

token = open("canvas-token.txt", "r")
apiKey = token.readline().strip()
user_id = token.readline().strip()
url ="http://canvas.uw.edu/api/v1/courses/"

headers = {
    'Authorization': f'Bearer {apiKey}'
}

params = {
    'enrollment_type': 'student',  # Change to your preferred enrollment type
    'enrollment_state': 'active',  # Change to your preferred enrollment state
}

response = requests.get(url, params=params, headers=headers)
if response.status_code == 200:
    courses = response.json()
    print(courses)
else:
    print('Failed to retrieve courses. Status code', response.status_code)