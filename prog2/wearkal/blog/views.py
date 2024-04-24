from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib.auth.decorators import permission_required, login_required
from datetime import datetime 
from blog.models import*
from blog.forms import BlogPostForm

def home(request): 
    posts = (BlogPost.objects
                .filter(is_published=True)                
                .order_by('-pub_date')[:10]            
    )
    data = {        
    'blog_posts': posts    
    }
    return render(request, 'blog/home.html', data)

def blog_post_view(request, post_id):    
    blog_post = BlogPost.objects.get(id=post_id)          
    data = {        
    'post': blog_post    
    }
    return render(request, 'blog/blog-post-view.html', data)

def blog_post_detail(request, post_id):    
    blog_post = get_object_or_404(BlogPost, id=post_id) 
    data = {        
        'post': blog_post    
    }
    return render(request, 'blog/blog-post-detail.html', data)


@login_required        
@permission_required('blog:add_blogpost', raise_exception=True) 
def blog_post_add(request):    
    if request.method == "POST":        
        form = BlogPostForm(request.POST)        
        if form.is_valid():            
            blog_post = form.save()            
            return redirect(blog_post)  # r e d i r e c t s t o b l o g _ p o s t . g e t _ a b s o l u t e _ u r l ( )
    else:        
        form = BlogPostForm()
    return render(request, 'blog/blog-post-add.html', { 'form': form })


@permission_required('blog:change_blogpost', raise_exception=True)
def blog_post_change(request, post_id):    
     post = get_object_or_404(BlogPost, id=post_id) # N e e d t o f e t c h t h e s p e c i f i c o b j e c t    
     if request.method == "POST":        
        form = BlogPostForm(request.POST, instance=post)        
        if form.is_valid():            
            blog_post = form.save()   # T h i s w i l l u p d a t e t h e o b j e c t            
            return redirect('/blog/')
        else:        
            form = BlogPostForm(instance=post)
        return render(request, 'blog/blog-post-change.html', { 'form': form, 'post': post }) 




@permission_required('blog.delete_blogpost', raise_exception=True) 
def blog_post_delete(request, post_id):    
    post = get_object_or_404(BlogPost, id=post_id)    
    if request.method == "POST":        
        post.delete()        
        return redirect('/blog/')
    return render(request, 'blog/blog-post-delete.html', { 'post': post })


def blog_post_publish(request, post_id):    
    post = get_object_or_404(BlogPost, id=post_id)    
    if request.method == "POST":        
        post.is_published = True        
        post.pub_date = datetime.now()        
        post.save()
    # R e d i r e c t t o t h e p o s t ' s d e t a i l p a g e    
    return redirect(post)





    

# Create your views here.
