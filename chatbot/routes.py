from chatbot import api
from chatbot.apis.Get_Response import Get_chatbot_respone
from chatbot.apis.Get_all_chats import Get_all_chats

Chatbot = api.namespace('api/chatbot')
Chatbot.add_resource(Get_chatbot_respone, '/get_response')
Chatbot.add_resource(Get_all_chats, '/get_all_chats/<int:user_id>')