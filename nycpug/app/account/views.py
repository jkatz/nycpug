from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login as auth_login, logout as auth_logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.decorators.debug import sensitive_post_parameters
from django.template import RequestContext

from nycpug.app.core.models import Conference
from .forms import *

@sensitive_post_parameters('password')
def login(request):
    """perform authentication"""
    conference = get_object_or_404(Conference, active=True)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            response = _perform_login(request, form)
            if isinstance(response, HttpResponse):
                return response
    else:
        form = LoginForm()
    return render_to_response('submit.html', {
        'conference': conference,
        'login_form': form,
        'signup_form': SignupForm(),
    }, RequestContext(request))

def logout(request):
    """logout"""
    auth_logout(request)
    return redirect(reverse('home'))

@sensitive_post_parameters('password')
def signup(request):
    """signup form for a new User"""
    conference = get_object_or_404(Conference, active=True)
    if request.user.is_authenticated(): # if user is authenticated, get out of here
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # create a new user and automatically log user in
            get_user_model().objects.create_user(
                form.cleaned_data.get('email'),
                form.cleaned_data.get('password'),
                name=form.cleaned_data.get('name'),
            )
            response = _perform_login(request, form)
            if isinstance(response, HttpResponse):
                return response
    else:
        form = SignupForm()
    return render_to_response('submit.html', {
        'conference': conference,
        'login_form': LoginForm(),
        'signup_form': form,
    }, RequestContext(request))

def _perform_login(request, form):
    """actually perform a login"""
    user = authenticate(
        email=form.cleaned_data['email'],
        password=form.cleaned_data['password'])
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            if request.session.get('next'):
                next = request.session.pop('next')
                return redirect(next)
            else:
                return redirect(reverse('home'))
        else:
            form.errors['__all__'] = 'This account has been deactivated.'
    else:
        form.errors['__all__'] = 'Could not log you in.  Please check your email address and password.'
