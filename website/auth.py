from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/Logout')
def logout():
    return render_template("logout.html")

@auth.route('/Sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 4 characters',category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 character',category='error')
        elif len(password1) < 8:
            flash('Password must be at-least 7 characters',category='error')
        elif password1 != password2:
            flash('Passwords does not match',category='error')
        else:
            flash('Account created successfully!',category='success')
        
        
        
    return render_template("sign_up.html")

