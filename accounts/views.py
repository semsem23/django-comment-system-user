# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserCreationForm, CommentForm
from .models import Post, Author, Comment

class TopicListView(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'
 
    def get_queryset(self):
        return Post.objects.order_by('-published_date')
        
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'news/post_detail.html', {'post': post,
                                                     'form': form})
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('news')
    template_name = 'registration/signup.html'
    
