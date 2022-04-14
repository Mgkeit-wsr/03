from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import jobget
import json

class Strings:
    token = '5345411624:AAHJWU5S4AvCYk6229r1AWyExMgZL_ao3r8'

class Keys:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Конец',callback_data='end'))

class Data:
    def request(age,gender,exp):
        data_list = json.loads(jobget.request(age,gender,exp)).get('objects')
        return data_list
    def by_id(id,age,gender,exp):
        data_by_id = Data.request(age,gender,exp)[id]
        return data_by_id.get('profession')+'\n'+data_by_id.get('client').get('title')+'\n'+data_by_id.get('type_of_work').get('title')+'.\n<b>Ссылка:</b> '+data_by_id.get('link')