#Scope: This is a sample application to reurn a json with below forrmat with /info endpoint
{
    "service_name": "myapplication",
    "version: : "1.0.0",
    "git_commit_sha" : "abc57858585",
    "environment" : {
        "service_port": "8080",
        "log_vevel" : "INFO"
        }
     }

Application info:

# How To Build: Required Python 3.6 and Above
1. Clone This Project `git clone https://github.com/anz-ecp/manas1313.git`
2. Create a Virtual Environment `virtualenv dockerenv`
3. Activate Virtual Environment `source dockerenv/bin/activate`
   Come back to application directory `source`
4. Install Requirements Package `pip install -r requirements.txt`
5. Finally Run The Project `python main.py`

# How to Deploy: Dockers Image
# Prerequisites:
    - A non-root user with sudo privileges configured by following the Initial Server Setup with Ubuntu 18.04
    - One Ubuntu 18.04 server with Docker installed (DigitalOcean one-click Docker image)
    - Nginx installed in Ubuntu 18.04

# Steps to Deploy
    - create a directory and copy SampleDockerApp to location
    - Command to setup Docker Image 
        1. sudo bash start.sh
        2. sudo docker ps

