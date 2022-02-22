import pymongo
from config import Config
#from admin import notify

def insert_into(first_name,chat_id,reg_name,user_name,reg_id):
	connect = pymongo.MongoClient(Config.MONGODB)

	grade12 = connect["grade12"]

	students = grade12["students"]

	toAdd = { "name": str(first_name), "chat_id": str(chat_id),"reg_id":str(reg_id),"reg_name":reg_name,"userName":user_name }

	students.insert_one(toAdd)

	#Config.ADMIN

	#notify(Config.ADMIN)