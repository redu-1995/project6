import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

TOKEN = '6948667240:AAGvY2ISTgt1_biBkQzoJ__BV7KDpdhz4L0'
bot = telebot.TeleBot(TOKEN)
CHANNEL_ID = '-1002129425239' 



def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div_container = soup.find('div', {'class': 'container'})
    if div_container is not None:
        img_tags = div_container.find_all('img')
        img_data = [{'src': tag['src'], 'alt': tag.find_next('div', {'class': 'product__content content--center'}).text.strip() if tag.find_next('div', {'class': 'product__content content--center'}) else 'No description available'} for tag in img_tags]
        return img_data
    else:
        return []


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Art and Music')
    itembtn2 = types.KeyboardButton('Technology')
    itembtn3 = types.KeyboardButton('Entertainment')
    itembtn4 = types.KeyboardButton('Parenting and Relationship')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Choose a type of book:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Art and Music')
def handle_button1(message):
    img_data = scrape_website('https://www.jaferbooks.com/category.php?category_name=Art%20and%20Music')
    for data in img_data:
        img_url = data['src']
        if not img_url.startswith('http'):
            img_url = 'https://www.jaferbooks.com/' + img_url
        try:
            response = requests.get(img_url)
            response.raise_for_status()
        except (requests.HTTPError, requests.ConnectionError):
            print(f"Unable to access image at {img_url}")
            continue
        bot.send_photo(CHANNEL_ID, img_url, caption=data['alt'])

@bot.message_handler(func=lambda message: message.text == 'Technology')
def handle_button2(message):
    img_data = scrape_website('https://www.jaferbooks.com/category.php?category_name=Technology')
    for data in img_data:
        img_url = data['src']
        if not img_url.startswith('http'):
            img_url = 'https://www.jaferbooks.com/' + img_url
        try:
            response = requests.get(img_url)
            response.raise_for_status()
        except (requests.HTTPError, requests.ConnectionError):
            print(f"Unable to access image at {img_url}")
            continue
        bot.send_photo(CHANNEL_ID, img_url, caption=data['alt'])

@bot.message_handler(func=lambda message: message.text == 'Entertainment')
def handle_button3(message):
    img_data = scrape_website('https://www.jaferbooks.com/category.php?category_name=Entertainment')
    for data in img_data:
        img_url = data['src']
        if not img_url.startswith('http'):
            img_url = 'https://www.jaferbooks.com/' + img_url
        try:
            response = requests.get(img_url)
            response.raise_for_status()
        except (requests.HTTPError, requests.ConnectionError):
            print(f"Unable to access image at {img_url}")
            continue
        bot.send_photo(CHANNEL_ID, img_url, caption=data['alt'])

@bot.message_handler(func=lambda message: message.text == 'Parenting and Relationship')
def handle_button4(message):
    img_data = scrape_website('https://www.jaferbooks.com/category.php?category_name=Parenting%20and%20Relationship')
    for data in img_data:
        img_url = data['src']
        if not img_url.startswith('http'):
            img_url = 'https://www.jaferbooks.com/' + img_url
        try:
            response = requests.get(img_url)
            response.raise_for_status()
        except (requests.HTTPError, requests.ConnectionError):
            print(f"Unable to access image at {img_url}")
            continue
        bot.send_photo(CHANNEL_ID, img_url, caption=data['alt'])



bot.polling()