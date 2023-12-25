#!/usr/bin/python
# -*- coding: cp1251 -*-
import telebot
from telebot import types
bot = telebot.TeleBot('6445641755:AAEIPXZpUEGjNfdbuOYNDKxclKmfajr5BfM')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text.upper() == "ПРИВЕТ":
         keyboard = types.InlineKeyboardMarkup();
         key_cat = types.InlineKeyboardButton(text='Кошка', callback_data='cat');
         keyboard.add(key_cat); 
         key_dog= types.InlineKeyboardButton(text='Собака', callback_data='dog');
         keyboard.add(key_dog);
         key_parrot= types.InlineKeyboardButton(text='Попугай', callback_data='parrot');
         keyboard.add(key_parrot)
         bot.send_message(message.from_user.id, "Привет, информация о каких животных вас интересует?",reply_markup=keyboard)
    elif message.text == "/help":
         bot.send_message(message.from_user.id, "Напиши привет")
    else:
         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def get_information(call,animal):
    
    if animal =='cat':
        animal_text = 'кошке'
    elif animal =='dog':
        animal_text = 'собаке'
    elif animal =='parrot':
        animal_text = 'попугае'
    
    keyboard = types.InlineKeyboardMarkup();  
    key_age = types.InlineKeyboardButton(text='Продолжительность жизни', callback_data='age_'+animal)
    keyboard.add(key_age);
    key_names = types.InlineKeyboardButton(text='Возможные имена', callback_data='names_'+animal)
    keyboard.add(key_names);
    key_action = types.InlineKeyboardButton(text='Что больше всего любят делать?', callback_data='action_'+animal)
    keyboard.add(key_action);
    bot.send_message(call.message.chat.id, "Какая информация о "+animal_text+" вас интересует?",reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "cat" or call.data == "dog" or call.data == "parrot":
        get_information(call,call.data)
    elif call.data == 'age_cat':
        bot.send_message(call.message.chat.id, "Продолжительность жизни кошек около 0-38 лет.")
    elif call.data == 'age_dog':
        bot.send_message(call.message.chat.id, "Продолжительность жизни собак около 0-30 лет.")
    elif call.data == 'age_parrot':
        bot.send_message(call.message.chat.id, "Продолжительность жизни попугаев около 0-83 лет.")
    elif call.data == 'names_cat':
        bot.send_message(call.message.chat.id, "Возможные имена кошек: Маша, Василиса, Томас.")
    elif call.data == 'names_dog':
        bot.send_message(call.message.chat.id, "Возможные имена собак: Бобик, Гай, Шанти.")
    elif call.data == 'names_parrot':
        bot.send_message(call.message.chat.id, "Возможные имена попугаев: Толик, Кеша.")
    elif call.data == 'action_cat':
        bot.send_message(call.message.chat.id, "Кошки любят есть, спать и гладиться.")
    elif call.data == 'action_dog':
        bot.send_message(call.message.chat.id, "Собаки любят есть, гулять и играть.")
    elif call.data == 'action_parrot':
        bot.send_message(call.message.chat.id, "Попугаи любят орать.")    

bot.polling(none_stop=True, interval=0)
