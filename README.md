# BookMind AI 📚✨

BookMind AI is a full-stack web application that provides book summaries and intelligent recommendations through a clean interactive dashboard.

## Live Demo

Frontend: https://bookmind-ai.vercel.app
Backend API: https://bookmind-ai.onrender.com/api/books/

---

## Features

* Browse available books
* View AI-style book summaries
* Get recommendation suggestions
* Search books instantly
* Responsive modern UI

---

## Tech Stack

### Frontend

* React
* Vite
* Tailwind CSS

### Backend

* Django
* Django REST Framework

### Deployment

* Frontend: Vercel
* Backend: Render

---

## Project Structure

bookmind-ai/
├── frontend/
├── backend/

---

## API Endpoint

GET /api/books/

Returns all available books with:

* title
* author
* summary
* recommendations

---

## Sample Books Included

* Atomic Habits
* Deep Work

---

## Setup Locally

### Frontend

cd frontend
npm install
npm run dev

### Backend

cd backend
pip install -r requirements.txt
python manage.py runserver

---

## Author

Built by [Aditi Raj]

---

## Future Improvements

* Add authentication
* AI-generated summaries using LLM APIs
* Book categories
* User favorites
