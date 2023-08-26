
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField,TextAreaField,PasswordField,DateField,SelectField,FileField
from wtforms.validators import DataRequired,Email,Length, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired


class Signup(FlaskForm):
    firstname=StringField("Fullname",validators=[DataRequired(message="you should suplly your name")])
    lastname=StringField("Lastname",validators=[DataRequired(message="you should suplly your name")])
    email=StringField('Email', validators=[Email()])
    address= TextAreaField("Address")
    Dateofbirth= DateField('Date of Birth', format='%m/%d/%Y', validators=[DataRequired(message='Invalid date of birth')])
    phonenumber = StringField('Phone Number', validators=[DataRequired(message='Please enter a valid 10-digit phone number')
    ])
    state = SelectField('State', choices=[('AB', 'Abia'), ('AD', 'Adamawa'), ('AK', 'Akwa Ibom'), ('AN', 'Anambra'), ('BA', 'Bauchi'), ('BY', 'Bayelsa'), ('BE', 'Benue'), ('BO', 'Borno'), ('CR', 'Cross River'), ('DE', 'Delta'), ('EB', 'Ebonyi'), ('ED', 'Edo'), ('EK', 'Ekiti'), ('EN', 'Enugu'), ('FC', 'Federal Capital Territory'), ('GO', 'Gombe'), ('IM', 'Imo'), ('JI', 'Jigawa'), ('KD', 'Kaduna'), ('KN', 'Kano'), ('KT', 'Katsina'), ('KE', 'Kebbi'), ('KO', 'Kogi'), ('KW', 'Kwara'), ('LA', 'Lagos'), ('NA', 'Nasarawa'), ('NI', 'Niger'), ('OG', 'Ogun'), ('ON', 'Ondo'), ('OS', 'Osun'), ('OY', 'Oyo'), ('PL', 'Plateau'), ('RI', 'Rivers'), ('SO', 'Sokoto'), ('TA', 'Taraba'), ('YO', 'Yobe'), ('ZA', 'Zamfara')])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[DataRequired( message='Invalid gender')])
    password = PasswordField("password",validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password",validators=[EqualTo('password',message="confirm password must be equal to password")])
    btn = SubmitField("Sign up!")
 
   

class Loginform(FlaskForm): 
    email=StringField('Email', validators=[Email()])
    password = PasswordField("password",validators=[DataRequired()])
    btn = SubmitField("login !")
 
  
class Updateform(FlaskForm):
    firstname = StringField("Fullname",validators=[DataRequired(message="your fullname is required")])
    lastname=StringField("Fullname",validators=[DataRequired(message="your fullname is required")])
    email= email=StringField('Email', validators=[Email()])
    phonenumber = StringField('Phone Number', validators=[DataRequired(message='Please enter a valid 10-digit phone number')
    ])
    pix = FileField("Display picture",validators=[FileRequired(), FileAllowed(['jpg','png'], 'images only!')])
    btn = SubmitField("upload")


class Profileform(FlaskForm):
    firstname= StringField("Firstname",validators=[DataRequired(message="your fullname is required")])
    
    pix = FileField("Display picture",validators=[FileRequired(), FileAllowed(['jpg','png'], 'images only!')])
    btn = SubmitField("upload")
 