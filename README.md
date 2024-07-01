# Project_Management_API
**Developed By: Yogesh Jagtap**
## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x
- Django 3.x
- Django REST Framework
- POSTMAN for API Testing

## Installation

1. Clone the repository:
    bash
    git clone https://github.com/DevPyYogesh/Project_Management_API.git
    cd your-repository-name
    

2. Create a virtual environment and activate it:
    bash
    python -m venv env
    source env/bin/activate
    

3. Install the dependencies:
    bash
    pip install -r requirements.txt
    

4. Apply migrations:
    bash
    python manage.py migrate
    

5. Create a superuser to access the admin interface:
    bash
    python manage.py createsuperuser
    

6. Run the development server:
    bash
    python manage.py runserver
    

## Usage

- Access the admin interface at `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.
- Use the provided API endpoints to interact with the application.

## API Endpoints

### Clients

- List all clients
  - GET `/clients/`
  - Example Response:
    json
    [
        {
            "id": 1,
            "client_name": "Company A",
            "created_at": "2024-07-01T04:37:27.971519Z",
            "created_by": "user@example.com"
        },
        
    ]
    

- **Retrieve client details**
  - GET `/clients/{id}/`
  - Example Response:
    json
    {
        "id": 1,
        "client_name": "Company A",
        "projects": [
            {
                "id": 1,
                "name": "Project A"
            },
            
        ],
        "created_at": "2024-07-01T04:37:27.971519Z",
        "created_by": "user@example.com"
    }
    

- Create a new client
  - POST `/clients/`
  - Example Request:
    json
    {
        "client_name": "Company B",
        "created_by": "user@example.com"
    }
    

### Projects

- List all projects assigned to the logged-in user
  - GET `/projects/`
  - Example Response:
    json
    [
        {
            "id": 1,
            "project_name": "Project A",
            "created_at": "2024-07-01T04:37:27.971519Z",
            "created_by": "user@example.com"
        },
        
    ]
    

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes,
please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT Lice

## Contact

Yogesh Jagtap - [yj.yogeshjagtap@gmail.com](mailto:yj.yogeshjagtap@gmail.com)

Project Link: [https://github.com/DevPyYogesh/Project_Management_API.git](https://github.com/DevPyYogesh/Project_Management_API.git)
