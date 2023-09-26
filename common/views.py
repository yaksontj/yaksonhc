from django.shortcuts import render

# Create your views here.
from django.contrib.sessions.backends.db import SessionStore


def index(request):
    ...
    # 방법 1
    s = SessionStore()
    s['key'] = 'value'
    s.create()

    # 방법 2
    request.session['key'] = value
    ...
    return render(request, 'index.html')