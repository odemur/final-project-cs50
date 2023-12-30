# Real State System
#### Video Demo: <https://www.youtube.com/watch?v=jCCZrC1D988>
#### Description: This was my final project for conclude the CS50 Introduction to Computer Science.

## Technologies 
- Python 3
- JavaScript
- Vue.js
- Tailwind CSS
- SQLite 3

## How it works 

You can run this app following the instructions bellow. 

First install and run Python application: 

### Backend:
In backend folder run: 
```bash
pip3 install Flask Flask-SQLAlchemy Flask-Migrate flask-cors
```
And 

```bash
export FLASK_ENV=development
```
And start the application:

```bash
python3 main.py
```

### You can access the API endpoint at this address:
http://127.0.0.1:5000

### Frontend:
In frontend folder run: 
```bash
npm install
```

And run: 
```bash
npm run serve
```

### Open the URL in your browser:
<http://localhost:8080>

## Project structure 
```bash
real-estate/
│
├── backend/
│   ├── app/
│   │   ├── config.py
│   │   ├── models/
│   │   │   ├── property.py
│   │   ├── repositories/
│   │   │   ├── property_repository.py
│   │   ├── services/
│   │   │   ├── property_service.py
│   │   ├── tests/
│   │   │   ├── test_integration.py
│   │   │   ├── test_models.py
│   │   │   ├── test_repositories.py
│   │   │   ├── test_services.py
│   ├── instance/
│   │   ├── real_state.db
│   ├── tests/
│   │   ├── test_integration.py
│   │   ├── test_models.py
│   │   ├── test_repositories.py
│   ├── main.py
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── AppFooter.vue
│   │   │   ├── AppHeader.vue
│   │   ├── router/
│   │   │   ├── index.js
│   │   ├── services/
│   │   │   ├── api.js
│   │   ├── views/
│   │   │   ├── AddProperty.vue
│   │   │   ├── ExportProperties.vue
│   │   │   ├── ListProperties.vue
│   │   ├── App.vue
│   │   ├── index.css
│   │   ├── main.js
│   │ .gitignore
│   │ babel.config.js
│   │ jsconfig.json
│   │ package.json
│   │ postcss.config.js
│   │ README.md
│   │ tailwind.config.js
│   │ vue.config.js
├── README.md
```

## About CS50
CS50 is a openware course from **Havard University**.

Introduction to the intellectual enterprises of computer science and the art of programming. 

This course is about software engineering and teaches students how to think algorithmically and solve problems using abstraction, algorithms, data structures, encapsulation, resource management, and security. 

Languages include Python, SQL, HTML, CSS, and JavaScript (for web applications).

**Thank you for all CS50.**
