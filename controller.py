import jinja2

from core.db import Database
from core.errors import not_found
from core.settings import ROOT_PATH
from requests import HTTPResponseCode, response
from jinja2 import Environment, FileSystemLoader


class Controller:
    def __init__(self,request,response):
        self.request = request
        self.response = response
        self.builder = jinja2.Environment()


    def render_body(self, template_name, **ctx):
        template_path = ROOT_PATH + '/templates/' + template_name
        with open(template_path, 'r') as file:
            template_body = file.read()
            template = self.builder.from_string(template_body)
            return template.render(context=ctx)
class PagesController(Controller):
    # def home(self):
    #     self.response.add_header('Content-Type', 'text/html')
    #     body = self.render_body('home.html', **{'name': 'John', 'age': 22,'numbers': [1,2,3,4,5]})
    #     self.response.set_body(body)
        # self.response.set_body('<h1>This is home page</h1><img src="media/cat.jpg">')
    def home(self):
        body = self.render_body('home.html')
        self.response.set_body(body)

    def about(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<h1> This is about page</h1>')


    def stats(self):
        body = self.render_body('stats.html')
        self.response.set_body(body)




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



    def add_post(self):
        body = self.render_body('add_post.html')
        self.response.set_body(body)


    def add(self):
        post = {
            'category': self.request.body.get('category')[0],
            'description': self.request.body.get('description')[0],
            'amount': int(self.request.body.get('amount')[0]),

        }
        Database.add(post)
        self.response.set_status(HTTPResponseCode.MOVED_PERMANENTLY)
        self.response.add_header('location','/posts')









# class PostsController(Controller):
#     def posts(self, pk=None):
#         posts_db = Database.posts
#         if not pk:
#             body = f'<h1> This is post page. Posts count {len(posts_db)}</h1>'
#             for post in posts_db:
#                 body += f"<p>id: {post.get('id')}, title: {post.get('title')}</p>"
#         else:
#             post = Database.get_post_by_pk(pk=pk)
#             if post:
#                 body = f"<p>id: {post.get('id')}, title: {post.get('title')}</p>"
#             else:
#                 not_found(self.request, self.response)
#                 return
#         self.response.add_header('Content-Type', 'text/html')
#         self.response.set_body(body)
