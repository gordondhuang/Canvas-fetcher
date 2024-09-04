from datetime import datetime
import time
import requests
import json
import csv

def main():
    token = open("canvas-key.txt", "r")
    apiKey = token.readline().strip()
    user_id = token.readline().strip() 
    canvas = token.readline().strip()
    course_url = f"https://{canvas}/api/v1/courses/"

    headers = {
        'Authorization': f'Bearer {apiKey}'
    }

    params = {
        'enrollment_type': 'student',  # Change to your preferred enrollment type
        'enrollment_state': 'active',  # Change to your preferred enrollment state
        'exclude_blueprint_courses': True,
        'state[]': ['available'],
        'include[]': ['term', 'sections','teachers','concluded','favorites','public_description'],
        'per_page': 100
    }

    response = requests.get(course_url, params=params, headers=headers)
    if response.status_code == 200:
        courses_data = response.json()
        create_courses("courses.csv")
        parsed_courses = course_parser(courses_data)
    else:
        print('Failed to retrieve courses. Status code', response.status_code)

    assignment_list_generator(canvas, params, headers)

# Creates a CSV file with a column view of course information
def create_courses(fileName):
    with open(fileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headings = ["Course Name", "Instructor", "Section", "Course ID", "Syllabus Link","Time"]
        writer.writerow(headings)

# Creates a CSV file with a column view of assignments and due dates
def create_assignments(fileName):
    with open(fileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headings = ["Courses", "Assignments", "Dates"]
        writer.writerow(headings)

def create_courseList(data, fileName):
    with open(fileName, 'w+') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Parses the JSON data to convert to CSV
def course_parser(data):
    with open("courses.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        courses_list = []
        json.dumps('courses.json', indent=4)
        for course in data:
            course_data = []
            favorite = course.get('is_favorite') # Check if this is one of the courses that is listed as a favorite
            
            if favorite :
                courses_dict = {}
                course_Name = course.get('course_code')
                instructor_Name = course.get('teachers')[0].get('display_name')
                section = course.get('sections')[0].get('name')
                id = course.get('id')
                courses_dict.update({'course_name' : course_Name})
                courses_dict.update({'instructor_name' : instructor_Name})
                courses_dict.update({'section' : section})
                courses_dict.update({'id' : id})
            
                courses_list.append(courses_dict) 
                for key in courses_dict:
                    course_data.append(courses_dict[key])
                writer.writerow(course_data)

        create_courseList(courses_list, "courses.json")
        
def update_assignments(data, course):
    with open(course, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for assignment in data:
            assignment_data = []
            assign_name = assignment.get('name')
            due_date = assignment.get('due_at')
            if due_date is not None:
                due_date_obj = datetime.strptime(due_date, '%Y-%m-%dT%H:%M:%SZ')
                due_date = due_date_obj.strftime("%m/%d/%y")
            assignment_data.append(course)
            assignment_data.append(assign_name)
            assignment_data.append(due_date)
            writer.writerow(assignment_data)

        

# Generate assignment csv files for each class
def assignment_list_generator(canvas,params,headers):
    params.clear()
    params.update({'type': 'assignment'})
    params.update({'all_events' : 'True'})
    params.update({'order_by': 'due_at'})
    params.update({'per_page': 100})
    assignment_urls = []
    courses = []

    with open("courses.json", 'r') as jsonfile:
        courses_data = json.load(jsonfile)
        for course in courses_data:
            courses.append(course.get('course_name'))
            assignment_urls.append(f"https://{canvas}/api/v1/courses/{course.get('id')}/assignments")

        for i, url in enumerate(assignment_urls):
            response = requests.get(url, params=params, headers=headers)
            if response.status_code == 200:
                course_csv = f"{courses[i]}.csv"
                create_assignments(course_csv)
                update_assignments(response.json(), course_csv)
            else:
                print('Failed to retrieve assignments. Status code', response.status_code)
main()