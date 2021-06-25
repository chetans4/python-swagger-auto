# from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with
from flask import jsonify
from pyms.flask.app import Microservice

ms = Microservice(path=__file__)
app = ms.create_app()

# app = Flask(__name__)  # Flask app instance initiated
api = Api(app)  # Flask restful wraps Flask app around it.

awesome_response_schema = dict(
    message=fields.String(default='')
)

#  Restful way of creating APIs through Flask Restful

class AwesomeAPI(Resource):

    @marshal_with(awesome_response_schema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        return {'message': 'My First Awesome API'}


api.add_resource(AwesomeAPI, '/awesome')

if __name__ == '__main__':
    app.run(debug=True)
