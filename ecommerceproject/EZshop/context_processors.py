from .models import Category,Product
def Menu_links(request):
    links=Category.objects.all()
    return dict(links=links)
