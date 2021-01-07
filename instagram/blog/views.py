from django.shortcuts import (render, HttpResponseRedirect, get_object_or_404, redirect)

from .models import Post, Comment, Following
from insta.models import Profile

from .forms import CommentForm

from django.urls import reverse

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

import json
from django.http import HttpResponse

from django.db.models import Q

@login_required(login_url='login')
def home(request):
    posts = Post.objects.all()
    user = request.user
    profile = Profile.objects.get(user=user)
    cform = CommentForm()
    
    context = {
        'posts':posts,
        'cform': cform,
        'profile': profile,
    }
    template = 'blog/home.html'
    return render(request, template, context)

@login_required(login_url='login')
def delete_post(request, id):
    post_to_delete = get_object_or_404(Post, id = id)
    post_to_delete.delete()
    return HttpResponseRedirect('/')



# profile
@login_required(login_url='login')
def visit_pofile(request, id):
    profile = get_object_or_404(Profile, id = id)
    post_user = Post.objects.filter(author = profile.user.id)
    connection = Following.objects.filter(user = request.user, followed= profile.user)
    follower = Following.objects.filter(followed__in=[profile.user.id]).distinct().count()
    print(follower)
    try:
        following_user_count = Following.objects.get(user = profile.user)
        no_of_following = following_user_count.followed.all().count()
    except :
        no_of_following = 0
    context = {
        'post_user' : post_user,
        'profile' :profile,
        'post_users': post_user.count(),
        'connection' : connection,
        'no_of_following':no_of_following,
        'follower':follower,
    }
    template = 'blog/profile.html'
    return render(request, template, context)




# comment views
@login_required(login_url='login')
def add_comment(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        cform = CommentForm(request.POST or None)
        content = request.POST.get('content')
        comment = Comment.objects.create(post = post, user = request.user, content = content)
        comment.save()
        return HttpResponseRedirect('/')


@login_required(login_url='login')
def update_comment(request,id):
    comment = get_object_or_404(Comment, id= id)

    form = CommentForm(reques.POST, instance=comment)
    form.save()
    return HttpResponseRedirect('/')


@login_required(login_url='login')
def delete_comment(request, id):
    comment_to_delete = get_object_or_404(Comment, id)
    comment_to_delete.delete()
    return HttpResponseRedirect('/')


# change profile pics
@login_required(login_url='login')
def change_profile_pic(request, id):
    profile = get_object_or_404(Profile, id=id)
    profiles = Profile.objects.get(user = profile.user.id)
    # print(profiles)
    if request.method == "POST":
        pic = request.FILES['images']
        profiles.profile_pics = pic
        profiles.save()
        return redirect(visit_pofile,id=id)


# search functionality
@login_required(login_url='login')
def search(request):
    query = request.POST.get('search')
    
    query = User.objects.filter(Q(username__icontains=query)).first()
    post_user = Post.objects.filter(author=query)
    post_count = Post.objects.filter(author=query).count() 
    
    connection = Following.objects.filter(user = request.user, followed= query)
    context = {
       'query': query,
       'user': query.profile,
       'post_user': post_user,
       'post_count': post_count,
       'connection' : connection,
    }
    template = "blog/search.html"
    return render(request, template, context)


# to follow functionality
@login_required(login_url='login')
def follow(request, username):
    main_user = request.user
    to_follow = User.objects.get(username = username)

    # check if already following
    following = Following.objects.filter(user= main_user, followed= to_follow)
    is_following = True if following else False

    if is_following:
        #then unfollow the user
        Following.unfollow(main_user, to_follow)
        is_following = False
    else:
        Following.follow(main_user, to_follow)
        is_following = True

    resp = {
        'following' : is_following,
    }

    response = json.dumps(resp)
    return HttpResponse(response, content_type="application/json")
