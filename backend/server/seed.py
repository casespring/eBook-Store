from app import app
from models import db, Book, BookReview, User, Order, Category
import json
from datetime import datetime


if __name__ == "__main__":
    with app.app_context():
        with open("db.json") as f:
            data = json.load(f)

        Book.query.delete()
        BookReview.query.delete()
        User.query.delete()
        Order.query.delete()

        book_list = []
        book_review_list = []
        user_data = []
        order_data = []

        for book in data["books"]:
            b = Book(
                title = book.get('title'),
                author = book.get('author'),
                # isbn = book.get('isbn'),
                # page_count = book.get('page_count'),
                # summary = book.get('summary'),
                # detail = book.get('detail'),
                # table_of_contents = book.get('table_of_contents'),
                # price = book.get('price'),
                # published_date = book.get('published_date')
            )
            book_list.append(b)
        db.session.add_all(book_list)
        db.session.commit()

        for review in data["book_review"]:
            date_string = review.get('created_at')
            date_format = "%m/%d/%Y"
            date_object = datetime.strptime(date_string, date_format)
            r = BookReview(
                reviewer=review.get('reviewer'),
                comment=review.get('comment'),
                created_at= date_object,
            )
            book_review_list.append(r)
        db.session.add_all(book_review_list)
        db.session.commit()


        for user in data["user"]:
        # for user in user_data:
            u = User(
                email = user.get('email'),
                name = user.get('name'),
                password = user.get('password'),
            )
            user_data.append(u)
        db.session.add_all(user_data)
        db.session.commit()

        for order in data["order"]:
            # for od in order_data:
            o = Order(
                total_price = order.get('total_price')
            )
            order_data.append(o)
        db.session.add_all(order_data)
        db.session.commit()
