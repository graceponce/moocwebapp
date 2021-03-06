from typing import Any

from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('u2_index_ini.html')

@app.route('/ejemplo/')
def hello_world():
    return ('<!DOCTYPE html> '
            '<html lang="es">'
            '<head>'
            '<title> Home - SocNet </title>'
            '</head>'
            '<body> <div id="container">'
                '<a href="/"> Socnet </a> | <a href="/home/"> Home </a> | <a href="/login/"> Log In </a> | <a href="/signup/"> Sign Up </a>'
                '<h1>Hi, How are you?</h1>'
            )

@app.route('/home/', methods=['GET'])
def home():
    return app.send_static_file('home.html')


@app.route('/login/', methods=['GET'])
def login():
    return app.send_static_file('login.html')


@app.route('/signup/', methods=['GET'])
def signup():
    return app.send_static_file('signup_ini.html')


@app.route('/processing/', methods=['GET', 'POST'])
def processing():
    missing = []
    fields = ['email', 'passwd', 'login_submit']
    for field in fields:
        value = request.form.get(field, None)
        if value is None:
            missing.append(field)
    if missing:
        return "Warning: Some fields are missing"

    return ('<!DOCTYPE html> ' 
           '<html lang="es">' 
           '<head>' 
           '<title> Home - SocNet </title>' 
            '<style>'
              'form{font-size: 120%;'
              'border-radius: 10px;'
              'border: 2px solid #d69544;'
              'padding: 5px;'
              'margin: 5px;'
              'overflow-scrolling: auto;'
             '}'
              'h1 {color:#d69544;font-size:200%;margin: 20px;}'
            '</style>' 
           '</head>' 
           '<body> <div id ="container">' 
           '<a href="/"> SocNet </a> | <a href="/home/"> Home </a> | <a href="/login/"> Log In </a> | <a href="/signup/"> Sign Up </a>' 
           '<h1>Data from Form: Login</h1>' 
           '<form><label>email: ' + request.form.get('email',"") +
           '</label><br><label>passwd: ' + request.form.get('passwd',"")
                                                            +
           '</label></form></div></body>' 
           '</html>')


@app.route('/processSignup/', methods=['GET', 'POST'])
def processSignup():
       missing = []
       fields = ['nickname', 'email', 'passwd','confirm', 'signup_submit']
       for field in fields:
              value = request.form.get(field, None)
              if value is None:
                     missing.append(field)
       if missing:
              return "Warning: Some fields are missing"

       return ('<!DOCTYPE html> ' 
           '<html lang="es">' 
           '<head>' 
           '<title> Home - SocNet </title>' 
            '<style>'
              'form{font-size: 120%;'
              'border-radius: 10px;'
              'border: 2px solid #d69544;'
              'padding: 5px;'
              'margin: 5px;'
              'overflow-scrolling: auto;'
             '}'
              'h1 {color:#d69544;font-size:200%;margin: 20px;}'
            '</style>' 
           '</head>' 
           '<body> <div id ="container">' 
		   '<a href="/"> SocNet </a> | <a href="/home/"> Home </a> | <a href="/login/"> Log In </a> | <a href="/signup/"> Sign Up </a>' \
           '<h1>Data from Form: Sign Up</h1>' 
           '<form><label>Nickname: ' + request.form['nickname'] + 
	       '</label><br><label>email: ' + request.form['email'] + 
	       '</label><br><label>passwd: ' + request.form['passwd'] + 
	       '</label><br><label>confirm: ' + request.form['confirm'] + 
           '</label></form></div></body>' 
         '</html>')


@app.route('/processHome/', methods=['GET', 'POST'])
def processHome():
	missing = []
	fields = ['message', 'last', 'post_submit']
	for field in fields:
		value = request.form.get(field, None)
		if value is None:
			missing.append(field)
	if missing:
		return "Warning: Some fields are missing"

	return ('<!DOCTYPE html> ' 
           '<html lang="es">' 
           '<head>' 
           '<title> Home - SocNet </title>'
           '<style>'
              'form{font-size: 120%;'
              'border-radius: 10px;'
              'border: 2px solid #d69544;'
              'padding: 5px;'
              'margin: 5px;'
              'overflow-scrolling: auto;'
             '}'
              'h1 {color:#d69544;font-size:200%;margin: 20px;}'
            '</style>' 
           '</head>' 
           '<body> <div id="container">' 
		   '<a href="/"> SocNet </a> | <a href="/home/"> Home </a> | <a href="/login/"> Log In </a> | <a href="/signup/"> Sign Up </a>' 
           '<h1>Hi, How are you?</h1>' 
           '<form action="/processHome/" method="post" name="home"> ' 
			'<label for="message">Say something:</label><div class="inputs">' 
			'<input id="message" maxlength="128" name="message" size="80" type="text" required="true" value=""/>' 
			'<input id="last" type="hidden" name="last" required="true" value="' + request.form.get('last',"") + '<br>'+ request.form.get('message',"") + '">' 
	                 '</div>' 
                    	'<div class="inputs">' 
                        '<input id="post_submit" name="post_submit" type="submit" value="Post!"/>' 
           		'<br><br>Previous Posts: <br>' + request.form.get('last',"") + '<br>' +request.form.get('message',"") +
                	'</form>' 
            		'</div></div>' 
           '</body>' 
           '</html>')

#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, port=8080)