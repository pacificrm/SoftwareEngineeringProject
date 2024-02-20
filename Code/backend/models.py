from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin,RoleMixin
from datetime import datetime

db=SQLAlchemy()
    
class Student(db.Model):
    __tablename__ = 'student'
    roll_number = db.Column(db.Text, primary_key=True)
    full_name = db.Column(db.Text, nullable=False)
    dob = db.Column(db.Text, nullable=False)  
    current_level = db.Column(db.Text, nullable=False)
    current_status = db.Column(db.Text, nullable=False)
    offline_role = db.Column(db.Text, nullable=True)
    upload_date=db.Column(db.Text, default=datetime.utcnow)

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    prerequisite = db.Column(db.Text, nullable=True)
    corequisite = db.Column(db.Text, nullable=True)
    type = db.Column(db.Text, nullable=False)
    level = db.Column(db.Text, nullable=False)
    project = db.Column(db.Text, nullable=True)

class OfflineEducation(db.Model):
    __tablename__ = 'offline_education'
    roll_number = db.Column(db.Text, db.ForeignKey('student.roll_number'), primary_key=True)
    degree = db.Column(db.Text, nullable=False)
    major = db.Column(db.Text, nullable=False)
    end_year = db.Column(db.Text, nullable=False)  
    upload_date=db.Column(db.Text, default=datetime.utcnow)

class CourseFeedback(db.Model):
    _tablename_ = 'course_feedback'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    subject_id = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    remarks = db.Column(db.Text, nullable=True)
    created=db.Column(db.Text, default=datetime.utcnow)

class StudentAcademicInfo(db.Model):
    __tablename__ = 'student_academic_info'
    roll_number = db.Column(db.Text, db.ForeignKey('student.roll_number'), primary_key=True)
    term_id = db.Column(db.Text, primary_key=True)
    course_id = db.Column(db.Text, primary_key=True)
    avg_ga = db.Column(db.Float, nullable=False)
    quiz1 = db.Column(db.Float, nullable=True)
    quiz2 = db.Column(db.Float, nullable=True)
    end_term = db.Column(db.Float, nullable=True)
    oppe1 = db.Column(db.Float, nullable=True)
    oppe2 = db.Column(db.Float, nullable=True)
    project = db.Column(db.Float, nullable=True)
    final_score = db.Column(db.Float, nullable=True)
    upload_date=db.Column(db.Text, default=datetime.utcnow)

class StudentProfileInfo(db.Model):
    _tablename_ = 'student_profile'
    roll_number = db.Column(db.Text, db.ForeignKey('student.roll_number'), primary_key=True)
    academic_interests = db.Column(db.Text)
    learning_goals = db.Column(db.Text)
    schedules = db.Column(db.Text, nullable=False)
    commitments = db.Column(db.Text, nullable=True)
    upload_date=db.Column(db.Text, default=datetime.utcnow)

class GpaDetails(db.Model):
    __tablename__ = 'gpa_details'
    term_id = db.Column(db.Text,  primary_key=True)
    roll_number = db.Column(db.Text,db.ForeignKey('student.roll_number'), nullable=False,primary_key=True)
    sgpa = db.Column(db.Float, nullable=False)
    cgpa = db.Column(db.Float, nullable=False)
    upload_date=db.Column(db.Text, default=datetime.utcnow)

class LearningPath(db.Model):
    __tablename__ = 'learning_paths'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    image = db.Column(db.Text, nullable=False)
    roll_number = db.Column(db.Text, db.ForeignKey('student.roll_number'), nullable=False)
    created=db.Column(db.Text, default=datetime.utcnow)
    feedbacks = db.relationship('LearningPathFeedback', backref='learning_path', lazy=True)

class LearningPathFeedback(db.Model):
    __tablename__ = 'learning_path_feedback'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    learning_path_id = db.Column(db.Integer, db.ForeignKey('learning_paths.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    remarks = db.Column(db.Text, nullable=True)
    created=db.Column(db.Text, default=datetime.utcnow)


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))) 

class Users(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String , unique=True, nullable=False)
    password = db.Column(db.String , nullable=False)
    username = db.Column(db.String ,unique=True, nullable=True)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(), unique=True, nullable=False)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True)
    description = db.Column(db.String())