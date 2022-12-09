from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib import messages
from users.forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    
)
from blog.models import Post
from django.contrib.auth.models import User

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form})



class ProfilePostListView(ListView):
    model = Post
    template_name = 'users/profile_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

@login_required
def update_profile(request):

    if request.method=='POST':
        u_form= UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() 
            messages.success(request,f'Your account has been Updated!')
            return redirect('blog-home')
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context ={
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request,'users/update_profile.html',context)

