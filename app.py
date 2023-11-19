# from core.db import Database
# from requests import HTTPResponseCode
#
#
# def not_found(request, response):
#     response.set_status(HTTPResponseCode.NOT_FOUND)
#     response.add_header('Content-Type', 'text/css')
#     response.set_body('<h1> 404 Not Found</h1>')
#
#
# def home(request, response):
#     response.add_header('Content-Type', 'text/css')
#     response.set_body('<h1> This is main page</h1>')
#
# def about(request, response):
#     response.add_header('Content-Type', 'text/css')
#     response.set_body('<h1> This is about page</h1>')
#
#
#
#
# def posts(request, response, pk=None):
#     posts_db = Database.posts
#     if not pk:
#         body = f'<h1> This is post page. Posts count {len(posts_db)}</h1>'
#         for post in posts_db:
#             body += f"<p>id: {post.get('id')}, title: {post.get('title')}</p>"
#     else:
#         post = Database.get_post_by_pk(pk=pk)
#         if post:
#             body = f"<p>id: {post.get('id')}, title: {post.get('title')}</p>"
#         else:
#             not_found(request,response)
#             return
#     response.add_header('Content-Type', 'text/css')
#     response.set_body(body)
#
#
