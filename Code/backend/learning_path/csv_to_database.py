import sqlite3
import csv

# Function to create a connection to the SQLite database
def create_connection(database):
    try:
        conn = sqlite3.connect(database)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None



# Student table 
def create_student_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
                roll_number TEXT PRIMARY KEY,
                full_name TEXT,
                dob DATE,
                current_level TEXT,
                current_status TEXT,
                offline_role TEXT
            )
        ''')
    except sqlite3.Error as e:
        print(e)


# course Table 
def create_course_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id TEXT PRIMARY KEY,
                name TEXT,
                prerequisite TEXT NULL,
                corequisite TEXT NULL,
                course_type TEXT,
                type TEXT,
                level INTEGER,
                project TEXT NULL
            )
        ''')
    except sqlite3.Error as e:  
        print(e)

# offline Education table 
def create_offline_education(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS offline_education (
                roll_number TEXT PRIMARY KEY,
                degree TEXT,
                major TEXT,
                end_year INTEGER
            )
        ''')
    except sqlite3.Error as e:
        print(e)

# course feedback table   	
def create_course_feedback(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS course_feedback (
                id INTEGER PRIMARY KEY,
                subject_id TEXT,
                rating INTEGER,
                remarks TEXT
            )
        ''')
    except sqlite3.Error as e:
        print(e)



# acedemic info    
def create_academic_info(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS academic_info (
                roll_number TEXT,
                term_id INTEGER,
                course_id TEXT,
                avg_ga INTEGER,
                quiz1 INTEGER , 
                quiz2 INTEGER , 
                end_term INTEGER , 
                oppe1 INTEGER NULL , 
                oppe2 INTEGER NULL, 
                project INTEGER NULL, 
                final_score INTEGER 
                
            )
        ''')
    except sqlite3.Error as e:
        print(e)


# gpa details table   

def create_gpa_details(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gpa_details (
                student_id TEXT,
                term_id INTEGER,
                sgpa REAL,
                cgpa REAL
            )
        ''')
    except sqlite3.Error as e:
        print(e)



# Function to insert data into the student table
def insert_student_data(conn, data):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO student (
                roll_number, full_name, dob, current_level, current_status, offline_role
            ) VALUES (?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Insert data into the course table
def insert_course_data(conn, data):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO courses (id , name, prerequisite, corequisite, course_type, type , level , project)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Insert data into the offline_education table
def insert_offline_education_data(conn, data):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO offline_education (roll_number, degree, major, end_year)
            VALUES (?, ?, ?, ?)
        ''', data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Insert data into the course_feedback table
def insert_course_feedback_data(conn, data):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO course_feedback (id , subject_id, rating, remarks)
            VALUES (?, ?, ?, ?)
        ''', data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Insert data into the academic_info table
def insert_academic_info_data(conn, data):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO academic_info (
                roll_number, term_id, course_id, avg_ga, quiz1, quiz2, 
                end_term, oppe1, oppe2, project, final_score
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Insert data into the gpa_details table
def insert_gpa_details_data(conn, data):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO gpa_details (student_id, term_id, sgpa, cgpa)
            VALUES (?, ?, ?, ?)
        ''', data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)



# Function to read data from the CSV file and insert it into the database
def process_csv_and_insert_into_db(csv_file, database):
    conn = create_connection(database)
    if conn is not None:
        # create_student_table(conn)
        # create_course_table(conn)
        # create_offline_education(conn)
        # create_course_feedback(conn)
        # create_academic_info(conn)
        create_gpa_details(conn)

        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            # Skip the header row
            next(csv_reader)

            for row in csv_reader:
                # insert_student_data(conn, tuple(row))
                # insert_course_data(conn, tuple(row))
                # insert_offline_education_data(conn, tuple(row))
                # insert_course_feedback_data(conn, tuple(row))
                # insert_academic_info_data(conn, tuple(row))
                insert_gpa_details_data(conn, tuple(row))

        conn.close()
        print("Data inserted successfully.")


# process_csv_and_insert_into_db('student.csv', 'database.db')
# process_csv_and_insert_into_db('courses.csv', 'database.db')
# process_csv_and_insert_into_db('offline_education.csv', 'database.db')
# process_csv_and_insert_into_db('course_feedback.csv', 'database.db')
# process_csv_and_insert_into_db('acedemic_info.csv', 'database.db')
process_csv_and_insert_into_db('gpa_details.csv', 'database.db')
