from django.shortcuts import render
import re  
import time 
import instaloader
from datetime import datetime
from .models import Event
from django.http import HttpResponse



def extract_time_and_place(text):
    month_names = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]

    date = None
    place = None
    time = None
    date_month = None
    date_day = None
    courpus = None

    try:

        sentences = text.split("\n")
    except AttributeError:
        return None
    name = sentences[0]
      

    for sentence in sentences:
        for month in month_names:
            if month in sentence:
                date = re.search(r"\d{1,2}." + month, sentence)
                if date:
                    date = date.group()
                    date_month = month_names.index(month)+1
                    date_day = date.split()[0]
        if not time:
            time = re.search(r"\d{2}[:.]\d{2}", sentence)  

            if time:
                time = time.group()

        if "корпус" in sentence:
            place = re.search(r"\d{1}.{0,4}корпус", sentence)
            if place:
                courpus = place.group()[0]
            else:
                place = re.search(r"корпус.{0,4}\d{1}", sentence)

                if place:
                    courpus = place.group()[-1]
                else:
                    place = re.search(r"\d\d\d-\d", sentence)
                    if place:
                        courpus = place.group()[-1]

    if not time: 
        return None
    if not courpus:
        return None
    if not date_month:
        return None
    if not date_day:
        return None


    return {'month': date_month, 'day': int(date_day), 'time': time, 'building': courpus, 'name': name}



def index(request):
    bot = instaloader.Instaloader()
    bot.login(user="_d_i_n_o_z_a_v_r_i_k__", passwd="K1944A2NHE_N")

    profile = instaloader.Profile.from_username(bot.context, 'fcad_bsuir')

    posts = profile.get_posts() 

    target_date = datetime(2024, 1, 1)  

    for index, post in enumerate(posts, 1):
        if post.date > target_date:
            print(f"Post {index}:")
            post_url = f"https://www.instagram.com/p/{post.shortcode}/"
            try:
                event = extract_time_and_place(post.caption)
                Event.objects.create(
                name=event['name'], 
                date=datetime(year=2024, month=event['month'], day=event['day']), 
                time=event['time'], 
                university_building=event['building'], 
                description=post.caption, 
                faculty="FCAD",
                date_time_post=post.date,
                url=post_url) 
            except TypeError:
                pass

    return HttpResponse("Ich bin fertig!!")