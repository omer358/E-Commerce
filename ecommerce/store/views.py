import logging

from django.shortcuts import render


def store(request):
    logging.info(msg="store view")
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)