import time
import requests
import json
import csv

# Creates a CSV file with a column view of course information
def create_csv(fileName):
    with open(fileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headings = ["Course Name", "Instructor", "Section", "Syllabus Link","Time"]
        writer.writerow(headings)

# Creates the JSON file to create the CSV file
def create_json(data): 
    with open ("courses.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

# Parses the JSON data to convert to CSV
def json_parser(data):
    with open("courses.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for course in data:
            course_data = []
            favorite = course.get('is_favorite') # Check if this is one of the courses that is listed as a favorite
            
            if favorite :
                course_Name = course.get('course_code')
                instructor_Name = course.get('teachers')[0].get('display_name')
                section = course.get('sections')[0].get('name')
                course_data.append(course_Name)
                course_data.append(instructor_Name)
                course_data.append(section)
                writer.writerow(course_data)
                print(course_data)

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
    'exclude_blueprint_courses': True,
    'state[]': ['available'],
    'include[]': ['syllabus_body','term', 'sections','teachers','concluded','favorites','public_description']
}

response = requests.get(url, params=params, headers=headers)
if response.status_code == 200:
    courses_data = response.json()
    create_json(courses_data)
    create_csv("courses.csv")
    parsed_courses = json_parser(courses_data)
else:
    print('Failed to retrieve courses. Status code', response.status_code)