from flask_socketio import SocketIO,join_room,leave_room,send
import json
import re,random,os
from string import ascii_uppercase
from flask import render_template,request,redirect,flash,make_response,session,url_for
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash,check_password_hash
from errandapp import app, csrf
from errandapp.models import db,User,State,Lga,Task,Category

from errandapp.forms import Signup,Loginform,Updateform,Profileform


socketio=SocketIO(app)



@app.route("/chatting/<task_id>")
def chatting(task_id):

    useronline = session.get('userid') 
    userdeets = db.session.query(User).get(useronline) 
    return render_template("user/chatting.html", userdeets=userdeets)


@socketio.on('message') 
def handle_message(message):
    
     
    content={
        "name":session.get("userdeets"),         
        
    }

    print(f"recieved message {message}")
    send(message,broadcast=True)















# rooms={}

# def genderate_unique_code(length):
#     while True:
#         code=""
#         for _ in range(length):
#             code+=random.choice(ascii_uppercase)

#         if code not in rooms:
#                 break 
#     return code  

# @app.route('/home', methods=['POST','GET'])   
# def chat():

#     user=session.get('userid')
#     if request.method=="POST":
#         name=request.form.get('name')
#         code=request.form.get('code')
#         join=request.form.get('join',False)
#         create=request.form.get("create", False)

#         if not name:
#             room=session.get("room")
#             return render_template('user/home.html', error="please enter a name ", code=code, name=name,roomy=room,user=user)
        
#         if join !=False and not code:
#             room=session.get("room")
#             return render_template('user/home.html',  error="please enter a room code",code=code, name=name,roomy=room,user=user)
        
#         room = code
#         if create !=False:
#             room =genderate_unique_code(4)
#             rooms[room]={"members":0, "messages":[]}

#         elif code not in rooms:
#             room=session.get("room") 
#             return render_template("user/home.html", error="room does not exist",code=code, name=name,roomy=room,user=user)
        
#         session['room']=room
#         session['name']=name
#         session['code']=code
#         return redirect("/room")

#     return render_template('user/home.html')




# @app.route('/room', methods=['POST','GET'])   
# def room():
#     room=session.get("room")
#     if room is None or session.get('name') is None or room not in rooms:
#             return redirect("/home")

#     return render_template('user/room.html', code=room, messages=rooms[room]["messages"])

# @socketio.on("message")
# def message(data):
#     room= session.get("room")
#     if room not in rooms:
#         return
    
#     content={
#         "name":session.get("name"),
#         "message":data["data"]
#     }

#     send(content, to=room)
#     rooms[room]["messages"].append(content)
#     print(f"{session.get('name')} said: {data['data']}")
  

# @socketio.on("connect")
# def connect(auth):
#     room=session.get('room')
#     name=session.get('name')
#     if not name or not room:
#         return
#     if room not in rooms:
#         leave_room(room)
#         return 
    
#     join_room(room)
#     send({"name":name, "message": "has entered the room"}, to=room)
#     rooms[room]["members"]==1
#     print(f"{name} joined room {room}")



# @socketio.on("disconnect")
# def disconnect():
#     room=session.get("room")
#     name=session.get("name")   
#     leave_room(room) 

#     if room in rooms:
#         rooms[room]["members"] -=1
#         if rooms[room]["members"] <=0:
#             del rooms[room]

#     send({"name":name, "message": "has left the room"}, to=room)
#     print(f"{name} has left room {room}")

   



@app.route('/index/')
def index():
    return render_template('user/index.html')

@app.route('/signup/', methods=["POST","GET"])
def signup(): 
    if request.method=="GET":
        s=db.session.query(State).all()
        return render_template('user/signup.html', s=s)
    else:

        firstname=request.form.get('firstname')
        lastname=request.form.get('lastname')
        email=request.form.get('email')
        address=request.form.get('address')
        Dateofbirth=request.form.get('Dateofbirth')
        phonenumber=request.form.get('phonenumber')
        state=request.form.get("state")
        lga=request.form.get('lgas')
        gender=request.form.get('gender')
        password=request.form.get('password')
        c_password=request.form.get('confirmpassword')
        
        if firstname=="" or password=="" or  email=="" or  Dateofbirth=="" or  address=="" or  gender=="" :
            flash("All field(s) must be completed")
            s=db.session.query(State).all()
            return render_template("user/signup.html",s=s)
        
        elif  password != c_password:
            flash("password does not match")
           
            return render_template("user/signup.html")
        
        else:
            
            p=User(firstname=firstname,gender=gender,lga=lga,password=password,phonenumber=phonenumber,state=state,lastname=lastname,email=email,address=address,user_verification_status="1", Dateofbirth=Dateofbirth)
            db.session.add(p)
            db.session.commit()
            session['userid']=p.user_id
            session['user_loggedin']=True      
        return redirect("/profile/log")

@app.route("/aboutus")
def aboutus():
    return render_template("user/about.html")



@app.route('/login/',methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("user/login.html")
    else:
        email=request.form.get('email')
        password=request.form.get('password')  
        chk=db.session.query(User).filter(User.email==email,User.password==password).first()
        if chk:
            session['user_loggedin']=True
            session['userid']=chk.user_id
           
            return redirect("/dashboard/")
        
        elif email=="" or password=="":
            flash("kindly fill the form(s)")
            return render_template("user/login.html")

        else:
            return render_template("user/login.html")





@app.route("/dashboard/")
def dash():
    useronline = session.get('userid') 
    userdeets = db.session.query(User).get(useronline) 
    cats=db.session.query(Category).all()
    alltask=db.session.query(Task).all()

    return render_template("user/profile.html",  userdeets = userdeets,c=cats, alltask= alltask)


@app.route("/change", methods=["POST","GET"])
def change():
    useronline = session.get('userid') 
    userdeets = db.session.query(User).get(useronline)
    if request.method == "GET":  
        return render_template('user/profilechange.html',userdeets=userdeets)
    else:
        fullname = request.form.get('fullname')
        pix = request.files.get('pix')
        if pix !='':
            filename = pix.filename
            allowed =['.jpg','.png','.jpeg']
            name,ext = os.path.splitext(filename)
            newname = str(random.random()*1000000)+ext
            pix.save('errandapp/static/images/'+ newname)
            userdeets.firstname=fullname 
            userdeets.user_pix=newname 
            db.session.commit()
            return redirect("/dashboard/")
        else:
             return render_template('user/profilechange.html',userdeets=userdeets)

           
@app.route("/profile/log", methods=["GET","POST"] )
def userprofile():
    useronline = session.get('userid') 
    userdeets = db.session.query(User).get(useronline) 
    if request.method == "GET":  
        return render_template('user/profilechange.html',userdeets=userdeets)
    else:
        fullname = request.form.get('fullname')
        pix = request.files.get('pix')
        if pix !='':
            filename = pix.filename
            allowed =['.jpg','.png','.jpeg']
            name,ext = os.path.splitext(filename)
            newname = str(random.random()*1000000)+ext
            pix.save('errandapp/static/images/'+ newname)
            userdeets.firstname=fullname 
            userdeets.user_pix=newname 
            db.session.commit()
            return redirect("/dashboard/")
        else:
             return render_template('user/profilechange.html',userdeets=userdeets)





@app.route("/posttask", methods=["post","get"])
def post_task():
    useronline = session.get('userid') 
    userdeets = db.session.query(User).get(useronline)
  
    
    # alltask=db.session.query(Task).all()
    
    cats=db.session.query(Category).all()
    if request.method=="GET":
       
        return render_template("user/posttask.html",c=cats, userdeets=userdeets)
    else:
        # look=db.session.query(Task,Category).join(Category).all() 
        useronline = session.get('userid') 
       
        # data=db.session.query(Task.task_amount,Task.task_title,Category.cat_name,Task.description).join(Category).get(useronline)
        cat=request.form.get("category")  
        title=request.form.get('title')
        description=request.form.get('description')
        task_amount=request.form.get('task_amount')
        p=Task(task_title=title,description=description,task_posted_user=useronline,task_amount=task_amount, task_status="1", category_id=cat)
        db.session.add(p)
        db.session.commit()
       
        # return redirect("/dashboard/")
        # flash("comment sent")
        return render_template("user/profile.html",c=cats, userdeets=userdeets)#get request
       


       

@app.route("/getpost", methods=["POST","GET"])
def getcomments():
        useronline = session.get('userid') 
        data=db.session.query(Task,Category).join(Category).get(useronline)
        # data=db.session.query(Task,Category).join(Category).filter(Task.task_id).all()
        # data=Task.query.get(post_task)
        return render_template("user/profile.html", data=data)
        # return f"{data}"
   
   
  
   


@app.route('/delete/post/<task_id>')
def delete_post(task_id):
    #delete from post where id=postid
    d=Task.query.get(task_id)
    # d=db.session.query(Task).get(task_id)
    db.session.delete(d)
    db.session.commit()
    return redirect ("/dashboard/")
    # return f"{d}"


@app.route("/edit/post/<task_id>", methods=['POST','GET'])
def editpost(task_id):
    if request.method=='GET':
         #fect the post with the id post id and display to the user in an html page
        p=db.session.query(Task).get(task_id)
        cats=db.session.query(Category).all()
        return render_template("user/upload.html", p=p, c=cats)
    else:
        title=request.form.get('title') #new title from the form
        content=request.form.get('description')
        amount=request.form.get('amount')
        cat_name=request.form.get('cat_name')
        pp=Task.query.get(task_id)
        pp.task_title=title
        pp.description=content
        pp.task_amount=amount
        db.session.commit()
        flash("post has been updated")
        return redirect("/profile.log")
    



@app.route("/landing/")
def landing():
    code=session.get("code")
    name=session.get("name")
    useronline = session.get('userid') 
    userdeets = db.session.query(User).get(useronline)
    alltask=db.session.query(Task).all()
    return render_template("user/dashboard.html", userdeets=userdeets, alltask=alltask, code=code,name=name)
    
   

@app.route('/lga', methods=["GET","POST"])
def lga():
    #connect to db
    # real=db.session.query(State).all()
    s=db.session.query(State).all()
    return render_template("user/signup.html", s=s)

@app.route("/show_lga")
def show_lga():
    stateid=request.args.get('stateid')
    lgas=db.session.query(Lga).filter(Lga.state_id==stateid).all()
    toreturn=""
    for t in lgas:
        toreturn=toreturn + f'<option value="{t.lga_id}">' + t.lga_name + '</option>'
    return toreturn


@app.route("/grocery")
def grocery():
    return render_template("user/grocery.html")






@app.route("/handyservice")
def handyservice():
    return render_template("user/handyservice.html")





@app.route("/housecleaning")
def housecleaning():
    return render_template("user/housecleaning.html")


@app.route("/localbussiness")
def localbussiness():
    return render_template("user/localbussiness.html")





@app.route("/laundry")
def laundry():
    return render_template("user/laundry.html")

@app.route("/localshopping")
def localshopping():
    return render_template("user/localshopping.html")


@app.route("/ondemandshopping")
def ondemandshopping():
    return render_template("user/ondemandshopping.html")
