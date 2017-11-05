# -*- coding: utf-8 -*-
import redis
import os
import telebot
import json
from time import localtime,strftime
from pprint import pprint
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
bot = telebot.TeleBot(token);

#funcao que é chamada quanto o texto da mensagem comeca com '\start'
@bot.message_handler(commands=['start','hello'])
def command_start(message):
	#jsonMensagem 	= json.loads(message)
	#textoResposta 	= ''.join('Ola', jsonMensagem['message']['user']['first_name'])
	bot.reply_to(message, 'Ola '+message.from_user.first_name+', esta e a mensagem de boas vindas.')
	pass
#funcao que é chamada quanto o texto da mensagem comeca com '\time'
@bot.message_handler(commands=['time'])
def command_time(message):
	bot.reply_to(message, strftime("%d/%m/%Y -  %H:%M (%A)",localtime()))
	pass

@bot.message_handler(commands=['universo'])
def command_time(message):
	bot.send_message(message.chat.id, '42 é a resposta para a vida, o universo e tudo mais.')
	pass

#funcao que é chamada quanto o texto da mensagem comeca com for diferente dos comandos especificados
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, 'Mensagem recebida: '+'"'+message.text+'"')
    pass


#faz com que o bot fique procurando por atualizações no servidor do telegram
bot.polling()          ...
