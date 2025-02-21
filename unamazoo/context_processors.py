from mainsite.models import Post

def institutional_pages(request):
    pages = Post.objects.filter(place='institutional_pages')
    return {'institutional_pages': pages}

def load_constants(request):
    context = {
        'CANONICAL_PATH': request.build_absolute_uri(request.path),
    }

    return context