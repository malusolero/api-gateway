from schemas import UserServiceCreateBodySchema, HeaderSchema
from os import environ
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy.exc import IntegrityError
import requests
from dotenv import load_dotenv

load_dotenv()


info = Info(title="API Gateway", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Docs tags
home_tag = Tag(
    name="Docs", description="Select docs between: Swagger, Redoc or RapiDoc")
api_gateway = Tag(name="API Gateway",
                  description="Redirect each request for the right microservice")


LOGIN_SERVICE_URL = environ.get('LOGIN_SERVICE')


@app.get('/', tags=[home_tag])
def home():
    """ Redirects for /openapi, screen for choosing the documentation.
    """
    return redirect('/openapi')

# LOGIN SERVICE REDIRECTS


@app.post('/user', tags=[api_gateway])
def redirect_create_user(body: UserServiceCreateBodySchema):
    '''
        Redirects to user service create user route, check user service swagger for more details
    '''
    try:
        json = {"username": body.username, "password": body.password}
        print(json)
        response = requests.post(
            f'{LOGIN_SERVICE_URL}/user', json=json)
        print(response.text)
        return response.text, response.status_code
    except Exception as e:
        print(e)
        error_message = f'{e}'
        return {"message": error_message}, 400


@app.post('/user/login', tags=[api_gateway])
def redirect_login(body: UserServiceCreateBodySchema):
    '''
        Redirects to user service login route, check user service swagger for more details
    '''
    try:
        json = {"username": body.username, "password": body.password}
        print(json)
        response = requests.post(
            f'{LOGIN_SERVICE_URL}/user/login', json=json)
        print(response.text)
        return response.text, response.status_code
    except Exception as e:
        print(e)
        error_message = f'{e}'
        return {"message": error_message}, 400


@app.get('/user/is-authenticated', tags=[api_gateway])
def redirect_user_is_authenticated(header: HeaderSchema):
    '''
        Redirects to user service is authenticated route, check user service swagger for more details
    '''
    try:
        print('HEADEEEER')
        print(header.authorization)

        return {"message": 'ok'}, 200
    except Exception as e:
        print(e)
        error_message = f'{e}'
        return {"message": error_message}, 400
