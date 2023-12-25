#!/usr/bin/python
# -*- coding: cp1251 -*-
import telebot
from telebot import types
bot = telebot.TeleBot('6445641755:AAEIPXZpUEGjNfdbuOYNDKxclKmfajr5BfM')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text.upper() == "������":
         keyboard = types.InlineKeyboardMarkup();
         key_cat = types.InlineKeyboardButton(text='�����', callback_data='cat');
         keyboard.add(key_cat); 
         key_dog= types.InlineKeyboardButton(text='������', callback_data='dog');
         keyboard.add(key_dog);
         key_parrot= types.InlineKeyboardButton(text='�������', callback_data='parrot');
         keyboard.add(key_parrot)
         bot.send_message(message.from_user.id, "������, ���������� � ����� �������� ��� ����������?",reply_markup=keyboard)
    elif message.text == "/help":
         bot.send_message(message.from_user.id, "������ ������")
    else:
         bot.send_message(message.from_user.id, "� ���� �� �������. ������ /help.")

def get_information(call,animal):
    
    if animal =='cat':
        animal_text = '�����'
    elif animal =='dog':
        animal_text = '������'
    elif animal =='parrot':
        animal_text = '�������'
    
    keyboard = types.InlineKeyboardMarkup();  
    key_age = types.InlineKeyboardButton(text='����������������� �����', callback_data='age_'+animal)
    keyboard.add(key_age);
    key_names = types.InlineKeyboardButton(text='��������� �����', callback_data='names_'+animal)
    keyboard.add(key_names);
    key_action = types.InlineKeyboardButton(text='��� ������ ����� ����� ������?', callback_data='action_'+animal)
    keyboard.add(key_action);
    bot.send_message(call.message.chat.id, "����� ���������� � "+animal_text+" ��� ����������?",reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "cat" or call.data == "dog" or call.data == "parrot":
        get_information(call,call.data)
    elif call.data == 'age_cat':
        bot.send_message(call.message.chat.id, "����������������� ����� ����� ����� 0-38 ���.")
    elif call.data == 'age_dog':
        bot.send_message(call.message.chat.id, "����������������� ����� ����� ����� 0-30 ���.")
    elif call.data == 'age_parrot':
        bot.send_message(call.message.chat.id, "����������������� ����� �������� ����� 0-83 ���.")
    elif call.data == 'names_cat':
        bot.send_message(call.message.chat.id, "��������� ����� �����: ����, ��������, �����.")
    elif call.data == 'names_dog':
        bot.send_message(call.message.chat.id, "��������� ����� �����: �����, ���, �����.")
    elif call.data == 'names_parrot':
        bot.send_message(call.message.chat.id, "��������� ����� ��������: �����, ����.")
    elif call.data == 'action_cat':
        bot.send_message(call.message.chat.id, "����� ����� ����, ����� � ���������.")
    elif call.data == 'action_dog':
        bot.send_message(call.message.chat.id, "������ ����� ����, ������ � ������.")
    elif call.data == 'action_parrot':
        bot.send_message(call.message.chat.id, "������� ����� �����.")    

bot.polling(none_stop=True, interval=0)
