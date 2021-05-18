from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')
def success(request):
    return redirect('/wall')    
def register(request):
    errors=Users.objects.count_Vald(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    password = request.POST['pw_input']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    new_user = Users.objects.create(
        first_name = request.POST['first_name_input'],
        last_name = request.POST['last_name_input'],
        email = request.POST['email_input'],
        password = pw_hash,
        birthdate = request.POST['bday_input']
    )
    request.session['user_id'] = new_user.id
    return redirect('/success')
def log(request):
    user = Users.objects.filter(email=request.POST['email_input']) 
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['pw_input'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/success')
        return redirect("/success")
    else:
        return redirect('/')
    return redirect('/success')

def delete(request, val):
    this_post = Messages.objects.get(id=val)
    this_post.delete()
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')

def message(request):
    Messages.objects.create(
        user_id= Users.objects.get(id=request.session['user_id']),
        message = request.POST['new_message']
    )
    return redirect('/wall')
def wall(request):
    context ={
        'logged_in': Users.objects.get(id=request.session['user_id']),
        'messages_db': Messages.objects.all(),
        'comments_listed' : Comments.objects.all()
    }
    return render(request, 'wall.html', context)

def comments (request, val):
   Comments.objects.create(
       message_id=Messages.objects.get(id=val),
       commenting_user = Users.objects.get(id=request.session['user_id']),
       comment = request.POST['commet_to_post']
   )
   return redirect('/wall')