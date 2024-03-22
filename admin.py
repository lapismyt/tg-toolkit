'''
Powerful admin panel for Telegram bots using Telegram Web App powered by Flask.

Admin panel functions: edit database, give admin, delete admin, mailing, ban user, unban user, etc.
Admin rights connected to Telegram user.
Tonnel to admin panel via ngrok.
'''

# imports
import os
from flask import Flask, render_template, request, redirect, url_for
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


app = Flask(__name__)


@app.route('/admin')
def index():
    return render_template('admin.html')