from django.shortcuts import render
from .forms import TweetForm, UserRegistrationForm
from .models import Tweet
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

@login_required
def tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('all_tweets')
    else:
        form = TweetForm()
    return render(request, 'tweet/tweet.html', {'form' : form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('all_tweets')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet/tweet.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('all_tweets')
    return render(request, 'tweet/tweet_confirm_delete.html', {'tweet' : tweet})

def all_tweets(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/all_tweets.html', {'tweets': tweets})

def register(request):
    if request.method == "POST":
        print("register posted::::::::::::")
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('all_tweets')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})