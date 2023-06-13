#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# A print_string view should take one parameter, a string. It should print the string in the console and display it in the web browser. Its URL should be of the format /print/paramter.
@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'{param}'

# A count() view should take one parameter, an integer. It should display all numbers in the range of that parameter on separate lines. Its URL should be of the format

@app.route('/count/<int:param>')
def count(param):
    count = f''
    for n in range(param):
        count += f'{n}\n'
    return count


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math_add(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    else:
        return "Wrong"
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
