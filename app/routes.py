from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

@app.route('/learn')
def new_view():
    return "Hello learners"

if __name__ == '__main__':
    app.run(debug=True)