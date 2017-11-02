from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import time
import threading
import random
import sqlite3

my_token = 'token'
my_db = 'raisa.db'

def open_connect_db ():
    global conn
    conn = sqlite3.connect (my_db)
    
def get_poem_db ():
    open_connect_db ()
    c = conn.cursor ()
    try:
        c.execute ("SELECT * FROM poems WHERE count_shows = ?",  str (0))
        row = c.fetchall ()
        poem = row[random.randint(0, len (row)-1)]
        text = "\n".join (poem[1].split ("\\n"))
        c.execute ("SELECT * FROM poems WHERE count_shows > 0")
        shown_arr = c.fetchall ()
        for sa in shown_arr:
            c.execute ("UPDATE poems SET count_shows = ? WHERE id = ?", (sa[2] - 1, sa[0],))
            conn.commit ()
            
        c.execute ("UPDATE poems SET count_shows = ? WHERE id = ?", (poem[2] + 10, poem[0],))
        conn.commit ()
    except sqlite3.DatabaseError as err:
        print ("Error: ", err)
    else:
        conn.commit ()
    close_connect_db ()
    return text
    
def close_connect_db ():
    conn.close ()

def handle_message (bot, update):
    msg_text = update.message.text
    msg_text = msg_text.lower ()
    if "валентина!" in msg_text:
        for word in words:
            if word in msg_text: 
                bot.sendMessage (chat_id=update.message.chat_id, text="Ой, ну хорошо, уговорили :)")
                bot.sendMessage (chat_id=update.message.chat_id, text=get_poem_db ())

words = [
    "стих",
    "стишок",
    "стишк",
    "рифм",
    "стишие",
    "стишье",
    "поэт",
    "поэзи",
    "литератур",
    "строк",
    "строчк",
    "классик",
]
  
conn = None
    
updater = Updater (token=my_token)
handler = MessageHandler (Filters.text | Filters.command, handle_message)
updater.dispatcher.add_handler (handler)
updater.start_polling ()
