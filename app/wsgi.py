import bottle
from app.urls import router
from bottle_neck import StripPathMiddleware


wsgi = StripPathMiddleware(bottle.Bottle())

router.mount(wsgi)
