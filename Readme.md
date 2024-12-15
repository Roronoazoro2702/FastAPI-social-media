# Social Media API with FastAPI

A scalable social media API built with FastAPI, featuring user authentication, CRUD operations for posts, voting functionality, and Dockerized deployment.

## Features
- **User Authentication**: Secure login and registration with OAuth2 and JWT.
- **Posts Management**: Create, read, update, and delete posts.
- **Voting System**: Like/unlike posts with real-time vote counts.
- **Database**: PostgreSQL integration with Alembic for migrations.
- **Scalability**: Containerized using Docker and ready for production deployment.
- **CI/CD**: Automated integration and deployment pipelines.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Roronoazoro2702/FastAPI-social-media/tree/main
   cd FastAPI-social-media

2. Create a .env file with the required environment variables:

3. Build and run the application using Docker Compose:
   ```bash
   docker-compose -f Docker-compose-dev.yml up --build

## Tech Stack
- Framework: FastAPI
- Database: PostgreSQL
- Authentication: OAuth2 and JWT
- Containerization: Docker, Docker Compose
- CI/CD: GitHub Actions (or your preferred CI/CD tool)
