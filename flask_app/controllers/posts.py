from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.post import Post
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/publish', methods=['POST'])
def publish():
    if request.form['content'] == '':
        flash("Post content must not be blank")
        return redirect('/wall')
    data = {
        'id': session['user'],
        'content': request.form['content']
    }
    Post.save_post(data)
    return redirect('/wall')
@app.route('/delete', methods=['POST'])
def delete_post():
    if str(session['user']) != str(request.form['user_id']):
        flash("You Do Not Have Permission To Delet This")
        return redirect('/wall')
    data = {
        "id" : request.form['id']
    }
    Post.delete_post(data)
    return redirect('/wall')