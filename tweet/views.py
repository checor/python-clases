from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class AllTweets(LoginRequiredMixin, View):
    login_url = 'login/'
    def get(self, request):
        tweets = Tweet.objects.all().order_by('created_date').reverse()
        return render(request, 'tweet.html', {'tweets': tweets})


class NewTweet(View):
    def get(self, request):
        form = TweetForm()
        return render(request, 'tweet_edit.html', {'form': form})

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = request.user
            tweet.save()
            return redirect('/')
        else:
            form = TweetForm()
            return render(request, 'tweet_edit.html', {'form': form})


class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('/')
        else:
            return render(request, 'registration/signup.html', {'form': form})


# def new_tweet(request):
#     if request.method == "POST":
#         form = TweetForm(request.POST)  
#         tweet = form.save(commit=False)
#         tweet.author = request.user
#         tweet.save()
#         return redirect('/')
#     else:
#         form = TweetForm()
#     return render(request, 'tweet_edit.html', {'form': form})
