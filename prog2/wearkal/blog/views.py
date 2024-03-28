from django.shortcuts import render

def home(request): 

    posts = (BlogPost.objects
                .filter(is_published=True)                
                .order_by('-pub_date')[:10]            
    )



 # o n l y p u b l i s h e d p o s t s
    data = {        
        'blog_posts': posts    
    }
    return render(request, 'blog/home.html', data)


def blog_post_view(request, post_id):    
    blog_post = BlogPost.objectss.get(id=post_id)          
    data = {        
        'post': blog_post    
    }
    return render(request, 'blog/blog-post-view.html', data)

    

# Create your views here.
