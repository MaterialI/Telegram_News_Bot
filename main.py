from email import message
from numpy import source
import telebot
import telegram
import requests
from bs4 import BeautifulSoup
import os
import dead_orks
source = requests.get('https://armyinform.com.ua/tag/hronika-oborony/').text
soup = BeautifulSoup(source, 'lxml')

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands =["help","h","hello"])
def help(message):
    bot.reply_to(message, "no))")

@bot.message_handler(commands=['start'])
def start(message):
    f = open('start_txt.txt', "r")
    text  = f.read()
    bot.reply_to(message,text)
    f.close()

@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, "You are breathtaking "+ '\U0001F916')

@bot.message_handler(commands=["noot_noot"])
def noot(message):
    bot.reply_to(message, "https://www.youtube.com/watch?v=uDQwkvgBTpo")

@bot.message_handler(commands = ['info'])
def get_info(message):
    i = 0 
    for post in soup.find_all('div', class_ = 'archive-list'):
        link = post.find('a', href = True)
        bot.reply_to(message, post.text + link['href'])
        i+=1
        if(i==3):
            break

@bot.message_handler(commands = 'dead')
def dead(message):
    inf = dead_orks.Site()
    bot.reply_to(message, inf.info())

@bot.message_handler(commands=['sources'])
def sources(message):
    fi = open("sources.txt","r") 
    bot.reply_to(message, fi.read())
    fi.close()
@bot.message_handler(commands=['nik'])
def nik(massage):
    for i in range (0,100):
        bot.reply_to(message, "@nikitosiktb")
@bot.message_handler(commands=['drugs'])
def sources(message):
    bot.reply_to(message, "Чат підтримує академічну доброчесність та проти вживання наркотиків"+"\n"+"https://www.bccannabisstores.com/"+'\n'+"https://en.cannabisstoreamsterdam.com/")
def main():
    bot.polling()   

if __name__ == '__main__':
    main()
 
