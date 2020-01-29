# -*- coding: utf-8 -*-
import telebot
import json
import requests
from keyboards import *
import transliterate
from queryToDataBase import *
import sqlite3

class Session:
    def __init__(self, chat_id, answer):
        self.chat_id = chat_id
        self.answer = answer

    def first():
        pass
