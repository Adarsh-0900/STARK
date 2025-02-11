import telebot
import os
from yt_dlp import YoutubeDL
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🎵 This music bot is made by @MR_ADARSH_YTs\n\nSend me a YouTube link to download music!")

@bot.message_handler(commands=['stark'])
def play(message):
    bot.send_message(message.chat.id, "🎶 Playing music...")

@bot.message_handler(commands=['starkop'])
def skip(message):
    bot.send_message(message.chat.id, "⏭ Skipping to next track...")

@bot.message_handler(commands=['starkji'])
def stop(message):
    bot.send_message(message.chat.id, "⏹ Stopping music...")

@bot.message_handler(func=lambda message: "youtube.com" in message.text or "youtu.be" in message.text)
def download_audio(message):
    url = message.text
    bot.send_message(message.chat.id, "🎶 Downloading audio... Please wait.")

    options = {
        'format': 'bestaudio/best',
        'outtmpl': 'music.%(ext)s',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
    }

    with YoutubeDL(options) as ydl:
        ydl.download([url])

    for file in os.listdir():
        if file.endswith(".mp3"):
            bot.send_audio(message.chat.id, open(file, "rb"))
            os.remove(file)

bot.polling()
