from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    pubyear = db.Column(db.String(50), nullable=False)

@app.route('/add_book', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user = request.form
        new_user = Books(title=user['title'], author=user['author'], pubyear=user['pubyear'])
        db.session.add(new_user)
        db.session.commit()
        list = Books.query.all()
        return render_template('books.html', list=list)
    return render_template('add_book.html')

@app.route('/books')
def members():
    list = Books.query.all()
    return render_template('books.html', list=list)

def create_db():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_db()
    app.run()