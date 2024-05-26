from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib.auth.decorators import permission_required, login_required
from datetime import datetime 
from blog.models import*



from blog.forms import PatronForm, couturierForm,MaisonCoutureForm,SearchForm

def home(request): 
    posts = (patron.objects
                .filter(is_published=True)                
                .order_by('-pub_date')[:10]            
    )
    data = {        
    'blog_posts': posts    
    }
    return render(request, 'blog/home.html', data)

def blog_post_view(request, post_id):    
    blog_post = patron.objects.get(id=post_id)          
    data = {        
    'post': blog_post    
    }
    return render(request, 'blog/blog-post-view.html', data)

def blog_post_detail(request, post_id):    
    blog_post = get_object_or_404(patron, id=post_id) 
    data = {        
        'post': blog_post    
    }
    return render(request, 'blog/blog-post-detail.html', data)

@login_required        
@permission_required('blog:add_blogpost', raise_exception=True) 
def blog_post_add(request):   
    if request.method == "POST":        
        form = PatronForm(request.POST, request.FILES)        
        if form.is_valid():            
            return redirect(form.save())  # r e d i r e c t s t o b l o g _ p o s t . g e t _ a b s o l u t e _ u r l ( )
    else:        
        form = PatronForm()
    return render(request, 'blog/blog-post-add.html', { 'form': form })

@permission_required('blog.change_blogpost', raise_exception=True)
def blog_post_change(request, post_id):    
    post = get_object_or_404(patron, id=post_id) # N e e d t o f e t c h t h e s p e c i f i c o b j e c t    
    
    if request.method == "POST":        
        form = PatronForm(request.POST, request.FILES, instance=post)        
        if form.is_valid():  
                      
            post = form.save()   # T h i s w i l l u p d a t e t h e o b j e c t            
            return redirect('/blog/')
    else:        
        form = PatronForm(instance=post)
    return render(request, 'blog/blog-post-change.html', { 'form': form, 'post': post }) 

@permission_required('blog.delete_blogpost', raise_exception=True) 
def blog_post_delete(request, post_id):    
    post = get_object_or_404(patron, id=post_id)    
    if request.method == "POST":        
        post.delete()        
        return redirect('/blog/')
    return render(request, 'blog/blog-post-delete.html', { 'post': post })


def blog_post_publish(request, post_id):    
    post = get_object_or_404(patron, id=post_id)    
    if request.method == "POST":        
        post.is_published = True        
        post.pub_date = datetime.now()        
        post.save()
    # R e d i r e c t t o t h e p o s t ' s d e t a i l p a g e    
    return redirect(post)
#----------------------------------------------------------------------

def cout_home(request): 
    posts = couturier.objects.all()         
    data = {        
    'couturiers': posts    
    }
    return render(request, 'blog/cout-home.html', data)
def cout_view(request, id):    
    posts = couturier.objects.get(id=id)          
    data = {        
    'couturier': posts    
    }
    return render(request, 'blog/cout-view.html', data)
def cout_delete(request, id):    
    post = get_object_or_404(couturier, id=id)    
    if request.method == "POST":        
        post.delete()        
        return redirect('blog:cout-home')
    return render(request, 'blog/cout-delete.html', { 'post': post })

#------------------------------------------------------------------------------------------------------

def maisoncouture_list(request):
    maison = MaisonCouture.objects.all()
    data ={
        'maisons' : maison
    }
    return render(request, 'blog/maison_home.html', data)

def maisoncouture_detail(request, maison_id):
    maison = MaisonCouture.objects.get(id=maison_id) 
    data = {
        'atelier': maison
    }
    return render(request, 'blog/maison_detail.html', data)

@login_required
@permission_required('blog:add_maisoncouture', raise_exception=True)
def maisoncouture_add(request):
    if request.method == "POST":
        form = MaisonCoutureForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect(form.save())  # Redirige vers la page détails de la maison
    else:
        form = MaisonCoutureForm()
    return render(request, 'blog/maison_add.html', {'form': form})

@permission_required('blog:change_maisoncouture', raise_exception=True)
def maisoncouture_change(request, maison_id):
    maison = get_object_or_404(MaisonCouture, id=maison_id)
    if request.method == "POST":
        form = MaisonCoutureForm(request.POST, request.FILES, instance=maison)
        if form.is_valid():
            maison = form.save()
            return redirect('/blog/atelier/')
    else:
        form = MaisonCoutureForm(instance=maison)
    return render(request, 'blog/maison_change.html', {'form': form, 'maison': maison})

@permission_required('blog:delete_maisoncouture', raise_exception=True)
def maisoncouture_delete(request, maison_id):
    maison = get_object_or_404(MaisonCouture, id=maison_id)
    if request.method == "POST":
        maison.delete()
        return redirect('/blog/atelier/')
    return render(request, 'blog/maison_delete.html', {'maison': maison})
#------------------------------------------------------------------------------------
def search_view(request):
    form = SearchForm(request.GET)
    results = []
    
    if form.is_valid():
        query = form.cleaned_data['query']
        results = couturier.objects.filter(nom_complet__icontains=query)
    
    return render(request, 'blog/result.html', {'form': form, 'results': results})