from flask import Flask, render_template

app = Flask('Flask App')

# Home
@app.route('/')
def index():  # put application's code here
    data = ['Rajib Ahmed', 'Tasfiya Jahan', 'Tahiya Ibnat']
    return render_template('frontend/index.html', names=data)


if __name__ == '__main__':
    app.run()
