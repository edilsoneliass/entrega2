from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils.timezone import now

# Página inicial: lista de posts
def listar_posts(request):
    posts = Post.objects.order_by('-data_postagem')
    return render(request, 'listar_posts.html', {'posts': posts})

# Detalhes de um post
def detalhes_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detalhes_post.html', {'post': post})

# Criar novo post
def criar_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        if titulo and conteudo:
            Post.objects.create(titulo=titulo, conteudo=conteudo, data_postagem=now())
            return redirect('listar_posts')
    return render(request, 'form_post.html')

# Editar post
def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        if post.titulo and post.conteudo:
            post.save()
            return redirect('listar_posts')
    return render(request, 'form_post.html', {'post': post})

# Deletar post
def deletar_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('listar_posts')
    return render(request, 'confirmar_deletar.html', {'post': post})