from flask.globals import request
from app import app
from flask import render_template, redirect, url_for
import math




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('submit'):
            a = request.form['num1']
            b = request.form['num2']
            opr = request.form['operator']

            if opr == 'plus':
                try:
                    num1 = a
                    num2 = b
                    op = opr
                    result = float(num1) + float(num2)
                    return render_template('index.html', result=result, a=num1, b=num2, op=op)
                except ValueError:
                    pass

            elif opr == 'minus':
                try:
                    num1 = a
                    num2 = b
                    op = opr
                    result = float(num1) - float(num2)
                    return render_template('index.html', result=result, a=num1, b=num2, op=op)
                except ValueError:
                    pass

            elif opr == 'multiply':
                try:
                    num1 = a
                    num2 = b
                    op = opr
                    result = float(num1) * float(num2)
                    return render_template('index.html', result=result, a=num1, b=num2, op=op)
                except ValueError:
                    pass

            elif opr == 'divide':
                try:
                    num1 = a
                    num2 = b
                    op = opr
                    result = float(num1) / float(num2)
                    return render_template('index.html', result=result, a=num1, b=num2, op=op)
                except ZeroDivisionError:
                    result ='0'
                    return render_template('index.html', result=result, a=num1, b=num2, op=op)

            elif opr == 'power':
                try:
                    num1 = a
                    num2 = b
                    op = opr
                    result = float(num1) ** float(num2)
                    return render_template('index.html', result=result, a=num1, b=num2, op=op)
                except ValueError:
                    pass

            elif opr == 'remainder':
                try:
                    num1 = a
                    num2 = b
                    op = opr
                    result = float(num1) % float(num2)
                    return render_template('index.html', result=result, a=num1, b=num2, op=op)
                except ValueError:
                    pass

            elif opr == 'log':
                try:
                    num1 = float(a)
                    op = opr
                    result = math.log(num1)
                    return render_template('index.html', result=result, a=num1, op=op)
                except ValueError:
                    pass

            elif opr == 'log_base':
                try:
                    num1 = float(a)
                    num2 = float(b)
                    op = opr
                    result = math.log(num1, num2)
                    return render_template('index.html', result=result, a=num1, b=num2, op=op)
                except ValueError:
                    pass

                except ZeroDivisionError:
                    pass



        if request.form.get('clear'):
            return render_template('index.html')

    return render_template('index.html')



