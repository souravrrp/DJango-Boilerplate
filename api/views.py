import os
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import AddressForm

import dotenv
#database environment setup
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
db_user = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_dsn = os.environ["DB_DSN"]
db_lib_dir = os.environ["DB_LIB_DIR"]
db_name = os.environ["DB_NAME"]
db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]

# make dsn and create connection to db
# import cx_Oracle
# cx_Oracle.init_oracle_client(lib_dir=r"D:\Installed_Software\instantclient_11_2")
# dsn_tns = cx_Oracle.makedsn(db_host, db_port, db_name)
# oracon = cx_Oracle.connect(db_user, db_password, dsn_tns)
# print("cx_Oracle.version:", cx_Oracle.version)
# print("cx_Oracle.clientversion:", cx_Oracle.clientversion())

#Connect Oracle using sqlalchemy 
# from sqlalchemy import create_engine
# DIALECT = 'oracle'
# SQL_DRIVER = 'cx_oracle'
# ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + db_user + ':' + db_password +'@' + db_host + ':' + str(db_port) + '/?service_name=' + db_name
# sqlalchemy_engine = create_engine(ENGINE_PATH_WIN_AUTH)

# Return all rows from a cursor as a dict
# def dictfetchall(cursor):
#     "Return all rows from a cursor as a dict"
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def dashboard(request):
    return JsonResponse("Hello DJango!")

def login_view(request):
    context={}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(password)

        try:
            request.session['username'] = username.upper()
            request.session['password'] = password.upper()
            return redirect('api:home')

        except:
            messages.warning(request, "Username or Password is incorrect !")
        return JsonResponse(context)
    else:
        return JsonResponse(context)

def signup(request):
    signup_form=AddressForm
    context={'form': signup_form}
    return JsonResponse(context)

def profile(request):
    return HttpResponse("This is profile page! This Page is under construction !!!")

def home_view(request):
    home_data = "This is Home page! This Page is under construction !!!"
    print(home_data)
    context={'home_data': home_data}
    return JsonResponse(context)
    # return render(request, 'api/home.html',context)
    # return HttpResponse("This is Home page! This Page is under construction !!!")
