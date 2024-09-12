# Sojo Industries WeatherAPI Task
_By Kamal Qarain on 12 September 2024 for Sojo Industries_

---

## About
A simple Python FastAPI application with two main endpoints:
* Health Check
  * _Returns an "OK" response (to check if application is deployed correctly)_
* Current Weather 
   * _Uses the [WeatherAPI](https://www.weatherapi.com/) as its data source_

---

## Setup
Place a valid WeatherAPI key in the [`.env`](.env) file, for example:
```dotenv
WEATHER_API_KEY=123456....
```
---

## Local Deployment
You may run the application via Docker or directly on the host machine

### **Option A** - Deploy via Docker _(Recommended)_
1. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Run Docker Compose
   ```shell
   docker-compose up
   ```

### **Option B** - Deploy Directly on Host System
1. Download and install [Python 3.11](https://www.python.org/downloads/release/python-3110/)
2. Create and activate a [Python virtual environment (venv)](https://python.land/virtual-environments/virtualenv)
3. Install project dependencies inside the venv
    ```shell
    pip install -r requirements.txt
   ```
4. Start the API server
   ```shell
   python main.py
   ```
---

## Usage

Make an HTTP `GET` request and provide a location as a query parameter, for example: `/weather?city=London`

_The full API documentation can be accessed locally via http://localhost:8000/docs_

---

## Contributing
The code should generally be well-documented with clear variable names, type hints, and docstrings and comments throughout.

Contributions and suggestions are greatly welcomed. Feel free to **clone**, **fork**, or open a **pull request**.

In case there are any questions, please do not hesitate to contact via email [kamalq97@gmail.com](mailto:kamalq97@gmail.com)
