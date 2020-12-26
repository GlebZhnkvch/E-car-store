from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from ads.forms import AdForm
from ads.models import Ad
from django.shortcuts import render
from django.conf import settings


@login_required
def create(request):
    page = request.GET.get("page", 1)
    ads = Ad.objects.filter().order_by("-created_at")
    p = Paginator(ads, settings.ITEMS_PER_PAGE)
    if request.method == 'GET':
        ads = Ad.objects.all()
        form = AdForm()
        return render(request, 'create.html', context={
            "form": form,
            'page': p.page(page),
        })
    elif request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            form.save()
            return render(request, 'create_success.html', context={
                'page': p.page(page),
            })
        else:
            return render(request, 'create.html', context={
                "form": form,
                'page': p.page(page),
            })


def all_ads(request):
    query = request.GET.get("q", "")
    page = request.GET.get("page", 1)
    ads = Ad.objects.filter(Q(brand__name__icontains=query) | Q(car_model__icontains=query)).order_by("-id")
    p = Paginator(ads, settings.ITEMS_PER_PAGE)
    return render(request, 'ads.html', context={
        'page': p.page(page)
    })


def retrieve(request, id=None):
    ad = Ad.objects.get(pk=id)
    return render(request, 'retrieve.html', context={
        'ad': ad,
    })


def delete(request, id=None):
    page = request.GET.get("page", 1)
    ads = Ad.objects.filter().order_by("-created_at")
    p = Paginator(ads, settings.ITEMS_PER_PAGE)
    Ad.objects.filter(pk=id).delete()
    return render(request, 'delete_success.html', context={
        'page': p.page(page),
    })
