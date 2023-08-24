from chatbot import api
from chatbot.apis.Get_Response import Get_chatbot_respone

Chatbot = api.namespace('api/chatbot')
Chatbot.add_resource(Get_chatbot_respone, '/get_response')
