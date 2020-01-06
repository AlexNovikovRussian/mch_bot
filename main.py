#import requests as rq
import telebot
from bs4 import BeautifulSoup as BS
from requests_html import HTMLSession

bot = telebot.TeleBot("788640079:AAHD62n1KvZRhIGBJjYmryK075keL_XvsHM")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello, I am a mark cheking bot! Send me /get to get my marks!")

@bot.message_handler(content_types=['text'])
def get_command(message):
    if message.text == "get":

        session = HTMLSession()

        payload = {

            "isDelayed" : "false",
            "login" : "+79775543041",
            "password" : "14121416alex9",
            "notRememberMe" : "false"

        }

        b = session.post("https://login.mos.ru/sps/login/methods/password", data = payload)
        b.html.render(timeout=30000)

        resp = session.get("https://dnevnik.mos.ru")
        resp.html.render(timeout=30000)

        bs_dm = BS(resp.html.html, "html.parser")

        link = bs_dm.select('a[href*=\'login.mos.ru\']')[0]['href']
        
        bot.send_message(message.chat.id, link)

bot.polling()