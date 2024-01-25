# FastMongoAuth
FastMongoAuth is a FastAPI-based authentication and user management system with MongoDB as the backend storage. It provides token-based authentication using JWT (JSON Web Tokens) and uses Pydantic for data validation.

Features
User Management: Allows user registration, login, logout, and profile updates.
JWT Authentication: Secure token-based authentication using JSON Web Tokens.
MongoDB Integration: Utilizes MongoDB as the database for storing user information.
FastAPI Powered: Built on top of the FastAPI framework for high performance and asynchronous support.

## Installation

1. Clone the repository:
  ```git clone https://github.com/your-username/FastMongoAuth.git```
2. Install the required dependencies:
   ```pip install -r requirements.txt```
3. Set up a MongoDB instance and update the .env file with the appropriate MongoDB connection URL.
4. Run the FastAPI application:
   ```uvicorn main:app --reload```
The application will be accessible at **http://127.0.0.1:8000**.

## Configuration
Configuration settings are managed through the .env file. Modify the values as needed for your environment.

- **app_name**: The name of your FastAPI application.
- **mongodb_url**: The connection URL for your MongoDB instance.
- **secret_key**: A secret key used for JWT token generation.

## API Endpoints
- **Create User: POST /users/** - Register a new user.
- **Login: POST /login** - Obtain a JWT token by providing valid credentials.
- **Logout: POST /logout** - Log out the current user and invalidate their token.
- **Update Profile: PUT /update_profile** - Update the profile of the currently logged-in user.
- **Get Current User: GET /current_user** - Retrieve information about the currently logged-in user.

## Authentication

**OAuth2 Password Flow**: The login endpoint uses OAuth2 password flow to authenticate users and issue JWT tokens.

## Dependencies

FastAPI
Pydantic
Motor (async MongoDB driver)
FastAPI Users
PyJWT
Passlib

## License

Copyright © [2024] [Craxti]

Licensed under the [MIT] License.
