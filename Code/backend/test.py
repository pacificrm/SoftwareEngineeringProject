
import requests


#--------------------------------Prashant's code starts----------------------------------------#
def test_user_signup():
    api_url = 'http://127.0.0.1:5000/api/user'
    data = {
        "email": "testuser1@example.com",
        "username": "testuser1",
        "password1": "testpassword",
    }
    # Make the POST request
    response = requests.post(api_url, json=data)
    # Assert the status code is 200 (Success)
    assert response.status_code == 200 or response.status_code==400

def test_generate_learning_path():
    # Define the API URL
    api_url = 'http://127.0.0.1:5000/api/learning_path/S001'
    
    # Define the payload (course data)
    data = {
        "term_1": ["BDM", "MAD1", "DBMS", "MAD1 Project"],
        "term_2": ["PDSA", "MLF", "MAD2", "MAD2 Project"],
        "term_3": ["BA", "MLT", "Java", "TDS"],
        "term_4": ["MLP", "SC", "MLT Project", "MLP Project"]
    }
    # Make the API request
    response = requests.post(api_url, json=data)
    # Assert the status code
    assert response.status_code == 201

def test_generate_learning_path_errors():
    api_url = 'http://127.0.0.1:5000/api/learning_path/S001'
    # Intentionally omitting the course_data to trigger an error
    # Make the POST request. 
    response = requests.post(api_url)
    # Assert the status code is 400
    assert response.status_code == 400

def test_current_learning_path():
    api_url = 'http://127.0.0.1:5000/api/learning_path/S001'
    # Make the GET request
    response = requests.get(api_url)
    # Assert the status code is 200
    assert response.status_code == 200

def test_current_learning_path_error():
    api_url = 'http://127.0.0.1:5000/api/learning_path/x'
    # Make the GET request
    response = requests.get(api_url)
    # Assert the status code is 404 
    assert response.status_code == 404

def test_top_rated_learning_paths():
    api_url = 'http://127.0.0.1:5000/api/top_rated_learning_path' 
    # Make the GET request
    response = requests.get(api_url)
    # Assert the status code is 200 (Success)
    assert response.status_code == 200

def test_all_learning_paths():
    api_url = 'http://127.0.0.1:5000/api/all_learning_path'
    # Make the GET request
    response = requests.get(api_url)
    # Assert the status code is 200 (Success)
    assert response.status_code == 200

def test_learning_path_feedbacks():
    api_url = 'http://127.0.0.1:5000/api/feedbacks/1'
    # Make the GET request
    response = requests.get(api_url)
    # Assert the status code is 200 (Success)
    assert response.status_code == 200

def test_learning_path_feedbacks_error():
    api_url = 'http://127.0.0.1:5000/api/feedbacks/100009'
    # Make the GET request
    response = requests.get(api_url)
    # Assert the status code is 404 (Not Found)
    assert response.status_code == 404

def test_post_learning_path_feedbacks():
    api_url = 'http://127.0.0.1:5000/api/feedbacks/1/1'
    # Define the data you want to send in the POST request
    data = {
        'rating': 5,
        'remarks': 'Great learning experience!',
    }
    # Make the POST request
    response = requests.post(api_url, json=data)
    # Assert the status code is 201 (Created)
    assert response.status_code == 201

def test_post_learning_path_feedbacks_error():
    api_url = 'http://127.0.0.1:5000/api/feedbacks/1/100001'
    # Define the data with missing required fields for error case
    data = {
        'remarks': 'Great learning experience!',
    }
    # Make the POST request
    response = requests.post(api_url, json=data)
    # Assert the status code is 404 (Path Not found)
    assert response.status_code == 404

#--------------------------------Prashant's code ends---------------------------------------#

#-------------------------Aditi starts-----------------------------
def test_get_courses():
    # Make the GET request
    api_url = 'http://127.0.0.1:5000/api/courses'
    response = requests.get(api_url)
    # Assert the status code is 200 (Success)

def test_get_course():
    api_url='http://127.0.0.1:5000/api/course'

    # Make the GET request
    response = requests.get(api_url)
    # Assert the status code is 200 (Success)
    assert response.status_code == 200
    
def test_post_course():
    api_url = 'http://127.0.0.1:5000/api/course'
    data = {
        'course_id': 'CS004',
        'course_name': 'New Course',
        'pre_req': 'Prerequisite',
        'co_req': 'Corequisite',
        'type': 'Programming',
        'level': '4',
        'project': 'Project',
    }   
    # Make the POST request
    response = requests.post(api_url, json=data)
    # Assert the status code is 201 (Success)
    assert response.status_code == 201

def test_put_course():
    api_url = 'http://127.0.0.1:5000/api/course/CS004'
    # Replace {id} with the actual course_id
    data = {
        'course_name': 'Course',
        'pre_req': 'Updated Prerequisite',
        'co_req': 'Updated Corequisite',
        'type': 'Data Science',
        'level': '2',
        'project': 'Updated Project',
    }
    response = requests.put(api_url, json=data)
    # Assert the status code is 200 (Success)
    assert response.status_code == 200

def test_put_course_error():
    api_url = 'http://127.0.0.1:5000/api/course/CSS04'
    # Intentially giving wrong course id
    data = {}
    response = requests.put(api_url, json=data)
    # Assert the status code is 404 (Not Found)
    assert response.status_code == 404

def test_delete_course():
    api_url = 'http://127.0.0.1:5000/api/course/CS004'
    # Make the DELETE request
    response = requests.delete(api_url)
    # Assert the status code is 200 (Success)
    assert response.status_code == 200

def test_delete_course_error():
    api_url = 'http://127.0.0.1:5000/api/course/CSS004'
    # Make the DELETE request
    response = requests.delete(api_url)
    # Assert the status code is 500 (Success)
    assert response.status_code == 500


#-------------------------Aditi ends-----------------------------


#-------------------------Mukesh Starts----------------------------

def test_api_call_success():
    api_url = 'http://127.0.0.1:5000/api/CourseFeedback/1'
    
    # Make the API call
    response = requests.get(api_url)

    # Assert the status code is 200
    assert response.status_code == 200

def test_api_call_fail():
    api_url = 'http://127.0.0.1:5000/api/CourseFeedback/25'
    
    # Make the API call
    response = requests.get(api_url)

    # Assert the status code is 403
    assert response.status_code == 404

def test_api_call_fail_1():
    api_url = 'http://127.0.0.1:5000/api/CourseFeedback/1000000000'
    
    # Make the API call
    response = requests.get(api_url)

    # Assert the status code is 500
    assert response.status_code == 404

def test_api_call_fail_2():
    api_url = 'http://127.0.0.1:5000/api/CourseFeedback/-1'
    
    # Make the API call
    response = requests.get(api_url)

    # Assert the status code is 404
    assert response.status_code == 404

def test_post_request():

    api_url = 'http://127.0.0.1:5000/api/CourseFeedback/19'

    # Define the data you want to send in the POST request
    data = {
        "subject_id": '4',
        "rating": '5',
        "remarks": "Very good"
    }


    # Make the POST request. PLEASE use JSON so that data will pass as Json
    response = requests.post(api_url, json=data)

    # Assert the status code is 201 or any other expected status code
    assert response.status_code == 201

def test_post_request_fail():

    api_url = 'http://127.0.0.1:5000/api/CourseFeedback/1'

    # Define the data you want to send in the POST request
    data = {
        "subject_id": "",
        "rating": 4,
        "remarks": "Very good"
    }

    # Make the POST request. PLEASE use JSON so that data will pass as Json
    response = requests.post(api_url, json=data)

    # Assert the status code is 201 or any other expected status code
    assert response.status_code == 201

def test_put_request():

    api_url = 'http://127.0.0.1:5000/api/CourseFeedback/1/C001'

    # Define the data you want to send in the POST request
    data = {
        "rating": 5,
        "remarks": "Very good"
    }

    # Make the POST request. PLEASE use JSON so that data will pass as Json
    response = requests.put(api_url, json=data)

    # Assert the status code is 201 or any other expected status code
    assert (response.status_code == 201 or response.status_code ==404)

def test_StudentAcademic_api_call_success():
    api_url = 'http://127.0.0.1:5000/api/StudentAcademicInfo/S001/F2-2022'
    
    # Make the API call
    response = requests.get(api_url)

    # Assert the status code is 200
    assert response.status_code == 200

def test_Studentprofile_post_call_success():
    api_url = 'http://127.0.0.1:5000/api/StudentProfile'
    
    # Define the data you want to send in the POST request
    data = {
    "roll_number":"S009",
    "academic_interests": "Higher study",
    "learning_goals" : "DP",
    "schedules" :    "3 month",
    "commitments" :"Higher study+1"
}

    # Make the POST request. PLEASE use JSON so that data will pass as Json
    response = requests.post(api_url, json=data)

    # Assert the status code is 201 or any other expected status code
    assert (response.status_code == 201 or response.status_code == 200)

def test_Studentprofile_get_call_success():
    api_url = 'http://127.0.0.1:5000/api/StudentProfile/S009'
    

    # Make the API call
    response = requests.get(api_url)

    # Assert the status code is 200
    assert response.status_code == 200

def test_Studentprofile_get_call_fail():
    api_url = 'http://127.0.0.1:5000/api/StudentProfile/2999999999999'
    

    # Make the API call
    response = requests.get(api_url)

    # Assert the status code is 200
    assert response.status_code == 404    
#--------------------------Mukesh Ends-----------------------------

#-------------------------Anushka starts-------------------------

def test_admin_data():
    # Replace {email} with the actual admin email
    api_url = 'http://127.0.0.1:5000/api/admin/admin@example.com'
    email = 'admin@example.com'
    # Make the GET request
    #response = requests.get(f'{api_url}/{email}')
    response = requests.get('http://127.0.0.1:5000/api/admin/admin@example.com')
    # Assert the status code is 200 (Success)
    assert response.status_code == 200

#--------------------------Anushka Ends----------------------------

#----------------------------Sandeep Starts------------------------

def test_add_gpa_api_success():
    api_url = 'http://127.0.0.1:5000/api/add_gpa'
    data = {
    "roll_number": "S018", # Pleae increase the rollnumber to 1 so that it will save in database due to constraint issue
    "term_id": "F2-2022",
    "sgpa": 7.8,
    "cgpa": 7.6
}
    response = requests.post(api_url, json=data)
    assert (response.status_code == 201 or response.status_code == 200)

def test_add_gpa_api_failure():
    api_url = 'http://127.0.0.1:5000/api/add_gpa'

    # Define the data you want to send in the POST request
    data = {
    "roll_number": "S006",
    "term_id": "t23",
    "sgpa": "k",
    "cgpa": 7.6
}

    response = requests.post(api_url, json=data)
    assert response.status_code == 400

def test_add_student_academic_info_api_success():
    api_url = 'http://127.0.0.1:5000/api/add_student_acamdemic_info'
    data = {
  "roll_number": "S011", #
  "term_id": "F3-F023",
  "course_id": "CS101",
  "avg_ga": 85.5,
  "quiz1": 75.0,
  "quiz2": 88.5,
  "end_term": 92.0,
  "oppe1": 90.0,
  "oppe2": 87.5,
  "project": 95.0,
  "final_score": 89.7
}
    response = requests.post(api_url, json=data)
    assert response.status_code == 201

def test_add_student_academic_info_api_failure():
    api_url = 'http://127.0.0.1:5000/api/add_student_acamdemic_info'

    # Define the data you want to send in the POST request
    data = {
  "term_id": "F2Y232",
  "course_id": "CS101",
  "avg_ga": "na",
  "quiz1": 75.0,
  "quiz2": 88.5,
  "end_term": 92.0,
  "oppe1": 90.0,
  "oppe2": 87.5,
  "project": 95.0,
  "final_score": 89.7
}

    response = requests.post(api_url, json=data)
    assert response.status_code == 400

def test_add_offline_education_api_success():
    api_url = 'http://127.0.0.1:5000/api/add_offline_education'

    data = {
  "roll_number": "S001",
  "degree": "Bachelor of Science",
  "major": "Computer Science",
  "end_year": "2022"
    }
    response = requests.post(api_url, json=data)
    assert response.status_code == 201

def test_add_offline_education_api_failure():
    api_url = 'http://127.0.0.1:5000/api/add_offline_education'

    # Define the data you want to send in the POST request
    data = {
  "degree": "Bachelor of Science",
  "major": "Computer Science",
  "end_year": "2022"
}

    response = requests.post(api_url, json=data)
    assert response.status_code == 400


#-------------------------------Sandip Ends-----------------------------