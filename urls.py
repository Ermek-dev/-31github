from core.controller import PagesController, PostsController
from core.router import Router

router = Router()
router.get('/',PagesController, 'home')
router.get('/about',PagesController, 'about')
router.get('/stats',PagesController, 'stats')
router.get('/posts',PostsController, 'posts')
router.get('/posts/add', PostsController, 'add_post')
router.post('/posts/add', PostsController, 'add')