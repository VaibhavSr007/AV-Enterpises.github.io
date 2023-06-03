# Defence Dreamers

Welcome to the Defense Dreamers Website repository! This project aims to provide a comprehensive platform for individuals preparing for defense exams and SSB (Services Selection Board) interviews. The website offers a wide range of features, including an exam preparation guide, SSB interview preparation material, success stories and strategies from successful candidates, a contact form for sending doubts to the experts, a chatbot extension for clearing doubts, and a community chat feature where aspirants can seek and provide assistance to each other.


## Features

- Community Chat service
- Chatbot Intergration for exclusive doubt clearing
- Exam Preparation Guide and Resources
- SSB Interview Preparation Material
- Success Stories and Strategies of successful candidates.
- Exclusive defence knowledge section by experienced candidates in forces
- Contact Form for questions suggestions and other.


## Installation

 Clone this repository to your local machine using the following command:
```bash
  git clone https://github.com/VaibhavSr007/Defence-Dreamers.github.io.git
```

Install the necessary dependencies and libraries required for the website to function properly:
```bash
  pip insatll django
```

The project uses SQLite as the database backend by default. The necessary database file will be created automatically when running migrations. Run the following commands to apply the initial migrations:
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```

Create a superuser account to access the Django admin interface. Execute the following command and provide the required information:
```bash
  python manage.py createsuperuser
```

Start the Django development server with the following command:
```bash
  python manage.py runserver
```

Open your web browser and navigate to http://localhost:8000 to access the website locally. The admin interface is available at http://localhost:8000/admin/.


## Tech Stack

- HTML 
- CSS with Bootstrap
- JavaScript
- Python with Django
- SQL lite for Database
- AWS for deployment


## Screenshots

![App Screenshot](https://github.com/VaibhavSr007/static/1.png?raw=true)
![App Screenshot](https://github.com/VaibhavSr007/static/2.png?raw=true)
![App Screenshot](https://github.com/VaibhavSr007/static/4.png?raw=true)
![App Screenshot](https://github.com/VaibhavSr007/static/5.png?raw=true)
![App Screenshot](https://github.com/VaibhavSr007/static/7.png?raw=true)


## Demo

Demo Video Link

https://github.com/VaibhavSr007/static/1.png?raw=true


## Deployment

The Deployment of project is done on AWS through EC2 (Elastic Cloud Compute):

http://13.200.86.46:8000

