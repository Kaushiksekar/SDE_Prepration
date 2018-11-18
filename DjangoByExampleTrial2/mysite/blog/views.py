from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.db.models import Count
from taggit.models import Tag
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm

def post_list(request, tag_slug=None):
    posts = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    return render(request, 'blog/post/list.html', {'posts': posts, 'tag': tag})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    print('post_tags_ids')
    print(post_tags_ids)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    print('similar_posts')
    print(similar_posts)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    print('similar_posts')
    print(similar_posts)

    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form, 'similar_posts': similar_posts})

def post_share(request, post_id):
    #Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)

            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])

            send_mail(subject, message, 'kaushik3993@gmail.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})
