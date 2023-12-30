from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__, template_folder='templates')
app.secret_key = 'Arsen'

@app.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')

        response = make_response(redirect('/welcome'))
        response.set_cookie('user_name', user_name)
        response.set_cookie('user_email', user_email)

        return response

    user_name = request.cookies.get('user_name')

    if request.path == '/welcome' and user_name:
        return render_template('welcome.html', user_name=user_name)

    if request.path == '/logout':
        response = make_response(redirect('/'))
        response.delete_cookie('user_name')
        response.delete_cookie('user_email')

        return response

    return render_template('input_form.html')

if __name__ == '__main__':
    app.run(debug=True)
