from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .controllers import register_routes
from .logging_ import configure_logging, LogLevels


configure_logging(LogLevels.info)

app = FastAPI(
    debug=True,
    title="Nexus",
    description="",
    summary="",
    #contact={
        #"name": "",
        #"url": "",
        #"email": "",
    #},
    license_info={
        "name": "",
        "identifier": "MIT",
    },
    # openapi_tags=[
    #     {"name": "Users", "description": "User Management", "endpoints": [
    #         {"operationId": "getUsers", "summary": "Get Users"},
    #         {"operationId": "createUser", "summary": "Create User"},
    #         {"operationId": "getUserById", "summary": "Get User By Id"},
    #         {"operationId": "replaceUserById", "summary": "Replace User By Id"},
    #         {"operationId": "updateUserById", "summary": "Update User By Id"},
    #         {"operationId": "deleteUserById", "summary": "Delete User By Id"},
    #     ]},
    #     {"name": "Authorizations", "description": "Authorizations", "endpoints": [
    #         {"operationId": "register", "summary": "Register"},
    #         {"operationId": "login", "summary": "Login"},
    #         {"operationId": "logout", "summary": "Logout"},
    #         {"operationId": "token", "summary": "Token"},
    #     ]}
    # ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1:8000", "http://127.0.0.1:8002"],  # Allow localhost and 127.0.0.1 with any port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_routes(app)
