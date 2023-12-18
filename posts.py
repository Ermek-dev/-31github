from core.controllers.base import Controller
from core.db import Database
from core.errors import not_found
from requests import HTTPResponseCode


class PostsController(Controller):
    def posts(self, pk=None):
        posts_db = Database.posts
        if not pk:
            body = self.render_body('posts.html', **{'posts': posts_db})
            self.response.set_body(body)
            return
        post = Database.get_post_by_pk(pk)
        if post:
            body = self.render_body('posts.html', *{'post': post})
            self.response.set_body(body)
        else:
            not_found(self.request,self.response)


    def add(self):
        body = self.render_body('add_post.html')
        self.response.set_body(body)


    def add_post(self):
        post = {
            'id': int(self.request.body.get('id')[0]),
            'title': self.request.body.get('title')[0]
        }
        Database.add(post)
        self.response.set_status(HTTPResponseCode.MOVED_PERMANENTLY)
        self.response.add_header('location','/posts')
