




  <h3 align="center">weather</h3>

  <p align="center">
register and login user and get user info </p>   <br/>





<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project get a city name and return temperature.

This project will do:
* Create a mysql database
* create a super user 
* run project (python manage.py runserver)
* type in browser 127.0.0.1:8000/weather-api/city_name


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](https://www.python.org)
* [Django](https://django.com)
* [Mysql DB](https://www.mysqldb.com)
* [redis](https://www.redis.com)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In this part, there is an instructions on setting up the project locally.
To get a local copy up and running follow these simple steps.

### Prerequisites

For this project, you need python v3.8 and mongodb v5[Install Mysqldb](https://dev.to/sm0ke/how-to-use-mysql-with-django-for-beginners-2ni0/)

### Installation

After installing prerequisites, now you can install dependencies of this project:

1. Clone the repo
   ```sh
   git clone https://github.com/fatemehkhosravy67/WEATHER_API.git
   ```
2. Setup an environment
    ```sh
    sudo apt install python3-virtualenv
    virtualenv venv
    source venv/bin/activate
    ```
3. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```
4. Create your mysql User and Database and set it in settings.py
   ```buildoutcfg
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your database name',
        'USER': 'your user',
        'PASSWORD': 'your database password',
        'HOST': 'localhost',
        'PORT': '3306',
    }}
   ```
5. Migrate 
    ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To run the project, make sure that the mysqldb service is up locally and run this in the app directory
```sh
python manage.py runserver
```
- You can visit [localhost:8000/weather-api/city_name](http://localhost:8000/weather-api/city_name) for get city weather info. 

<p align="right">(<a href="#top">back to top</a>)</p>










