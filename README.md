This is a sample application to reurn a json with below forrmat with /info endpoint
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

## How To Setup
1. Clone This Project `git clone https://github.com/sajib1066/CurrencyConverterApp.git`
2. Create a Virtual Environment `virtualenv dockerenv`
3. Activate Virtual Environment `source dockerenv/bin/activate`
   Come back to application directory `source`
4. Install Requirements Package `pip install -r requirements.txt`
5. Finally Run The Project `python main.py`

Dockers Deployment:
new added