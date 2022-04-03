from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config.from_object('api.config.Config')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'strivers'
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(64), unique=False, nullable=True)

    def __init__(self, email, name=''):
        self.email = email
        self.name = name
        

class Striver_api(Resource):

    def get(self):
        args_parser = reqparse.RequestParser()
        args_parser.add_argument('email', type=str)

        args = args_parser.parse_args()
        email_ = args['email']

        try:
            user_info = db.session.query(User).filter_by(email=email_).first()
            return {"Name": user_info.name, 'Email': user_info.email}
        except:
            return {"ERROR": "Couldn't find email"}

        
    
    def post(self):
        # print('here')
        dict_ = request.json
        print('the content is: ',dict_)
        # args_parser = reqparse.RequestParser()
        # args_parser.add_argument('email', type=str)
        # args_parser.add_argument('name', type=str)

        # args = args_parser.parse_args()
        # email_ = args['email']
        # name_ = args['name']
        # print(email_, name_)
        

        

        # try:
        #     db.session.add(User(email=email_, name=name_))
        #     db.session.commit()
        #     # return {"email": email_, 'name': name_}
        #     print({"email": email_, 'name': name_})
        #     return jsonify({"email": email_, 'name': name_})
        # except:
        #     return {"ERROR": "Couldn't insert email"}
api.add_resource(Striver_api, '/striver')