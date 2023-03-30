# this file contains all the URL mapping
from app import app
from flask import render_template, redirect, url_for
from datetime import datetime


@app.route('/')
def index():
    # return 'Hello, Mohit!'
    return render_template('index.html')


# @app.route('/add', methods=['GET', 'POST'])
# def add():
#     form = forms.AddTaskForm()
#     if form.validate_on_submit():
#         # print('Submitted title', form.title.data)
#         t = Task(title=form.title.data, date=datetime.utcnow())
#         db.session.add(t)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('add.html', form=form)
