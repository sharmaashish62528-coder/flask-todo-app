# login and logout 


from flask import Blueprint, render_template, request,  redirect, url_for, flash , session
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)  # A Blueprint is used to group related routes together.


@auth_bp.route('/login' , methods = ["GET" , "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username = username).first() # Find me the user whose username is equal to the username the person entered.
        if user and user.password == password:
            session['user'] = user.id
            flash("login Successful" , 'success')
            return redirect(url_for('tasks.view_tasks'))

        else:
            flash('Invalid username or  password' , 'danger')

    return render_template('login.html')



@auth_bp.route('/register' , methods = ["GET" , "POST"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User(
            username = username,
            password = password
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    return render_template('register.html')
    
    


@auth_bp.route('/logout')
def logout():
    session.pop('user' , None)
    flash('Logged out', 'info')

    return redirect(url_for('auth.login'))