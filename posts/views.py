from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post



""" Primeira parte de implementação de views com arquivos funcionais sem Django Forms"""
# Página inicial: lista de posts
def listar_posts(request):
    posts = Post.objects.order_by('-data_postagem')
    return render(request, 'posts/listar_posts.html', {'posts': posts})

# Detalhes de um post com exibição dos comentários
def detalhes_post(request, id):
    post = get_object_or_404(Post, id=id)
    comentarios = post.comments.order_by('-data_postagem')  # Ordenar por mais recente
    categorias = post.categorias.all()
    return render(request, 'posts/detalhes_post.html', {'post': post, 'comentarios': comentarios, 'categorias': categorias} )

# Criar novo post
def criar_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        if titulo and conteudo:
            Post.objects.create(titulo=titulo, conteudo=conteudo, data_postagem=now())
            return redirect('listar_posts')
    return render(request, 'posts/form_post.html')

# Editar post
def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        if post.titulo and post.conteudo:
            post.save()
            return redirect('listar_posts')
    return render(request, 'posts/form_post.html', {'post': post})

# Deletar post
def deletar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('listar_posts')
    return render(request, 'posts/confirmar_deletar.html', {'post': post})

# Página lista de categorias
def listar_categorias(request):
    categorias = Category.objects.all()
    return render(request, 'posts/listar_categorias.html', {'categorias': categorias})

# View individual de cada categoria
def detalhes_categoria(request, id):
    categoria = get_object_or_404(Category, id=id)
    posts = categoria.posts.order_by('-data_postagem')
    return render(request, 'posts/listar_posts.html', {'posts': posts, 'categoria': categoria})

# View para criar um comentário
@login_required
def criar_comentario(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        texto = request.POST.get('texto')
        if texto:
            Comment.objects.create(post=post, autor=request.user, texto=texto, data_postagem=now())
            return redirect('detalhes_post', id=post.id)
    return render(request, 'posts/form_comentario.html', {'post': post})

"""Segunda parte de implementação de views com Django Forms"""

"""# Criar um novo post
def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')
    else:
        form = PostForm()
    return render(request, 'posts/form_post.html', {'form': form})

# Editar um post existente
def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/form_post.html', {'form': form})

# Deletar post
def deletar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('listar_posts')
    return render(request, 'posts/confirmar_deletar.html', {'post': post})"""

"""Terceira parte de implementação de views genéricas"""

"""# Listar posts
class PostListView(ListView):
    model = Post
    template_name = 'posts/listar_posts.html'
    context_object_name = 'posts'
    ordering = ['-data_postagem']

# Detalhes do post
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detalhes_post.html'

# Criar post
class PostCreateView(CreateView):
    model = Post
    fields = ['titulo', 'conteudo']
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('listar_posts')

# Editar post
class PostUpdateView(UpdateView):
    model = Post
    fields = ['titulo', 'conteudo']
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('listar_posts')

# Deletar post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirmar_deletar.html'
    success_url = reverse_lazy('listar_posts')"""

