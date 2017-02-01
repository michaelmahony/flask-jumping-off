from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():

    myData = 'This is how flask passes data through. You can pass through lists, dicts, etc., and display the results in the template'

    return render_template('test_template.html', test_data=myData)


if __name__ == '__main__':
    app.run()
