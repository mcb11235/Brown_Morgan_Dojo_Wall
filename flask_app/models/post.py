from typing import ByteString
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt
class Post:
    def __init__(self, data):
        self.id = data['id'],
        self.content = data['content'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.users_id = data['users_id'],
        self.first_name=data['first_name'],
        self.last_name=data['last_name']
    @classmethod
    def save_post(cls, data):
        query = "INSERT INTO posts (content, users_id) VALUES ( %(content)s , %(id)s );"
        return connectToMySQL('user_schema').query_db(query, data)
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM posts JOIN users ON users_id=users.id "
        posts = []
        results = connectToMySQL('user_schema').query_db(query)
        for post in results:
            posts.append(cls(post))
        return posts
    @classmethod
    def delete_post(cls, data):
        query = "DELETE FROM posts WHERE id=%(id)s"
        return connectToMySQL('user_schema').query_db(query, data)