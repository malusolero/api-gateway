from schemas import UserServiceCreateBodySchema, HeaderSchema, ProductServiceSearchSchema, ProductServiceCreateOrderSchema, ProductServiceProductPathSchema, ProductServiceCreateProductSchema
from os import environ
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, jsonify
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
PRODUCT_SERVICE_URL = environ.get('PRODUCT_SERVICE')


def transform_authorization_header(header: HeaderSchema):
    return {
        "Authorization": header.authorization
    }


@app.get('/', tags=[home_tag])
def home():
    """ Redirects for /openapi, screen for choosing the documentation.
    """
    return redirect('/openapi')

# LOGIN SERVICE redirect


@app.post('/user', tags=[api_gateway])
def redirect_create_user(body: UserServiceCreateBodySchema):
    '''
        Redirects to user service create user route, check user service swagger for more details
    '''
    json = {"username": body.username, "password": body.password}
    response = requests.post(
        f'{LOGIN_SERVICE_URL}/user', json=json)
    try:
        return response.text, response.status_code
    except Exception as e:
        print(e)
        error_message = f'{e}'
        return {"message": error_message}, response.status_code


@app.post('/user/login', tags=[api_gateway])
def redirect_login(body: UserServiceCreateBodySchema):
    '''
        Redirects to user service login route, check user service swagger for more details
    '''
    json = {"username": body.username, "password": body.password}
    response = requests.post(
        f'{LOGIN_SERVICE_URL}/user/login', json=json)
    try:
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code


@app.get('/user/is-authenticated', tags=[api_gateway])
def redirect_user_is_authenticated(header: HeaderSchema):
    '''
        Redirects to user service is authenticated route, check user service swagger for more details
    '''
    response = requests.get(
        f'{LOGIN_SERVICE_URL}/user/is-authenticated', headers=transform_authorization_header(header))
    try:
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code


@app.put('/user', tags=[api_gateway])
def redirect_update_user(header: HeaderSchema, body: UserServiceCreateBodySchema):
    """
        Redirects to user service update user route, check user service swagger for more details
    """
    json = {"username": body.username, "password": body.password}
    response = requests.put(
        f'{LOGIN_SERVICE_URL}/user', headers=transform_authorization_header(header), json=json)

    try:
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code


@app.delete('/user', tags=[api_gateway])
def redirect_delete_user(header: HeaderSchema):
    """
        Redirects to user service update user route, check user service swagger for more details
    """
    response = requests.delete(
        f'{LOGIN_SERVICE_URL}/user', headers=transform_authorization_header(header))
    try:
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code

# PRODUCT SERVICE redirect

# public routes


@app.get('/product', tags=[api_gateway])
def redirect_get_product():
    """
        Redirects to product service get product route, check user service swagger for more details
    """
    response = requests.get(
        f'{PRODUCT_SERVICE_URL}/product',)
    try:
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code


@app.get('/product/<int:product_id>', tags=[api_gateway])
def redirect_get_product_id(path: ProductServiceProductPathSchema):
    """
        Redirects to product service get product by id route, check user service swagger for more details
    """
    response = requests.get(
        f'{PRODUCT_SERVICE_URL}/product/{path.product_id}',)
    try:
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code


@app.get('/product/search', tags=[api_gateway])
def redirect_search_product(query: ProductServiceSearchSchema):
    """
        Redirects to product service get product route, check user service swagger for more details
    """
    if not query or not query.name:
        return {"message": 'missing query parameter "name"'}, 400

    response = requests.get(
        f'{PRODUCT_SERVICE_URL}/product/search?name={query.name}',)
    try:
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code


@app.post('/product/order', tags=[api_gateway])
def redirect_order_product(body: ProductServiceCreateOrderSchema):
    """
        Redirects to product service create order route, check user service swagger for more details
    """
    json = {
        "user_email": body.user_email,
        "total_price": body.total_price,
        "date": body.date,
        "order_products": body.order_products
    }
    response = requests.post(
        f'{PRODUCT_SERVICE_URL}/order', json=json)
    try:
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code


# private routes
@app.post('/product', tags=[api_gateway])
def redirect_create_product(body: ProductServiceCreateProductSchema, header: HeaderSchema):
    """
         Redirects to product service create product route, check user service swagger for more details
    """
    logged_in = redirect_user_is_authenticated(header)
    if logged_in['status_code'] != 200:
        return {'message': 'Unauthorized'}, 401

    json = {
        "name": body.name,
        "description": body.description,
        "amount": body.amount,
        "image": body.image,
        "weight": body.weight,
        "price": body.price,
    }
    response = requests.post(
        f'{PRODUCT_SERVICE_URL}/product', json=json)
    try:
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code


@app.put('/product/<int:product_id>', tags=[api_gateway])
def redirect_update_product(body: ProductServiceCreateProductSchema, header: HeaderSchema, path: ProductServiceProductPathSchema):
    """
         Redirects to product service update product route, check user service swagger for more details
    """
    logged_in = redirect_user_is_authenticated(header)
    if logged_in['status_code'] != 200:
        return {'message': 'Unauthorized'}, 401

    json = {
        "name": body.name,
        "description": body.description,
        "amount": body.amount,
        "image": body.image,
        "weight": body.weight,
        "price": body.price,
    }
    try:
        response = requests.post(
            f'{PRODUCT_SERVICE_URL}//product/{path.product_id}', json=json)
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code


@app.delete('/product/<int:product_id>', tags=[api_gateway])
def redirect_delete_product(path: ProductServiceProductPathSchema, header: HeaderSchema):
    """
        Redirects to product service delete product by id route, check user service swagger for more details
    """
    logged_in = redirect_user_is_authenticated(header)
    if logged_in['status_code'] != 200:
        return {'message': 'Unauthorized'}, 401

    response = requests.get(
        f'{PRODUCT_SERVICE_URL}/product/{path.product_id}',)
    try:
        return response.text, response.status_code
    except Exception as e:
        error_message = f'{e}'
        return {"message": error_message}, response.status_code
