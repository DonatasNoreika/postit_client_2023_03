from django.shortcuts import render, redirect
import requests

token = "fcc268819175a3c60ed81374f32371f8d5354683"

# Create your views here.
def posts(request):
    r = requests.get('http://127.0.0.1:8000/posts')
    return render(request, 'posts.html', context={'posts': r.json()})


def post(request, post_id):
    r = requests.get(f'http://127.0.0.1:8000/posts/{post_id}')
    return render(request, 'post.html', context={'post': r.json()})


def new_post(request):
    if request.method == "POST":
        naujas_irasas = {
            'title': request.POST['title'],
            'body': request.POST['body'],
        }
        headers = {
            "Authorization": f"Token {token}"
        }
        r = requests.post('http://127.0.0.1:8000/posts', data=naujas_irasas, headers=headers)
        return redirect("posts")
    else:
        return render(request, "new_post.html")