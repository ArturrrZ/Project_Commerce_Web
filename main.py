from flask import Flask, render_template,redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm,LoginForm

app=Flask(__name__)
app.config['SECRET_KEY']="asdxzcz124aASDzzxc23145asfzzx"

app.config['SQLALCHEMY_DATABASE_URI']=('sqlite:///database.db')
db = SQLAlchemy()
db.init_app(app)

class User(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(250),unique=True,nullable=False)
    password=db.Column(db.String(250),nullable=False)
    name=db.Column(db.String(100),nullable=False)

with app.app_context():
    db.create_all()

Bootstrap5(app)

ITEMS_FOR_SALE={
    "chair": {
        "title": "Black Computer Chair",
        "price": 30,
        "pic_1": "./static/assets/img/items_for_sale/chair_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/chair_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/chair_3.jpg",
        "description": "Introducing the epitome of comfort and sophistication – our Black Leather Chair. This elegant "
                       "and luxurious chair is"
                       " the perfect addition to any space, whether it's your home, office, or a high-end lounge. "
                       "Crafted with "
                       "meticulous attention to detail and designed for both style and relaxation, this chair offers a "
                       "sublime seating"
                       " experience."
    },
    "table": {
        "title": "Glass Table",
        "price": 50,
        "pic_1": "./static/assets/img/items_for_sale/table_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/table_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/table_3.jpg",
        "description": "Elevate your workspace with Black Glass Computer Table – a sleek and functional addition that "
                       "combines "
                       "modern design with practicality. This contemporary desk is designed to enhance your"
                       " productivity"
                       "and create "
                       "an atmosphere of sophistication in any home or office."

    },
    "laptop": {
        "title": "ASUS TUF Dash F15 Gaming Laptop",
        "price": 1000,
        "pic_1": "./static/assets/img/items_for_sale/laptop_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/laptop_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/laptop_3.jpg",
        "description": "Step into the world of high-performance gaming with the ASUS TUF Dash F15, a gaming laptop "
                       "that's "
                       "engineered to deliver exceptional power, style, and portability. Whether you're a competitive "
                       "gamer,"
                       " content creator, or just seeking a cutting-edge laptop for your computing needs, the ASUS TUF"
                       " Dash F15"
                       " has you covered.",
    },
    "mouse": {
        "title": "Logitech G305 Wireless Gaming Mouse",
        "price": 20,
        "pic_1": "./static/assets/img/items_for_sale/mouse_1.jpg",
        "pic_2 ": "./static/assets/img/items_for_sale/mouse_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/mouse_3.jpg",
        "description": "Get ready to up your gaming performance with the Logitech G305 Wireless Gaming Mouse. "
                       "This cutting-edge "
                       "gaming accessory is designed to deliver precision, speed, and freedom of movement for "
                       "gamers of all levels.",
    },
    "mousepad":
        {
        "title": "Mouse Pad",
        "price": 10,
        "pic_1": "./static/assets/img/items_for_sale/mousepad_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/mousepad_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/mousepad_3.jpg",
        "description": "Elevate your gaming setup with the USCIS Mouse Pad, a sleek and high-performance"
                       " accessory designed to"
                       " enhance your gaming experience in style and precision."
        },

    "book":
        {
        "title": "Atomic Habits by J.Clear",
        "price": 10,
        "pic_1": "./static/assets/img/items_for_sale/book_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/book_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/book_3.jpg",
        "description": "Dive into the world of personal development and transformative change with the book"
                       " 'Atomic Habits' by James Clear. This bestselling book is your ultimate guide to unlocking"
                       " the power of small habits for big, positive changes in your life."
        },
    "notebook":
        {
        "title": "Study Notebook",
        "price": 99,
        "pic_1": "./static/assets/img/items_for_sale/notebook_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/notebook_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/notebook_3.jpg",
        "description": "Unlock your potential in Python programming with the Green Python Study Notebook, "
                       "the perfect companion for both beginners and seasoned coders embarking "
                       "on their Python learning journey.",
        }

}



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/check_father")
def check():
    return render_template("father_template.html")

@app.route("/items")
def display_items():
    return render_template("items.html", items=ITEMS_FOR_SALE)


@app.route("/sale/<item>")
def sale(item):
    print(ITEMS_FOR_SALE[item])
    return render_template('item_separate.html', item=ITEMS_FOR_SALE[item],name=item)

@app.route("/register", methods=['POST','GET'])
def register():
    register_form=RegisterForm()
    if register_form.validate_on_submit():
        email=register_form.email.data
        password=register_form.password.data
        hash_password=generate_password_hash(password,method='pbkdf2:sha256',salt_length=8)
        name=register_form.name.data
        find_user=db.session.execute(db.select(User).where(User.email==email)).scalar()
        if find_user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        else:
            new_user=User(
                email=email,
                password=hash_password,
                name=name,
            )
            db.session.add(new_user)
            db.session.commit()
            #login
            return redirect(url_for('home'))


    return render_template('register.html',form=register_form)

@app.route("/login",methods=['POST','GET'])
def login():
    login_form=LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        find_user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if not find_user:
            flash("Invalid email, try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(find_user.password, password):
            flash('Invalid password, try again')
            return redirect(url_for('login'))
        else:
            return "You logged in!"


    return render_template('login.html',form=login_form)


















if __name__ == "__main__":
    app.run(debug=True)


