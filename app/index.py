from flask import Flask, render_template
import dao

app = Flask(__name__)


@app.route('/')
def index():
    cat = dao.get_categories()
    pro = dao.get_product()
    return render_template('index.html', categories= cat, products = pro)


@app.route('/trang1')
def index1():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
