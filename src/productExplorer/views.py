from django.shortcuts import render
from databaseModels.models import ObjectItem, ProductChain

# Create your views here.


def index(request):
    objectItems = ObjectItem.objects.filter(state__iexact='FIN')

    context = {
        "objectItems": objectItems,
    }

    return render(request, 'index.html', context=context)


def viewProduct(request, id=None):
    if id is None:
        return render(request, 'productChain.html', context=None)

    objectItem = ObjectItem.objects.filter(id_exact=id)
    chains = ProductChain.objects.filter(object__exact=objectItem)

    context = {
        "objectItem": objectItem,
        "chains": chains,
    }

    return render(request, 'productChain.html', context=context)
