from flask import Blueprint, render_template, redirect, request
from interact_with_DB import interact_db
assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')

@assignment10.route('/')
@assignment10.route('/assignment10')
def users_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', Users=users)

@assignment10.route('/insert_user', methods=['get'])  
def insert_user_func():
    name = request.args['name']
    email = request.args['email']

    query = "insert into users(name,email) values ('%s', '%s');" % (name, email)
    interact_db(query=query, query_type='commit')

    return redirect('/assignment10')

@assignment10.route('/update_user', methods=['get'])
def update_user_func():
    newName = request.args['newName']
    newEmail = request.args['newEmail']
    user_id = request.args['id']

    if newName != '' and newEmail == '':
        query = "update users set name='%s', where id='%s';" % (newName, user_id)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10') 

    if newName != '' and newEmail != '':
        query = "update users set name='%s', email='%s' where id='%s';" % (newName, newEmail, user_id)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')

    if newName == '' and newEmail != '':
        query = "update users set email='%s' where id='%s';" % (newEmail, user_id)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')

@assignment10.route('/delete_user', methods=['get'])
def delete_user_func():
    user_id = request.args['id']
    query = "delete from users where id='%s';" % user_id

    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')
