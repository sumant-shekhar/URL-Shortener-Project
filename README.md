# Simple URl Shortener 

-----
That Html, css ,js all AI generative i just typed basic stuff and let ai generate other things 
-----

> This is simple 
first: take the URL using POST method.

second: generate a random short url using random.choice.    "chars = string.ascii_letters + string.digits"

FUN Part

check if the generated short url already exists in the database.
    if it exists then generate new short url "cuz there will be clash in dataBase for that short url"

else 
    store the original url and new short url in the database
    return the full short url with "http://localhost:8000/" + short_url

so User can click on the URL or copy 
redirect work like this 
"full_short_url = request.build_absolute_uri('/') + short_code"
"link_obj = Link.objects.get(short_url=short_url)"