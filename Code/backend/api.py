from flask_security import SQLAlchemyUserDatastore, auth_required, current_user, hash_password
from flask_restful import Resource, reqparse, fields, marshal_with,abort
from flask import jsonify,request,json
from sqlalchemy import func
from models import *
from datetime import datetime
from Path_generator import path_generator
from matplotlib import pyplot as plt
import os
from sqlalchemy.exc import IntegrityError
from flask import abort, current_app

user_datastore = SQLAlchemyUserDatastore(db, Users, Role)
wrkng_dir = os.path.abspath(os.path.dirname(__file__))

user_fields = {
    'username' : fields.String ,
    'email' : fields.String ,
}
user_req = reqparse.RequestParser()
user_req.add_argument('email', required=True, help="email required")
user_req.add_argument('username', required=True, help="username required")
user_req.add_argument('password1', required=True, help="password required")


class UsersAPI(Resource):
    @auth_required('token')
    def get(self):
        # chk=Users.query.filter_by(id=current_user.id).first()
        return { 'email':current_user.email,'username':current_user.username, }
    @marshal_with(user_fields)
    def post(self):
        args = user_req.parse_args()
        email = args.get("email")
        user_name = args.get("username")
        passw = args.get("password1")
        check1=Users.query.filter_by(email=email).first()
        check2=Users.query.filter_by(username=user_name).first()
        if check1:
           return jsonify('User already exist!! Try with another email.'),400
        elif check2:
           return jsonify('User already exist!! Try with another username.'),401
        elif not check1 and not check2:    
            user_datastore.create_user(email=email,username=user_name,password=hash_password(passw))
            db.session.commit()
            data = Users.query.filter_by(email=email).first()
            return data,200
        else:
            return jsonify('Error happend !! Please enter the details again. '),500
#---------------------Anushka Starts---------------------------------------------
admin_fields = {
    'tstudents': fields.Integer,
    'tcourses': fields.Integer,
    'counts':fields.String,
    'StudentsDataSummaryReport':fields.String
}

class AdminHomeAPI(Resource):
    admin_req=reqparse.RequestParser()
    admin_req.add_argument('tstudents', required=True, help="Total Number of students")
    admin_req.add_argument('tcourses', required=True, help="Total Number of students")
    #@auth_required('token')
    @marshal_with(admin_fields)
    def get(self, email):
        tstudents=Student.query.all()
        t=Course.query.all()
        tcourses = len(t)
        possible_ratings=[1,2,3,4,5]
        counts={}
        y_l=[]
        for i in possible_ratings:
            cnt =LearningPathFeedback.query.filter_by(rating=i).all()
            counts[i] = len(cnt)
            y_l.append(counts[i])
        plt.clf()
        plt.plot(possible_ratings, y_l, c='r', ls='dashed', marker='o')
        path = os.path.join(wrkng_dir, "static/IMG/")
        plt.savefig(path+"StudentSatisfactionMetric.png")
        StudentsDataSummaryReport={}
        # x=Student.query.filter(date).unique().all()
        return tstudents, tcourses, counts, StudentsDataSummaryReport, 200
#------------------------Anushka Ends--------------------------------------------

#---------------------Aditi Starts-----------------------------------------------

course_fields={
    'course_id':fields.Integer,
    'course_name':fields.String,
    'pre_req':fields.String,
    'co_req':fields.String,
    'type':fields.String,
    'level':fields.String,
    'project':fields.String
}
 
course_req=reqparse.RequestParser()
course_req.add_argument('course_id', help="Course ID")
course_req.add_argument('course_name', help="Course Name")
course_req.add_argument('pre_req', help="Pre requisite")
course_req.add_argument('co_req', help="Co-requisite")
course_req.add_argument('type', help="Type of Course")
course_req.add_argument('level', help="Level of Course")
course_req.add_argument('project', help="Whether or not project is there in the course")
 
class CourseAPI(Resource):
    def get(self):
        try:
            c = Course.query.all()
            courses = {}
            for i in c:
                courses[i.id] = {
                    'id': i.id,
                    'name': i.name,
                    'prerequisite': i.prerequisite,
                    'corequisite': i.corequisite,
                    'type': i.type,
                    'level': i.level,
                    'project': i.project
                }
            return courses, 200
        except:
            return jsonify({'error': 'An error occurred! Please try again.'}), 403
    
    @marshal_with(course_fields)
    def post(self):
        try:
            args = course_req.parse_args()
            course_id = args.get("course_id")
            course_name = args.get("course_name")
            pre_req = args.get("pre_req")
            co_req = args.get("co_req")
            type = args.get("type")
            level = args.get("level")
            project = args.get("project")

            chk = Course.query.filter_by(id=course_id).first()
            if chk:
                return jsonify({'error': 'course already exists'}), 401
            ad = Course(id=course_id, name=course_name, prerequisite=pre_req, corequisite=co_req, type=type, level=level, project=project)
            db.session.add(ad)
            db.session.commit()
            return ad, 201
        except Exception as e:
            print(e)
            return jsonify({'error': 'An error occurred! Please enter the details again.'}), 403
        
    # @auth_required('token')
    @marshal_with(course_fields)
    def put(self, id):
        try:
            args = course_req.parse_args()
            course_name = args.get("course_name")
            pre_req = args.get("pre_req")
            co_req = args.get("co_req")
            type = args.get("type")
            level = args.get("level")
            project = args.get("project")
            
            chk = Course.query.filter_by(id=id).first()
            if chk:
                upd = Course.query.filter_by(id=id);
                upd.name=course_name
                upd.prerequisite=pre_req
                upd.corequisite=co_req
                upd.type=type
                upd.level=level
                upd.project=project
                db.session.commit()
                return upd, 200
            else:
                return jsonify({'error': 'The course id does not exist'}), 404

        except:
            return jsonify({'error': 'An error occurred! Please enter the details again.'}), 403
    
    # @auth_required('token')
    def delete(self, id):
        try:
            chk = Course.query.filter_by(id=id).first()
            if chk:
                Course.query.filter_by(id=id).delete()
                db.session.commit()
                return 200
            else:
                return jsonify({'error': 'The course id does not exist'}), 500

        except:
            return jsonify({'error': 'An error occurred! Please try deleting again.'}), 403


#------------------------------------Aditi Ends------------------------------------------------


#-------------------------------------- Mukesh Start ------------------------------------------#

course_feedback = reqparse.RequestParser()
course_feedback.add_argument('user_id')
course_feedback.add_argument('subject_id')
course_feedback.add_argument('rating')
course_feedback.add_argument('remarks')

output_course_feedback ={
    "id" : fields.Integer,
    "user_id" : fields.Integer,
    "subject_id" : fields.String,
    "rating" : fields.Integer,
    "remarks" : fields.String,
    "created" : fields.String
}


class CourseFeedbackAPI(Resource):
    @marshal_with(output_course_feedback)
    def post(self,UserIdParam):
        data = course_feedback.parse_args()
        course_feedback_add = CourseFeedback(user_id=UserIdParam,
                                            subject_id= data.subject_id,
                                            rating = data.rating,
                                            remarks = data.remarks
                                            )
        db.session.add(course_feedback_add)
        db.session.commit()
        return course_feedback_add, 201

    @marshal_with(output_course_feedback)
    def get(self,UserIdParam):
        course_feedback_data = CourseFeedback.query.filter_by(user_id=UserIdParam).all()
        if course_feedback_data:
            return course_feedback_data, 200
        else:
            abort(404,"No feedback for given by user")    

    @marshal_with(output_course_feedback)
    def put(self,UserIdParam,subject_id):

        data = course_feedback.parse_args()

        course_feedback_upd = CourseFeedback.query.filter_by(user_id=UserIdParam,subject_id = subject_id).first()

        if not course_feedback_upd:  
            abort(404, "No feedback for given by user")    
        else:
            course_feedback_upd.rating = data.rating
            course_feedback_upd.remarks = data.remarks
            db.session.commit()
            return course_feedback_upd, 201

output_StudentAcademicInfo={
    "roll_number" : fields.String,
    "term_id" : fields.String,
    "course_id" : fields.String,
    "avg_ga" : fields.Float,
    "quiz1" : fields.Float,
    "quiz2" : fields.Float,
    "end_term" : fields.Float,
    "oppe1" : fields.Float,
    "oppe2" : fields.Float,
    "project" : fields.Float,
    "final_score" : fields.Float,
    "upload_date" : fields.String
}

class StudentAcademicInfoAPI(Resource):
    @marshal_with(output_StudentAcademicInfo)
    def get(self,RollNumberParam,TermIdParam):

        StudentAcademic_data = StudentAcademicInfo.query.filter_by(roll_number=RollNumberParam,term_id=TermIdParam).first()
        if StudentAcademic_data:
            return StudentAcademic_data, 200
        else:
            abort(404, "No previous course registerd by Student")    


student_profile = reqparse.RequestParser()
student_profile.add_argument('roll_number')
student_profile.add_argument('academic_interests')
student_profile.add_argument('learning_goals')
student_profile.add_argument('schedules')
student_profile.add_argument('commitments')

output_student_profile ={
    "roll_number" : fields.String,
    "academic_interests" : fields.String,
    "learning_goals" : fields.String,
    "schedules" : fields.String,
    "commitments" : fields.String
}

class StudentProfileAPI(Resource):
    @marshal_with(output_student_profile)
    def post(self):
        data = student_profile.parse_args()

        student_profile_data = StudentProfileInfo.query.filter_by(roll_number=data.roll_number).first()
        if student_profile_data:
            return  200
        else:    
            student_profile_add = StudentProfileInfo(roll_number=data.roll_number,
                                                academic_interests= data.academic_interests,
                                                learning_goals = data.learning_goals,
                                                schedules = data.schedules,
                                                commitments = data.commitments
                                                )
            db.session.add(student_profile_add)
            db.session.commit()
            return student_profile_add, 201

    @marshal_with(output_student_profile)
    def get(self,RollNumberParam):
        student_profile_data = StudentProfileInfo.query.filter_by(roll_number=RollNumberParam).first()
        if student_profile_data:
            return student_profile_data, 200
        else:
            abort(404,"No student profile found")    

#---------------------- Mukesh Ends------------------------------------------#

#-------------------------Prashant Starts--------------------------

output_learning_path_response = {
    "image_path": fields.String,
}

class LearningPathAPI(Resource):
    @marshal_with(output_learning_path_response)
    def post(self, roll_number):
        try:
            if not request.is_json:
                return {"message": "Request must contain a valid JSON payload"}, 400
            
            course_data = request.get_json()
            image_filename = f"learning_path_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.png"
            path_generator(course_data, image_filename)
            learning_path = LearningPath(image=image_filename, roll_number=roll_number)
            db.session.add(learning_path)
            db.session.commit()

            return {"image_path": image_filename}, 201

        except Exception as e:
            return {"message": str(e)}, 400
               
    @marshal_with(output_learning_path_response)
    def get(self, roll_number):
        # Query the latest learning path for the user
        latest_path = (
            db.session.query(LearningPath)
            .filter_by(roll_number=roll_number)
            .order_by(LearningPath.created.desc())
            .first()
        )

        if latest_path:
            return {"image_path": latest_path.image}

        return {"message": "No learning path found for the user"}, 404


class TopRatedPathAPI(Resource):
    @marshal_with(output_learning_path_response)
    def get(self):
        # Query the top 6 highest rated learning paths
        top_rated_paths = (
            db.session.query(LearningPath)
            .join(LearningPathFeedback)
            .group_by(LearningPath.id)
            .order_by(func.avg(LearningPathFeedback.rating).desc())
            .limit(6)
            .all()
        )

        if top_rated_paths:
            return [{"image_path": path.image} for path in top_rated_paths]

        return {"message": "No learning paths found"}, 404
    
    
class AllPathAPI(Resource):
    @marshal_with(output_learning_path_response)
    def get(self):
        # Query all learning paths sorted by created date in descending order
        all_paths = (
            db.session.query(LearningPath)
            .order_by(LearningPath.created.desc())
            .all()
        )
        if all_paths:
            return [{"image_path": path.image} for path in all_paths]

        return {"message": "No learning paths found"}, 404

feedback_fields = {
    'id': fields.Integer,
    'learning_path_id': fields.Integer,
    'rating': fields.Integer,
    'remarks': fields.String,
}

class LearningPathFeedbackListAPI(Resource):
    @marshal_with(feedback_fields)
    def get(self, learning_path_id):
        learning_path = LearningPath.query.get(learning_path_id)
        if learning_path is None:
            return {'message': 'LearningPath not found.'}, 404
        feedbacks = LearningPathFeedback.query.filter_by(learning_path_id=learning_path_id).all()
        return feedbacks
    @marshal_with(feedback_fields)
    def post(self, user_id, learning_path_id):
        learning_path = LearningPath.query.get(learning_path_id)
        if learning_path is None:
            return {'message': 'LearningPath not found.'}, 404
        json_data = request.get_json()
        # Allow creating feedback with only rating or only remarks
        rating = json_data.get('rating')
        remarks = json_data.get('remarks')

        new_feedback = LearningPathFeedback(
            user_id=user_id,
            learning_path_id=learning_path_id,
            rating=rating,
            remarks=remarks,
        )
        db.session.add(new_feedback)
        db.session.commit()
        return new_feedback, 201

#-----------------------------Prashant Ends-------------------------


#-------------------------Sandip Starts-------------------------------

# Request parser for Student endpoint
student_parser = reqparse.RequestParser()
student_parser.add_argument('roll_number', type=str, required=True)
student_parser.add_argument('full_name', type=str, required=True)
student_parser.add_argument('dob', type=str, required=True)
student_parser.add_argument('current_level', type=str, required=True)
student_parser.add_argument('current_status', type=str, required=True)
student_parser.add_argument('offline_role', type=str, required=True)

# Request parser for GPA endpoint
gpa_parser = reqparse.RequestParser()
gpa_parser.add_argument('term_id', type=str, required=True)
gpa_parser.add_argument('roll_number', type=str, required=True)
gpa_parser.add_argument('sgpa', type=float, required=True)
gpa_parser.add_argument('cgpa', type=float, required=True)

# Request parser for Offline Education endpoint
offline_education_parser = reqparse.RequestParser()
offline_education_parser.add_argument('roll_number', type=str, required=True)
offline_education_parser.add_argument('degree', type=str, required=True)
offline_education_parser.add_argument('major', type=str, required=True)
offline_education_parser.add_argument('end_year', type=str, required=True)

# Request parser for Student Academic Info endpoint
academic_info_parser = reqparse.RequestParser()
academic_info_parser.add_argument('roll_number', type=str, required=True)
academic_info_parser.add_argument('term_id', type=str, required=True)
academic_info_parser.add_argument('course_id', type=str, required=True)
academic_info_parser.add_argument('avg_ga', type=float, required=True)
academic_info_parser.add_argument('quiz1', type=float)
academic_info_parser.add_argument('quiz2', type=float)
academic_info_parser.add_argument('end_term', type=float)
academic_info_parser.add_argument('oppe1', type=float)
academic_info_parser.add_argument('oppe2', type=float)
academic_info_parser.add_argument('project', type=float)
academic_info_parser.add_argument('final_score', type=float)

# Define response fields for marshaling
student_fields = {
    'roll_number': fields.String,
    'full_name': fields.String,
    'dob': fields.String,
    'current_level': fields.String,
    'current_status': fields.String,
    'offline_role': fields.String,
}

gpa_fields = {
    'term_id': fields.String,
    'roll_number': fields.String,
    'sgpa': fields.Float,
    'cgpa': fields.Float,
}

offline_education_fields = {
    'roll_number': fields.String,
    'degree': fields.String,
    'major': fields.String,
    'end_year': fields.String,
}

academic_info_fields = {
    'roll_number': fields.String,
    'term_id': fields.String,
    'course_id': fields.String,
    'avg_ga': fields.Float,
    'quiz1': fields.Float,
    'quiz2': fields.Float,
    'end_term': fields.Float,
    'oppe1': fields.Float,
    'oppe2': fields.Float,
    'project': fields.Float,
    'final_score': fields.Float,
}


# Resource for Student endpoint
class StudentResource(Resource):
    @marshal_with(student_fields)
    def post(self):
        args = student_parser.parse_args()
        # dob_string = args["dob"]
        # try:
        #     date_obj = datetime.strptime(dob_string, "%Y-%m-%d")
        # except ValueError:
        #         abort(400, "Invalid date format for dob. Expected format: YYYY-MM-DD")
        # args["dob"] = date_obj
        try:
            # args = student_parser.parse_args()
            student = Student(**args)
            db.session.add(student)
            db.session.commit()
            return student, 201
        except IntegrityError:
            db.session.rollback()
            abort(409, "Duplicate entry. Roll number already exists.")
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error creating student: {str(e)}")
            abort(500, "Internal Server Error")


# Resource for GPA endpoint
class GpaResource(Resource):
    @marshal_with(gpa_fields)
    def post(self):
        args = gpa_parser.parse_args()
        dummy_student_records = GpaDetails.query.filter_by(roll_number = args["roll_number"]).first()
        try:
            if dummy_student_records :
                return  200
            else:    
                gpa = GpaDetails(**args)
                db.session.add(gpa)
                db.session.commit()
                return gpa, 201
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error creating GPA details: {str(e)}")
            abort(500, "Internal Server Error")

# Resource for Offline Education endpoint
class OfflineEducationResource(Resource):
    @marshal_with(offline_education_fields)
    def post(self):
        args = offline_education_parser.parse_args()
        if not Student.query.filter_by(roll_number=args["roll_number"]).first():
                abort(404, "student not found")
        ole_student = OfflineEducation.query.filter_by(roll_number=args["roll_number"]).first()
        if ole_student:
            db.session.delete(ole_student)
            db.session.commit()
        try:
            offline_education = OfflineEducation(**args)
            db.session.add(offline_education)
            db.session.commit()
            return offline_education, 201
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error creating offline education details: {str(e)}")
            abort(500, "Internal Server Error")

# Resource for Student Academic Info endpoint
class StudentAcademicInfoResource(Resource):
    @marshal_with(academic_info_fields)
    def post(self):       
        args = academic_info_parser.parse_args()
        ole_student = Student.query.filter_by(roll_number=args["roll_number"]).first()
        if not ole_student:
            abort(404, "student not found")
        else:
            try:
                student_tobe_updated = StudentAcademicInfo.query.filter_by(roll_number=args["roll_number"]).first()
                if student_tobe_updated:
                    db.session.delete(student_tobe_updated)
                    db.session.commit()
                academic_info = StudentAcademicInfo(**args)
                db.session.add(academic_info)
                db.session.commit()
                return academic_info, 201
            except Exception as e:
                db.session.rollback()
                current_app.logger.error(f"Error creating student academic info: {str(e)}")
                abort(500, "Internal Server Error")

#-------------------------Sandip Ends-------------------------------