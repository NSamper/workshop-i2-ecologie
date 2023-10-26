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

    current_node = ProductChain.objects.filter(objectItem__id__exact=objectItem.id)

    first_mail = current_node.exclude(lastStep__objectItem__id__exact=objectItem.id).first()
    last_mail = current_node.exclude(nextStep__objectItem__id__exact=objectItem.id).first()

    if first_mail is not None and last_mail is not None:

        next_node_objects = ProductChain.objects.filter(nextStep__id__exact=first_mail.id)
        last_node_objects = ProductChain.objects.filter(lastStep__id__exact=last_mail.id)

        chain = []
        i = 1
        done = False

        chain.append(first_mail)

        while not done:
            next_mail = current_node.get(pk=chain[-1].nextStep.id)

            if next_mail.id == last_mail.id:
                done = True

            chain.append(current_node.get(pk=chain[-1].nextStep.id))
            i += 1

    else:
        chain = None
        next_node_objects = None
        last_node_objects = None

    print(chain)
    context = {
        "objectItem": objectItem,
        "chain": chain,
        "next_nodes": list(next_node_objects),
        "last_nodes": list(last_node_objects)
    }

    return render(request, 'productChain.html', context=context)
