from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class User(db.Model):
    user_id=db.Column(db.Integer(), primary_key=True,autoincrement=True)
    firstname = db.Column(db.String(120), nullable=False)
    lastname= db.Column(db.String(120), nullable=False)
    email= db.Column(db.String(100), nullable=False) 
    address= db.Column(db.String(200), nullable=False) 
    gender=db.Column(db.String(20), nullable=False)
    state=db.Column(db.String(50), nullable=False)
    lga=db.Column(db.String(50), nullable=False)
    Dateofbirth=db.Column(db.DateTime(), default=datetime.utcnow)
    user_pix=db.Column(db.String(50), nullable=True)
    phonenumber=db.Column(db.String(20), nullable=False)
    password=db.Column(db.String(50), nullable=False)
    user_verification_status=db.Column(db.Enum('1','0'),nullable=False)
    reg_date=db.Column(db.DateTime(), default=datetime.utcnow)
     
    categories = db.relationship('Category', backref='caty_user')
    tasks = db.relationship('Task', backref='tasky_user')
    # from_user=db.relationship("Messages", foreign_keys="Messages.from_id", backref="fromuser")
    # to_user=db.relationship('Messages', foreign_keys="Messages.to_id",backhref="touser")


class Lga(db.Model):
    lga_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    state_id=db.Column(db.Integer(), db.ForeignKey('state.state_id'))
    lga_name = db.Column(db.String(255), nullable=False)
     #linking two tables post and category
    lga_statedeets= db.relationship('State', backref='all_lgas')

class State(db.Model):
    state_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    state_name = db.Column(db.String(255), nullable=False)
    





class Admin(db.Model):
    task_id=db.Column(db.Integer(), primary_key=True,autoincrement=True)
    email= db.Column(db.String(120), nullable=False)
    password=db.Column(db.String(50), nullable=False)

class Task(db.Model):
    task_id=db.Column(db.Integer(), primary_key=True,autoincrement=True)
    task_status=db.Column(db.Enum('1','0'),nullable=False)
    posted_when=db.Column(db.DateTime(), default=datetime.utcnow)
    description= db.Column(db.String(200), nullable=False)
    task_title=db.Column(db.String(50), nullable=False)
    task_posted_user=db.Column(db.Integer, db.ForeignKey('user.user_id'),nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.cat_id'), nullable=False)
    task_amount=db.Column(db.Float(), nullable=False)

    usertaskdeets=db.relationship('User',backref="taskuser")

   


class Category(db.Model):
    cat_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    cat_name = db.Column(db.String(50), nullable=False)  
    user_cat=db.Column(db.Integer, db.ForeignKey('user.user_id'),nullable=False)
    
    tasks = db.relationship('Task', backref='category') 
    



class Guarantor(db.Model):
    Guarantor_id=db.Column(db.Integer(), primary_key=True,autoincrement=True)
    Guarantor_email= db.Column(db.String(100), nullable=False) 
    Guarantor_address= db.Column(db.String(100), nullable=False) 
    Guarantor_phonenumber=db.Column(db.String(20), nullable=False)
    Guarantor_user_id=db.Column(db.Integer, db.ForeignKey('user.user_id'),nullable=False) 
    
    userguandeets=db.relationship('User',backref="userguanrator")

class Payment(db.Model):
    payment_id=db.Column(db.Integer(), primary_key=True,autoincrement=True)
    date_paid=db.Column(db.DateTime(), default=datetime.utcnow)
    task_payment=db.Column(db.Integer, db.ForeignKey('task.task_id'),nullable=False) 
    amount_paid=db.Column(db.Float(), nullable=False)
    ref_no=db.Column(db.String(150), nullable=False)
    payment_status=db.Column(db.Enum('1','0'),nullable=False)

    taskpaydeets=db.relationship('Task',backref="taskpaid")

class Messages(db.Model):
    message_id=db.Column(db.Integer(), primary_key=True,autoincrement=True)
    content=db.Column(db.String(200), nullable=False)
    from_id=db.Column(db.Integer, db.ForeignKey('user.user_id'))
    to_id=db.Column(db.Integer, db.ForeignKey('user.user_id'))

