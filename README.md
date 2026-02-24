# E-Vuriro Platform

An integrated multilingual telemedicine and digital health platform for remote healthcare delivery, video consultations, electronic medical records, prescription management, and AI-enabled clinical support.

## Features

- **User Authentication**: Role-based access for patients, doctors, and admins
- **Video Consultations**: Real-time video calls using WebRTC
- **Electronic Health Records (EHR)**: Comprehensive patient medical history
- **Digital Prescriptions**: PDF generation and management
- **AI Services**: Symptom checking, transcription, drug interaction analysis
- **Multilingual Support**: English, French, Kinyarwanda
- **Appointment Scheduling**: Calendar-based booking system

## Tech Stack

- **Backend**: Django REST Framework, PostgreSQL, Redis, Channels
- **Frontend**: React, TypeScript, Redux Toolkit, Vite
- **AI Service**: FastAPI, Whisper, NLP models
- **Deployment**: Docker, Docker Compose, Nginx

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and configure
3. Run `docker-compose up --build`
4. Access the application at http://localhost

## API Documentation

Available at `/api/docs` when running the backend.

## License

This project is licensed under the MIT License.