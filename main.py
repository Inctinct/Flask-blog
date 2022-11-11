from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app= Flask(__name__)
#To work correctly, you need to manually create the database.
# And specify the correct path to the database:
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://username:pass@localhost:port/name_database'
db=SQLAlchemy(app)
migrate= Migrate(app,db)

class Posts(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100),primary_key=False)
    text=db.Column(db.Text,nullable=False)
    date=db.Column(db.DateTime,default=datetime.utcnow)


    def __repr__(self):
        return f'Posts: {self.id}'


with app.app_context() as context:
    db.create_all()


@app.route('/')
def index():
    posts=Posts.query.order_by(Posts.id).all()
    return render_template('index.html',data=posts)

@app.route('/create',methods=['POST','GET'])
def create():
    if request.method == 'POST':
        title=request.form['title']
        text=request.form['text']
        post=Posts(title=title,text=text)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return 'Не удалось создать пост'
    else:
        return render_template('create.html')


@app.route('/update/<int:id>',methods=['POST','GET'])
def update(id):
    post=Posts.query.get(id)
    if request.method == 'POST':
        post.title=request.form['title']
        post.text=request.form['text']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "При редактировании произошла ошибка"
    else:
        return render_template('update.html',post=post)

@app.route('/delete/<int:id>')
def delete(id):
    post = Posts.query.get_or_404(id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect('/')
    except:
        return 'При удалении статьи произошла ошибка'

if __name__ == '__main__':
    app.run(debug=True)
