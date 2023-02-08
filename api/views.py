import os

#django
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#forms
from .forms import NewUserForm

#views
from django.views import generic

# Create your views here.
def index(request):
    index_data = "This is Index page! This Page is under construction !!!"
    print(index_data)
    context={'index_data': index_data}
    # return HttpResponse("Hello World!")
    return render(request, 'api/index.html',context)

def signup_request(request):
	if request.method == "POST":
		signup_data = NewUserForm(request.POST)
		if signup_data.is_valid():
			user = signup_data.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("api:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	signup_data = NewUserForm()
	return render (request=request, template_name="api/signup.html", context={"signup_data":signup_data})

def login_request(request):
	if request.method == "POST":
		login_data = AuthenticationForm(request, data=request.POST)
		if login_data.is_valid():
			username = login_data.cleaned_data.get('username')
			password = login_data.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("api:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	login_data = AuthenticationForm()
	return render(request=request, template_name="api/login.html", context={"login_form":login_data})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("api:index")

def profile(request):
    profile_data = "This is Index page! This Page is under construction !!!"
    print(profile_data)
    context={'profile_data': profile_data}
    # return HttpResponse("This is profile page! This Page is under construction !!!")
    return render(request, 'api/profile.html',context)

def about(request):
    about_data = "This is About page! This Page is under construction !!!"
    print(about_data)
    context={'about_data': about_data}
    # return HttpResponse("This is profile page! This Page is under construction !!!")
    return render(request, 'api/about.html',context)

def service(request):
    service_data = "This is Service page! This Page is under construction !!!"
    print(service_data)
    context={'service_data': service_data}
    # return HttpResponse("This is profile page! This Page is under construction !!!")
    return render(request, 'api/service.html',context)

def project(request):
    project_data = "This is Project page! This Page is under construction !!!"
    print(project_data)
    context={'project_data': project_data}
    # return HttpResponse("This is profile page! This Page is under construction !!!")
    return render(request, 'api/project.html',context)

def feature(request):
    feature_data = "This is Feature page! This Page is under construction !!!"
    print(feature_data)
    context={'feature_data': feature_data}
    # return HttpResponse("This is profile page! This Page is under construction !!!")
    return render(request, 'api/feature.html',context)

def support(request):
    support_data = "This is support page! This Page is under construction !!!"
    print(support_data)
    context={'support_data': support_data}
    # return HttpResponse("This is profile page! This Page is under construction !!!")
    return render(request, 'api/support.html',context)

def terms(request):
    terms_data = "This is terms and conditions page! This Page is under construction !!!"
    print(terms_data)
    context={'terms_data': terms_data}
    # return HttpResponse("This is profile page! This Page is under construction !!!")
    return render(request, 'api/terms.html',context)

def newsletter(request):
    newsletter_data = "This is newsletter page! This Page is under construction !!!"
    print(newsletter_data)
    context={'newsletter_data': newsletter_data}
    # return HttpResponse("This is profile page! This Page is under construction !!!")
    return render(request, 'api/newsletter.html',context)

def team(request):
    team_data = "This is our team page! This Page is under construction !!!"
    print(team_data)
    context={'team_data': team_data}
    # return HttpResponse("This is profile page! This Page is under construction !!!")
    return render(request, 'api/team.html',context)

def contact(request):
    contact_data = "This is contact page! This Page is under construction !!!"
    print(contact_data)
    context={'contact_data': contact_data}
    # return HttpResponse("This is profile page! This Page is under construction !!!")
    return render(request, 'api/contact.html',context)

###################################################################################################################################
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

def dashboard(request):
    return JsonResponse("Hello DJango!")

def home(request):
    home_data = "This is Home page! This Page is under construction !!!"
    print(home_data)
    context={'home_data': home_data}
    return JsonResponse(context)
    # return render(request, 'api/home.html',context)
    # return HttpResponse("This is Home page! This Page is under construction !!!")

###################################################################################################################################
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

# Return query result as dictionary
# def dictfetchall(cursor):
#     "Return all rows from a cursor as a dict"
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]