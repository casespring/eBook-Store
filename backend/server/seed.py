from app import app
from models import db, Book, BookReview, User, OrderDetail
import json


if __name__ == "__main__":
    with app.app_context():
        with open("db.json") as f:
            data = json.load(f)
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
            for review in book_review_list:
                r = BookReview(
                reviewer = review.get('reviewer'),
                comment = review.get('comment'),
                created_at = review.get('created_at'),
                )
            book_review_list.append(r)
        db.session.add_all(book_review_list)
        db.session.commit()

        for use in data["user"]:
            for user in user_data:
                u = User(
                    email = user.get('email'),
                    name = user.get('name'),
                    password = user.get('password'),
                )
            user_data.append(u)
        db.session.add_all(user_data)
        db.session.commit()

        for order in data["order"]:
            for od in order_data:
                o = OrderDetail(
                    total_price = od.get('total_price')
                )
            order_data.append(o)
        db.session.add_all(order_data)
        db.session.commit()


# from app import app
# from models import db, Book, BookReview, User, OrderDetail
# import json

# if __name__ == "__main__":
#     with app.app_context():
#         with open("db.json") as f:
#             data = json.load(f)
        
#         book_list = []
#         for book_data in data["books"]:
#             b = Book(
#                 title=book_data.get('title'),
#                 author=book_data.get('author'),
#                 isbn=book_data.get('isbn'),
#                 # ... other attributes
#             )
#             book_list.append(b)
#         db.session.add_all(book_list)
#         db.session.commit()

#         book_review_list = []
#         for review_data in data["book_review"]:
#             r = BookReview(
#                 reviewer=review_data.get('reviewer'),
#                 comment=review_data.get('comment'),
#                 created_at=review_data.get('created_at'),
#             )
#             book_review_list.append(r)
#         db.session.add_all(book_review_list)
#         db.session.commit()

#         user_data = []
#         for user_data in data["user"]:
#             u = User(
#                 email=user_data.get('email'),
#                 name=user_data.get('name'),
#                 password=user_data.get('password'),
#             )
#             user_data.append(u)
#         db.session.add_all(user_data)
#         db.session.commit()

#         order_data = []
#         for order_data in data["order"]:
#             o = OrderDetail(
#                 total_price=order_data.get('total_price')
#             )
#             order_data.append(o)
#         db.session.add_all(order_data)
#         db.session.commit()