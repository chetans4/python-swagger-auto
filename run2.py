from flask_apispec import marshal_with
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from flask_restful import Resource, Api

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

from flask import jsonify
from pyms.flask.app import Microservice

ms = Microservice(path=__file__)
app = ms.create_app()

# app = Flask(__name__)  # Flask app instance initiated
api = Api(app)  # Flask restful wraps Flask app around it.


class AwesomeResponseSchema(Schema):
    message = fields.Str(default='Success')


class AwesomeAPI(MethodResource, Resource):

    @doc(description='My First GET Awesome API.', tags=['Awesome'])
    @marshal_with(AwesomeResponseSchema)  # marshalling with marshmallow library
    def get(self):
        """
        Get method represents a GET API method
        """
        return {'message': 'My First Awesome API'}


api.add_resource(AwesomeAPI, '/awesome')

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Awesome Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

docs.register(AwesomeAPI)

if __name__ == '__main__':
    app.run(debug=True)
