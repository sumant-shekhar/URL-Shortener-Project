from django.shortcuts import render, redirect
from .models import URL
import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=length))

def create_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('link')
        if original_url:
            # Check if URL already exists to avoid duplicates
            url_obj, created = URL.objects.get_or_create(
                url=original_url,
                defaults={'uuid': generate_random_string(6)}
            )
            # Build the absolute URL for the user to copy
            short_url = f"{request.scheme}://{request.get_host()}/{url_obj.uuid}"
            return render(request, 'index.html', {'short_url': short_url})
    return render(request, 'index.html')

def redirect_url(request, uuid):
    try:
        url_details = URL.objects.get(uuid=uuid)
        return redirect(url_details.url)
    except URL.DoesNotExist:
        return render(request, 'index.html', {'error': 'URL not found'})

        