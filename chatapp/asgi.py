import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from room.routing import websocket_urlpatterns


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatapp.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  
        )
    ),
})

def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart:
        print('Kevin', kevin)
    elif kevin < stuart:
        print('Stuart', stuart)
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)