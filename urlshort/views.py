from django.shortcuts import render, redirect
import string
import random

from .models import Link

def index(request):
    if request.method == 'POST':
        link = request.POST.get('link', '').strip()

        if Link.objects.filter(original_url=link).exists():

            short_code = Link.objects.get(original_url=link).short_url

            full_short_url = request.build_absolute_uri('/') + short_code

            return render(request, "index.html", {"short_url": full_short_url})

        chars = string.ascii_letters + string.digits

        while True:

            short_code = ''.join(random.choice(chars) for _ in range(random.randint(4, 7)))
                
            if not Link.objects.filter(short_url=short_code).exists():
                break

        Link.objects.create(
            original_url=link, 
            short_url=short_code,
            )

        full_short_url = request.build_absolute_uri('/') + short_code

        return render(request, "index.html", {"short_url": full_short_url})

    return render(request, "index.html")

def redirect_url(request, short_url):
    try:
        link_obj = Link.objects.get(short_url=short_url)
        url = link_obj.original_url
        return redirect(url)
    except Link.DoesNotExist:
        return render(request, "index.html", {"error": "Invalid"})