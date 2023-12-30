from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key'  # Замените 'your_secret_key' на свой секретный ключ

@app.route('/')
def input_form():
    return render_template('input_form.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    user_name = request.form.get('user_name')
    user_email = request.form.get('user_email')

    response = make_response(redirect('/welcome'))
    response.set_cookie('user_name', user_name)
    response.set_cookie('user_email', user_email)

    return response

@app.route('/welcome')
def welcome():
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('welcome.html', user_name=user_name)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')

    return response

if __name__ == '__main__':
    app.run(debug=True)
