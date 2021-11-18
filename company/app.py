from bottle import run, get, view, post, request

##############################
@get("/")
@view("index.html")
def do():
    return dict(company_name = "SUPER")
##############################
@post("get/-name-by-cpr")
def do():
    print(request.body)
    data_from_client = request.json
    print(data_from_client)
    # connect to sql/db/document query
    return "message"

##############################
run(host="127.0.0.1", port=4444, debug=True, reloader=True, server="paste")

