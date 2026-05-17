# Simple URl Shortener 

-----

That Html, css ,js all AI generative i just the basic stuff and let ai generate other things 

-----

> This is simple 
first i take the URL using POST method and then i generate a random short url using random.choice

FUN Part\

check if that short url already exists in the database, 

if exists then generate new short url "cuz there will be clash in dataBase for that short url"

else
    store the original url and new short url in the database
    return the full short url with "http://localhost:8000/" + short_url

so User can click on the URL or copy 