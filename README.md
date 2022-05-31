# Moscow-Time

### About The Project

Done by: Daniil Shilintsev 
Group: MS21-02

### Built With

Django python framework  
- It enables fast development of maintainable and secure websites
- Server automatically restarts when file is changed
- Good debugging tools
- Logging is already set up

## Getting Started - Lab 1 

To get a local copy up and running follow these simple steps.

### Prerequisites 

* Ensure you have python3 by running the following command
  ```sh
  python3 --version
  ```
* Install the virtual environment
  ```sh
  sudo apt install -y python3-venv
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Danilum/DevOpsCourseLabs.git
   ```
2. Enter the working directory
   ```sh
   cd DevOpsCourseLabs
   
   cd app_python
   ```
3. Create the virtual environment
   ```sh
   python3 -m venv .venv
   ```
4. Activate the virtual environment
   ```sh
   source .venv/bin/activate
   ```
5. Use pip to install Django
   ```sh
   python3 -m pip install django~=4.0.0
   ```
6. Finally run the application and view it on your browser
   ```sh
   python3 manage.py runserver
   ```

## Getting Started - Lab 2 

To get the Docker image up and running follow these simple steps.

### Prerequisites 

* Ensure you have docker by running the following command
  ```sh
  sudo docker run hello-world
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Danilum/DevOpsCourseLabs.git
   ```
2. Enter the working directory
   ```sh
   cd DevOpsCourseLabs
   
   cd app_python
   ```
3. Create the virtual environment
   ```sh
   python3 -m venv .venv
   ```
4. Activate the virtual environment
   ```sh
   source .venv/bin/activate
   ```
5. In your new environment, you can run directly from docker hub    
   ```sh
   docker run -p 8000:8000 danilkadocker99/moscow_app
   ```  
6. Finally open to view on your browser at http://0.0.0.0:8000/ 



## Contact

Email: [innopolis email](mailto:d.shilintsev@innopolis.ru)
