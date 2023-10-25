from django.shortcuts import render
from databaseModels.models import ObjectItem, ProductChain

# Create your views here.


def index(request):
    objectItems = ObjectItem.objects.filter(state__iexact='FIN')

    context = {
        "objectItems": objectItems,
    }

    return render(request, 'index.html', context=context)


def viewProduct(request, id):

    objectItem = ObjectItem.objects.filter(id__exact=id).first()
    all_mail = ProductChain.objects.filter(object__id__exact=objectItem.id)


    chain = []
    for mail in all_mail:
        pass


    context = {
        "objectItem": objectItem,
        "chains": all_mail,
    }

    return render(request, 'productChain.html', context=context)
