import json
import re,random,os
from flask import render_template,request,redirect,flash,make_response,session,url_for
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash,check_password_hash
from errandapp import app, csrf
from errandapp.models import db,Admin

from errandapp.forms import Signup,Loginform,Updateform

       
       
# @app.route("/admin/login", methods=['POST','GET'])
# def admin_login():
#     login=Loginform()
#     if request.method=='GET':
#         return render_template("admin/login.html",log=login)
#     else:#retrieving the form data
#         email=request.form['email']
#         password=request.form['password'] #or password
#         chk=db.session.query(Admin).filter(Admin.email==email, Admin.password==password)
#         if chk:
#             return redirect("/admin/dashboard")
#         else:
#             return redirect("/admin/login")


# @app.route("/admin/dashboard", methods=["GET","POST"])
# def admin_dashboard():
#     if request.method=="GET":
#         return render_template("admin/dashboard.html")
#     else:
        # return render_template("admin/dashboard.html")


















# from flask import render_template,request,redirect,flash,make_response,session

# from errandapp import app

# @app.route('/profile')
# def profile():
#     session['firstname']='segun'
#     return "welcome!"

# #to delete a session use session.pop('firstname',None)




# #cookies 
# @app.route("/tour", methods=['POST','GET'])
# def tour():
#     if request.method=="GET":
#         return render_template('admin/tour.html')

#     else:
#        continent=request.form.get("continent")
#        rsp= make_response(redirect('/shop'))
#        rsp.set_cookie('destination', continent)
#        return rsp







# '''to retrieve data from post, we use: request.form.get('fieldname') or reuest.get('fillename')'''

# #when you search for something
# @app.route("/shop")
# def shop():

#     dest=request.cookies.get('destination')
#     # c=request.cookies.get('country')
#     # return c
#     return render_template("admin/searchform.html", dest=dest)

# @app.route("/search")
# def sear():
#     data=request.args['s'] #s represent the name given to the input used mostly for search 
#     menu=request.args.getlist('food')
#     # return f"you are looking for...{data}"
#     return render_template('slow.html', menu=menu)

    


# @app.route("/admin/products")
# def products():
#     return render_template("admin/products.html")

# @app.route("/admin/authenticate", methods=['POST'])
# def authenticate():
#     name=request.form['username']
#     password=request.form['password'] #or password
#     if name=="" or password=="":
#         return "fill the form"
#     else:
#         with open('registration.txt', 'a') as file:
#             file.write(f"your name is {name} \r\n")
#         return f"welcome {name}!"




# @app.route("/admin/login", methods=['POST','GET'])
# def admin_login():
#     if request.method=='GET':
#         return render_template("admin/login.html")
#     else:#retrieving the form data
#         name=request.form['username']
#         password=request.form['password'] #or password
#         if name=="":
#            flash('please complete the form', category='error')
#         else:
#             with open('registration.txt', 'a') as file:
#                 file.write(f"your name is {name} \r\n")
#                 flash( "registration was successful", category='success')
#                 flash( "welcome", category='success')
#             # return f"welcome {name}"
#         return redirect("/")


# @app.route('/')
# def home():
#     users=["atiku","bat","peter"]
#     return render_template('index.html',userlist=users,pagename="home page")
        

# @app.route("/admin/dashboard")
# def dashboard():
#     message="welcome admin! you can view all the users"
#     return render_template("admin/dashboard.html", message=message)


# @app.route("/admin/list/users")
# def listusers():
#     users=['ada','collins', 'noel', 'chinwe', 'kareem']
#     return render_template("admin/user.html", users=users)



# @app.errorhandler(404)
# def notfound(error):
#     # return "sorry, the page your are trying to vist does not exist."
#     return render_template("admin/404.html", error=error),404

# @app.errorhandler(500)
# def programmingerror(error):
#     return "sorry, something went wrong.",505
#     # return render_template("admin/404.html", error=error)


'''end of admin routes'''



# @app.route('/free/')
# def free():
#        team = {'CEO' : 'Alhaji Dangote',  'Secretary' : 'Mayor Olu', 
#                'President' : 'Prof Yemi' ,  'Chairman': 'Bola Tinubu', 
#                'HR Manager' : 'Miss Ada' }
#        return render_template('assign.html', userlist=team)










# @app.route("/aboutus")
# def about():
#     return render_template('about.html')

# @app.route("/contact/")
# def contact():
#     return render_template('contact.html')





# def home():
#     return render_template('index.html')


#trailing slash
# @app.route("/contact/")
# def contact():
#     return "<h1>contact us from here</h1>"
# def home():
#     return render_template('index.html')

# dynamic route
# @app.route("/users/<int:userid>/") #can help us change the parameter to be supply
# def showusers(userid):
#     return f"the details of our user {userid} will be here"

