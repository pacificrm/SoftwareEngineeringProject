from os import path
from flask import Flask , render_template,request,redirect,flash
from models import *
from flask_security import Security
from flask_restful import Api
from flask_cors import CORS
from api import *

app= Flask(__name__)

cd= path.abspath(path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+path.join(cd,"database.sqlite3")
app.config['SECURITY_USERNAME_ENABLE']=True
# app.config['SECURITY_TRACKABLE']=True
app.config['SECRET_KEY'] = "yudw890_ASHudb^T^%VSA%&*CASGVHSbsjdbjsd"
app.config['SECURITY_PASSWORD_SALT'] = 'Thi$_is@#super9secrets%$'
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = "Authentication-Token"
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'

api=Api(app)
CORS(app)
db.init_app(app)

app.app_context().push()

Security().init_app(app, user_datastore)

api.add_resource(UsersAPI, '/api/user')
api.add_resource(CourseAPI, '/api/course', '/api/course/<string:id>')
api.add_resource(CourseFeedbackAPI,"/api/CourseFeedback/<int:UserIdParam>","/api/CourseFeedback/<int:UserIdParam>/<string:subject_id>")
api.add_resource(StudentAcademicInfoAPI,"/api/StudentAcademicInfo/<string:RollNumberParam>/<string:TermIdParam>")
api.add_resource(StudentProfileAPI,"/api/StudentProfile","/api/StudentProfile/<string:RollNumberParam>")
api.add_resource(LearningPathAPI, '/api/learning_path/<string:roll_number>')
api.add_resource(LearningPathFeedbackListAPI, '/api/feedbacks/<int:learning_path_id>','/api/feedbacks/<int:user_id>/<int:learning_path_id>')
api.add_resource(StudentResource,"/api/add_student")
api.add_resource(GpaResource,"/api/add_gpa")
api.add_resource(OfflineEducationResource,"/api/add_offline_education")
api.add_resource(StudentAcademicInfoResource,"/api/add_student_acamdemic_info")
api.add_resource(AdminHomeAPI,"/api/admin/<string:email>")
api.add_resource(TopRatedPathAPI,'/api/top_rated_learning_path')
api.add_resource(AllPathAPI,'/api/all_learning_path')

# @app.before_first_request
# def create():
#     if not path.exists('sqlite:///database.sqlite3'):
#         db.create_all()
with app.app_context():
    if not path.exists('sqlite:///database.sqlite3'):
        db.create_all()

@app.route('/')
def start():
    return "hello"

if __name__=="__main__":
    app.run(debug=True)
