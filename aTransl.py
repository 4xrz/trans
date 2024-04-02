import telebot
from telebot import types
from kvsqlite.sync import Client
import requests

db = Client('t.hex')

b = types.InlineKeyboardMarkup(row_width=2)
ar = types.InlineKeyboardButton(text='العربية 🇸🇦',callback_data='ar')
en = types.InlineKeyboardButton(text='الانجليزية 🇺🇲',callback_data='en')
es = types.InlineKeyboardButton('الاسبانية 🇪🇦',callback_data='es')
b.add(ar,en)
b.add(es)



bot = telebot.TeleBot('6624779069:AAEs_84VO3Go457hpG2sdYWRhOzByEpFcaU')

@bot.message_handler(commands=['start'])
def start(m):
  fe = types.InlineKeyboardMarkup(row_width=2)
  dirt = types.InlineKeyboardButton(text='♪',url='rKKuu.t.me')
  fe.add(dirt)
  iid = m.from_user.id
  name = m.from_user.first_name
  ms = m.chat.id
  #db.set(f'n_{ms}',name)
  id = m.from_user.id
#	db.set(f'id_{iid}',id)
  dmj = f'[{m.from_user.first_name}](tg://user?id={m.from_user.id})'
 # db.set(f'n_{ms}',dmj)
  bot.reply_to(m,f'• اهلاً بك في بوت الترجمة ^-^ ،\n•ارسل الجملة ليتم ترجمتها ✓',
  reply_markup=fe)

@bot.message_handler(func=lambda m:True) 
def tr(m):
	text = 'اختر اللغة التي تريد ترجمة النص لها :'
	iid = m.from_user.id
	mm = m.text
	db.set(f'_{iid}',mm)
	bot.reply_to(m,text,reply_markup=b)
	
@bot.callback_query_handler(func=lambda call:True)
def tran(call):
	data = call.data
	n = call.message.reply_to_message.from_user.id
	te = db.get(f'_{n}')
	mm = call.message.text
	print(te)
	
	if data =='ar':
		bot.delete_message(call.message.chat.id , call.message.message_id)
		ra = requests.get(f'https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl=ar&q={te}').json()[0][0][0]
		bot.send_message(call.message.chat.id,text=ra)
	if data =='en':
		bot.delete_message(call.message.chat.id , call.message.message_id)
		rn = requests.get(f'https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl=en&q={te}').json()[0][0][0]
		bot.send_message(call.message.chat.id,text=rn)
	if data=='es':
		bot.delete_message(call.message.chat.id , call.message.message_id)
		rs = requests.get(f'https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl=es&q={te}').json()[0][0][0]
		print(rs)
		bot.send_message(call.message.chat.id,text=rs)
		
bot.infinity_polling()