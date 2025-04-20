# Hello Professor!

# Homework 10 – 

Event Manager Company: User Management REST API

Welcome to my submission for Assignment 10. This repository showcases my contributions as a Software QA Analyst/Developer Intern at the Event Manager Company. My primary focus was on building and improving a secure RESTful API that leverages OAuth2 authentication using JWTs. This API forms the core foundation for managing user-related operations, upon which modules like event registration and administration will be developed in the future.

# Project Summary

# 1. Setup Instructions

Step 1: Fork the professor’s GitHub repository to your own GitHub account.

Step 2: Clone the forked repository to your local system using:

git clone https://github.com/Bharath-k-11/Homework-10.git

Step 3: Start the application using Docker:

docker compose up --build
2
Step 4: Access the interactive API documentation via Swagger UI at:
<img width="1012" alt="Screenshot 2025-04-19 at 8 19 16 PM" src="https://github.com/user-attachments/assets/c4a70753-33d0-4ac7-86b4-5206c4e9b0bc" />

<img width="1012" alt="Screenshot 2025-04-19 at 8 19 34 PM" src="https://github.com/user-attachments/assets/6e71db74-fcd8-4503-924d-c236d24b31b4" />


http://localhost/docs

Step 5: Access PGAdmin by navigating to:

http://localhost:5050

<img width="1012" alt="Screenshot 2025-04-19 at 8 19 53 PM" src="https://github.com/user-attachments/assets/19432773-bfa1-4eba-9340-d0a0bb9ceb18" />

# 2. Database Migration Process

Open PGAdmin at localhost:5050.

Add a new server with the following configuration:

Server Name: myserver

Host: postgres

Port: 5432

Database: myappdb

Username/Password: your credentials

Save the server configuration.

Navigate to the project directory in your terminal and run:

docker compose exec fastapi alembic upgrade head

# 3. Issues Resolved

1. JWT access token expires

What Was Fixed:

When a JWT access token expires, the API was previously: Throwing an unhandled exception or generic 500 error.

🔗 https://github.com/Bharath-k-11/Homework-10/issues/1#issue-2997892779 — 1-jwt-access-token-expires

2. Token request issue

Description

Currently, when requesting a JWT token (via login or other authentication methods), the API doesn't handle various edge cases properly.

Users may experience unexpected behavior such as:

Missing or incorrect credentials.

Server errors or unhandled exceptions.

Unclear or generic error messages.

The goal is to improve error handling and ensure that requests for tokens fail gracefully with clear, actionable error messages.

🔗 https://github.com/Bharath-k-11/Homework-10/issues/2#issue-2997904602 — token request issue

3. password logic

The application currently doesn't handle password request failures properly. When users request a password reset or attempt to recover their password, they might encounter the following issues:

Missing or invalid data (e.g., incorrect email).

Failure to validate the request before proceeding.

Unclear error messages or lack of meaningful feedback for the user.

We need to improve error handling and provide users with clear, actionable error messages when their password request fails.

🔗 https://github.com/Bharath-k-11/Homework-10/issues/3#issue-2997922030 — tests/conftest.py

4. login page

Currently, the login page has limited validation and poor error feedback when incorrect credentials are submitted. Users are either not informed clearly, or receive a generic error that makes debugging or understanding the problem difficult.

We need to:

Improve the validation and error handling during login.

Ensure clear, actionable error messages are returned.

Protect the API from leaking unnecessary info (like whether an email exists).

🔗 https://github.com/Bharath-k-11/Homework-10/issues/4#issue-2997953169 — https://github.com/Bharath-k-11/Homework-10/tree/4-login-page

5. URL validation

Currently, the application does not validate whether a submitted string (e.g., for profile links, social URLs, or website fields) is a valid URL format. This can result in:

Invalid links being stored in the database.

Broken redirections or UI errors when rendering those URLs.

🔗 https://github.com/Bharath-k-11/Homework-10/issues/5#issue-2997967927 — .github/workflows/production.yml

#4. Docker Hub Deployment

Deployment was configured and tested successfully via Docker Compose.

<img width="1440" alt="Screenshot 2025-04-19 at 8 29 44 PM" src="https://github.com/user-attachments/assets/77aea7d1-2e35-43f4-bf8c-d387be7a4923" />

<img width="1440" alt="Screenshot 2025-04-19 at 8 30 46 PM" src="https://github.com/user-attachments/assets/d94bc01c-936d-4283-a1ed-1c463a401e2f" />




# 5. Testing Instructions

Run the entire test suite using:

docker compose exec fastapi pytest

Run a specific test file using:

docker compose exec fastapi pytest path/to/test_file.py

# 6. Code Coverage

Generate coverage reports by executing:

docker compose exec fastapi pytest --cov

# Project Outcomes & Reflections

This assignment was an intensive and rewarding experience. The initial phase required a steep learning curve to fully understand the expected flow of the system and integrate new features effectively. Throughout development, I tackled various issues such as inconsistent example values, missing validations for URLs and passwords, incomplete email verification workflows, and inadequate login error feedback.

I addressed these by:

Standardizing example data for Swagger.

Adding robust input validation.

Improving error message clarity.

Securing endpoints using proper authorization.

Refactoring authentication to use JWT-based OAuth2.

Structuring the database using Alembic migrations.

Achieving 90% test coverage through comprehensive test cases.

Successfully configuring a CI/CD pipeline using Docker and GitHub Actions.
