from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm

# Create your views here.
def get_all_tweets(request):
    tweets = Tweet.objects.all().order_by('created_date').reverse()
    return render(request, 'tweet.html', {'tweets': tweets})

def new_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST)  
        tweet = form.save(commit=False)
        tweet.author = request.user
        tweet.save()
        return redirect('/')
    else:
        form = TweetForm()
    return render(request, 'tweet_edit.html', {'form': form})
