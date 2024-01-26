from app import app
from models import db, Book, User, Like, Cart, BookReview, Category, Order, Delivery, OrderDetail
from random import choice, randint, choice as rc
import json
from datetime import datetime
import random
from faker import Faker
from sqlalchemy.sql import func 
from flask_bcrypt import Bcrypt

fake = Faker()

def seed_categories():
    category_names = ["Fiction", "Science Fiction", "Mystery", "Thriller", "Romance", "Fantasy"]
    for category_name in category_names:
        existing_category = Category.query.filter_by(name=category_name).first()
        if not existing_category:
            category = Category(name=category_name)
            db.session.add(category)
    db.session.commit()

def seed_books(num_books=5):
    categories = Category.query.all()
    book_list = []
    b1 = Book(
                title= "Jujutsu Kaisen, Vol. 1",
                author= "Gege Akutami",
                page_count= 192,
                summary= "To gain the power he needs to save his friend from a cursed spirit, Yuji Itadori swallows a piece of a demon, only to find himself caught in the midst of a horrific war of the supernatural! In a world where cursed spirits feed on unsuspecting humans, fragments of the legendary and feared demon Ryomen Sukuna have been lost and scattered about. Should any demon consume Sukuna’s body parts, the power they gain could destroy the world as we know it. Fortunately, there exists a mysterious school of jujutsu sorcerers who exist to protect the precarious existence of the living from the supernatural! Although Yuji Itadori looks like your average teenager, his immense physical strength is something to behold! Every sports club wants him to join, but Itadori would rather hang out with the school outcasts in the Occult Research Club. One day, the club manages to get their hands on a sealed cursed object. Little do they know the terror they’ll unleash when they break the seal…",
                detail= "Publisher: VIZ Media LLC (December 3, 2019) Length: 192 pages ISBN13: 9781974710027",
                table_of_contents=fake.text(),
                price= 11.99,
                published_date= 2019,
                book_image= "https://m.media-amazon.com/images/I/81TmHlRleJL._SL1500_.jpg",
            )
    b2 = Book(title= "One Piece Vol. 1",
                author= "Eiichiro Oda",
                page_count= 216,
                summary= "As a child, Monkey D. Luffy dreamed of becoming King of the Pirates. But his life changed when he accidentally gained the power to stretch like rubber…at the cost of never being able to swim again! Years, later, Luffy sets off in search of the “One Piece,” said to be the greatest treasure in the world... ",
                detail= "Publisher: VIZ Media LLC (June 1, 2003) Length: 216 pages ISBN-13: 978-1569319017",
                table_of_contents=fake.text(),
                price= 9.59,
                published_date= 1997,
                book_image= "https://covers2.booksamillion.com/covers/bam/1/56/931/901/1569319014.jpg?_gl=1*15qvk6l*_ga*MTI0NjQ0MDI1OC4xNzA1NDIwOTU5*_ga_49VMH3SVSG*MTcwNjIzMzIwNy4xNC4xLjE3MDYyMzcyNTAuNTkuMC4w")
    b3 = Book(title= "Undead Unluck, Vol. 1",
                author= "Yoshifumi Tozuka",
                page_count= 192,
                summary= "Tired of inadvertently killing people with her special ability Unluck, Fuuko Izumo sets out to end it all. But when she meets Andy, a man who longs for death but can’t die, she finds a reason to live—and he finds someone capable of giving him the death he’s been longing for.",
                detail= "Publisher: VIZ Media LLC (June 1, 2003) Length: 216 pages ISBN-13: 9781974719266",
                table_of_contents=fake.text(),
                price= 9.99,
                published_date= 2021,
                book_image= "https://covers3.booksamillion.com/covers/bam/1/97/471/926/197471926X.jpg?_gl=1*1n5jp0i*_ga*MTI0NjQ0MDI1OC4xNzA1NDIwOTU5*_ga_49VMH3SVSG*MTcwNjIzMzIwNy4xNC4xLjE3MDYyMzc4MzMuMzguMC4w")
    b4 = Book(title= "Mashle: Magic and Muscles, Vol. 1",
                author= "Hajime Komoto",
                page_count= 216,
                summary= "Tired of inadvertently killing people with her special ability Unluck, Fuuko Izumo sets out to end it all. But when she meets Andy, a man who longs for death but can’t die, she finds a reason to live—and he finds someone capable of giving him the death he’s been longing for.",
                detail= "Publisher: VIZ Media LLC (July 20, 2021) Length: 216 pages ISBN-13: 9781974719266",
                table_of_contents=fake.text(),
                price= 8.50,
                published_date= 2021,
                book_image= "https://m.media-amazon.com/images/I/81nCS4q6R8L._SL1500_.jpg")
    b5 = Book(title= "Zom 100: Bucket List of the Dead, Vol. 1",
                author= "Haro Aso",
                page_count= 160,
                summary= "In a trash-filled apartment, 24-year-old Akira Tendo watches a zombie movie with lifeless, envious eyes. After spending three hard years at an exploitative corporation in Japan, his spirit is broken. He can’t even muster the courage to confess his feelings to his beautiful co-worker Ohtori. Then one morning, he stumbles upon his landlord eating lunch—which happens to be another tenant! The whole city’s swarming with zombies, and even though he’s running for his life, Akira has never felt more alive!",
                detail= "Publisher: VIZ Media LLC (February 16, 2021) Length: 160 pages ISBN-13: 978-1974720569",
                table_of_contents=fake.text(),
                price= 11.69,
                published_date= 2021,
                book_image= "https://m.media-amazon.com/images/I/81a7O+gbBAL._SL1500_.jpg")
    b6 = Book(title= "Kaiju No. 8, Vol. 1",
                author= "Naoya Matsumoto",
                page_count= 204,
                summary= "With the highest kaiju-emergence rates in the world, Japan is no stranger to attack by deadly monsters. Enter the Japan Defense Force, a military organization tasked with the neutralization of kaiju. Kafka Hibino, a kaiju-corpse cleanup man, has always dreamed of joining the force. But when he gets another shot at achieving his childhood dream, he undergoes an unexpected transformation. How can he fight kaiju now that he’s become one himself?!",
                detail= "Publisher: VIZ Media LLC (December 7, 2021) Length: 204 pages ISBN-13: 978-1974725984",
                table_of_contents=fake.text(),
                price= 6.99,
                published_date= 2021,
                book_image= "https://m.media-amazon.com/images/I/81IgJ1cGaWS._SL1500_.jpg")
    b7 = Book(title= "Sakamoto Days, Vol. 1",
                author= "Yuto Suzuki",
                page_count= 200,
                summary= "Taro Sakamoto was once a legendary hit man considered the greatest of all time. Bad guys feared him! Assassins revered him! But then one day he quit, got married, and had a baby. He’s now living the quiet life as the owner of a neighborhood store, but how long can Sakamoto enjoy his days of retirement before his past catches up to him?!",
                detail= "Publisher: VIZ Media LLC (April 5, 2022) Length: 20 pages ISBN-13: 978-1974728947",
                table_of_contents=fake.text(),
                price= 8.38,
                published_date= 2022,
                book_image= "https://m.media-amazon.com/images/I/81fNp2prCvL._SL1500_.jpg")
    b8 = Book(title= "Dandadan, Vol. 1",
                author= "Yukinobu Tatsu",
                page_count= 208,
                summary= "Momo Ayase strikes up an unusual friendship with her school’s UFO fanatic, whom she nicknames “Okarun” because he has a name that is not to be said aloud. While Momo believes in spirits, she thinks aliens are nothing but nonsense. Her new friend, meanwhile, thinks the exact opposite. To settle matters, the two set out to prove each other wrong—Momo to a UFO hotspot and Okarun to a haunted tunnel! What unfolds next is a beautiful story of young love…and oddly horny aliens and spirits?",
                detail= "Publisher: VIZ Media LLC (October 11, 2022) Length: 208 pages ISBN-13: 978-1974734634",
                table_of_contents=fake.text(),
                price= 10.79,
                published_date= 2022,
                book_image= "https://m.media-amazon.com/images/I/81kHWcb7n4L._SL1500_.jpg")
    b9 = Book(title= "Blue Period 1",
                author= "Tsubasa Yamaguchi",
                page_count= 224,
                summary= "Yatora is the perfect high school student, with good grades and lots of friends. It's an effortless performance, and, ultimately... a dull one. But he wanders into the art room one day, and a lone painting captures his eye, awakening him to a kind of beauty he never knew. Compelled and consumed, he dives in headfirst--and he's about to learn how savage and unforgiving art can be...",
                detail= "Publisher: VIZ Media LLC (October 13, 2020) Length: 224 pages ISBN-13: 978-1646511129",
                table_of_contents=fake.text(),
                price= 8.93,
                published_date= 2020,
                book_image= "https://m.media-amazon.com/images/I/81CHe2lqzDL._SL1500_.jpg")
    b10 = Book(title= "Bungo Stray Dogs, Vol. 1",
                author= "Kafka Asagiri ",
                page_count= 224,
                summary= "Having been kicked out of the orphanage, a despairing young man by the name of Atsushi Nakajima rescues a strange man from a suicide attempt--Osamu Dazai. Turns out that Dazai is part of a detective agency staffed by individuals whose supernatural powers take on a literary bent!",
                detail= "Publisher: Yen Press; Illustrated edition (December 20, 2016) Length: 196 pages ISBN-13: 978-0316554701",
                table_of_contents=fake.text(),
                price= 10.01,
                published_date= 2016,
                book_image= "https://m.media-amazon.com/images/I/818EC6x5BjL._SL1500_.jpg")

    # for _ in range(num_books):
    #     title = fake.word()
    #     used_titles = set()
    #     while title in used_titles:
    #         title = fake.word()

    #     # Check if a book with the same title already exists
    #     # existing_book = Book.query.filter_by(title=title).first()
    #     print(title)
    #     if title not in used_titles:
    #         # Insert the book if no duplicate title found
    #         book = Book(
    #             title=title,
    #             author=fake.name(),
    #             isbn=fake.isbn13(),
    #             page_count=fake.random_int(min=100, max=500),
    #             summary=fake.text(),
    #             detail=fake.text(),
    #             table_of_contents=fake.text(),
    #             price=fake.random_int(min=10, max=50),
    #             published_date=fake.date_between(start_date='-2y', end_date='today'),
    #             book_image=fake.image_url(),
    #             category=choice(categories)
    #         )
    #         book_list.append(book)
    #         used_titles.add(title)
    db.session.add(b1)
    db.session.add(b2)
    db.session.add(b3)
    db.session.add(b4)
    db.session.add(b5)
    db.session.add(b6)
    db.session.add(b7)
    db.session.add(b8)
    db.session.add(b9)
    db.session.add(b10)
    db.session.commit()

def seed_users(bcrypt, num_users=5):
    user_list = []

    for i in range(num_users):
        user = User(
            email=fake.email(),
            name=str(i),
            password=bcrypt.generate_password_hash(str(i)),
        )
        user_list.append(user)

    db.session.add_all(user_list)
    db.session.commit()

def seed_likes(num_likes=5):
    users = User.query.all()
    books = Book.query.all()

    like_list = set()

    while len(like_list) < num_likes:
        user = choice(users)
        book = choice(books)
        
        # Check if the like already exists
        existing_like = Like.query.filter_by(user_id=user.id, book_id=book.id).first()

        if existing_like is None:
            # Add a new like
            new_like = Like(user_id=user.id, book_id=book.id)
            like_list.add(new_like)

    # Convert the set of Like objects to a list before saving
    db.session.bulk_save_objects(list(like_list))
    db.session.commit()

def seed_carts(num_carts=15):
    users = User.query.all()
    books = Book.query.all()
    cart_list = []

    for _ in range(num_carts):
        cart = Cart(
            quantity=fake.random_int(min=1, max=5),
            user=choice(users),
            book=choice(books),
        )
        cart_list.append(cart)

    db.session.add_all(cart_list)
    db.session.commit()

def seed_reviews(num_reviews=20):
    users = User.query.all()
    books = Book.query.all()
    reviews_list = []

    for _ in range(num_reviews):
        review = BookReview(
            rating=fake.random_int(min=1, max=5),
            comment=fake.text(),
            reviewer=random.choice(users).name,  
            created_at=fake.date_time_this_decade(),
            book=random.choice(books),
        )
        reviews_list.append(review)

    db.session.add_all(reviews_list)
    db.session.commit()

def seed_orders(num_orders=10):
    users = User.query.all()
    deliveries = Delivery.query.all()
    order_list = []

    for _ in range(num_orders):
        order = Order(
            total_price=fake.random_int(min=50, max=200),
            ordered_at=fake.date_time_this_decade(),
            user=choice(users),
            delivery=choice(deliveries),
        )
        order_list.append(order)

    db.session.add_all(order_list)
    db.session.commit()

def seed_deliveries(num_deliveries=5):
    delivery_list = []

    for _ in range(num_deliveries):
        delivery = Delivery(
            address=fake.address(),
            recipient=fake.name(),
            contact=fake.phone_number(),
        )
        delivery_list.append(delivery)

    db.session.add_all(delivery_list)
    db.session.commit()

def seed_order_details():
    # Your seeding logic here
    order_id = 2
    book_id = 4
    quantity = 3

    # Check if the record already exists
    existing_order_detail = OrderDetail.query.filter_by(order_id=order_id, book_id=book_id).first()

    if existing_order_detail is None:
        # Record doesn't exist, proceed with insertion
        new_order_detail = OrderDetail(order_id=order_id, book_id=book_id, quantity=quantity)
        db.session.add(new_order_detail)
        db.session.commit()
    else:
        # Record already exists, handle accordingly
        print(f"Record for order_id={order_id}, book_id={book_id} already exists.")

if __name__ == "__main__":
    with app.app_context():
        bcrypt = Bcrypt(app)
        Book.query.delete()
        Category.query.delete()
        User.query.delete()
        Like.query.delete()
        Cart.query.delete()
        BookReview.query.delete()
        Delivery.query.delete()
        Order.query.delete()
        OrderDetail.query.delete()

        seed_categories()
        seed_books()
        seed_users(bcrypt)
        seed_likes()
        seed_carts()
        seed_reviews()
        seed_deliveries()
        seed_orders()
        seed_order_details()