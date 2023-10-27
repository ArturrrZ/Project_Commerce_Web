from flask import Flask, request,render_template,redirect

from flask_bootstrap import Bootstrap5
app=Flask(__name__)

Bootstrap5(app)

ITEMS_FOR_SALE={
    "chair": {
        "title": "Black Computer Chair",
        "price": "30$",
        "pic_1": "./static/assets/img/items_for_sale/chair_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/chair_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/chair_3.jpg",
    },
    "table": {
        "title": "Glass Table",
        "price": "50$",
        "pic_1": "./static/assets/img/items_for_sale/table_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/table_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/table_3.jpg"

    },
    "laptop": {
        "title": "ASUS TUF Dash F15 Gaming Laptop",
        "price": "1000$",
        "pic_1": "./static/assets/img/items_for_sale/laptop_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/laptop_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/laptop_3.jpg"

    },
    "mouse": {
        "title": "Logitech G305 Wireless Gaming Mouse",
        "price": "20$",
        "pic_1": "./static/assets/img/items_for_sale/mouse_1.jpg",
        "pic_2 ": "./static/assets/img/items_for_sale/mouse_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/mouse_3.jpg",

    },
    "mousepad":
        {
        "title": "Mouse Pad",
        "price": "10$",
        "pic_1": "./static/assets/img/items_for_sale/mousepad_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/mousepad_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/mousepad_3.jpg",
        },
    "book":
        {
        "title": "Atomic Habits by J.Clear",
        "price": "10$",
        "pic_1": "./static/assets/img/items_for_sale/book_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/book_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/book_3.jpg"
        },
    "notebook":
        {
        "title": "Study Notebook",
        "price": "99$",
        "pic_1": "./static/assets/img/items_for_sale/notebook_1.jpg",
        "pic_2": "./static/assets/img/items_for_sale/notebook_2.jpg",
        "pic_3": "./static/assets/img/items_for_sale/notebook_3.jpg"
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


















if __name__ == "__main__":
    app.run(debug=True)


