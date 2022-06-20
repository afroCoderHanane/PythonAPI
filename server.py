from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import LinkedList

#app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

#configure sqlite to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor =dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.close()

#
db =SQLAlchemy(app)
now = datetime.now()


#models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade ="all, delete")


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(75))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)

#

@app.route("/",methods=["GET"])
def welcome_message():
    return "Welcome to Flask API"

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
            name= data["name"],
            email = data["email"],
            address = data["address"],
            phone = data["phone"]
            )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 200

@app.route("/user/descending_id", methods = ["GET"])
def get_all_users_descending():
    users = User.query.all() #get all the users created
    usersll = LinkedList.LinkedList()

    for user in users:
        usersll.insertFront({
            "id":user.id,
            "name":user.name,
            "email":user.email,
            "address":user.address,
            "phone":user.phone
            })
    return jsonify(usersll.convert_to_list()),200

@app.route("/user/ascending_id", methods = ["GET"])
def get_all_users_ascending():
    users = User.query.all() #get all the users created
    usersll = LinkedList.LinkedList()

    for user in users:
        usersll.insertEnd({
            "id":user.id,
            "name":user.name,
            "email":user.email,
            "address":user.address,
            "phone":user.phone
            })
    return jsonify(usersll.convert_to_list()),200


@app.route("/user/<user_id>", methods = ["GET"])
def get_one_user(user_id):
    users = User.query.all()

    all_users_ll = LinkedList.LinkedList()

    for user in users:
        all_users_ll.insertFront(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )

    user = all_users_ll.get_user_by_id(user_id)

    return jsonify(user), 200


@app.route("/user/<user_id>", methods = ["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({}), 200

@app.route("/user/<user_id>", methods = ["POST"])
def create_blog_post(user_id):
    pass

@app.route("/user/<user_id>", methods = ["GET"])
def get_all_blog_posts(user_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods = ["GET"])
def get_one_blog_post(blog_post_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods = ["DELETE"])
def delete_blog_post(blog_post_id):
    pass

if __name__ == "__main__":
    app.run(debug=True )
