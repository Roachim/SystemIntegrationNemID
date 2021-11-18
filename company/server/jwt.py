from bottle import run, get, view, post, request, route
import requests
import jwt
url = 'https://fatsms.com/send-sms'
phoneNumber = "53447600"
APIKey = 'fe8f0664-f2ac-40fa-bf91-b4506ecf3d90'
the_secret = 'jwt-secret-key'

##############################
@view("index.html")
def do():
    return dict(company_name = "SUPER")

##############################
@route("/hello")
def Hello():
    return "hello world"
##############################
@post("jwt-token")
def do():
    print(request.body)
    data_from_client = request.json
    
    decoded_message = jwt.decode(data_from_client, the_secret)
    # connect to sql/db/document query
    return decoded_message

##############################
@get("sendSMS")
def do():
    sms = {'to-phone': '53447600', 
    'message': "hello", 
    'api_key':'fe8f0664-f2ac-40fa-bf91-b4506ecf3d90'}

    x = requests.post(url, data = sms)
    return x.text

##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")

