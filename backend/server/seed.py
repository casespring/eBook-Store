from app import app
from models import db, Book, Book_Review, User, Order_Detail
import json

if __name__ == "__main__":
    with app.app_context():
        with open("db.json") as f:
            data = json.load(f)

        for book in data["books"]:
            book_list = []
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
        db.session.add(book_list)
        db.session.commit()

        for review in data["book_review"]:
            book_review_list = []
            for review in book_review_list:
                r = Book_Review(
                reviewer = review.get('reviewer'),
                comment = review.get('comment'),
                created_at = review.get('created_at'),
                )
            book_review_list.append(r)
        db.session.add(book_review_list)
        db.session.commit()

        for use in data["user"]:
            user_data = []
            for user in user_data:
                u = User(
                    email = user.get('email'),
                    name = user.get('name'),
                    password = user.get('password'),
                )
            user_data.append(u)
        db.session.add(user_data)
        db.session.commit()

        for order in data["order"]:
            order_data = []
            for od in order_data:
                o = Order_Detail(
                    total_price = od.get('total_price')
                )
            order_data.append(o)
        db.session.add(order_data)
        db.session.commit()


