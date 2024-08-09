from pathlib import Path
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from blog.models import Post, Comment, Author

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "images/kseniia-rastvorova-U2AwijfUNS4-unsplash.jpg",
        "author": "Alejandra Valdivia",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Alejandra Valdivia",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Alejandra Valdivia",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post['date']

def homepage(request):
    # latests_posts = Post.objects.all().order_by('-date')[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, 'home.html', {'posts': posts}) #latests_posts goes here


class Post:
    def __init__(self, slug, image, author, date, title, excerpt, content):
        self.slug = slug
        self.image = image
        self.author = author
        self.date = date
        self.title = title
        self.excerpt = excerpt
        self.content = content

    def __str__(self):
        return self.title



def posts(request):  #this is our posts page(might delete the homepage if not needed)
    return render(request, 'posts/index.html', {'all_posts': all_posts})


# create PostDetail class here
class PostDetail:
    def __init__(self, title, content, author, created_at, image):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = created_at
        self.image = image

    def __str__(self):
        return self.title
    

def post_detail(request, slug):
    identified_post = Post.objects.get(slug=slug)
    return render(request, 'blog/post-detail.html', {'post': identified_post})

def error_404_view(request, exception):
    return render(request, '404.html')