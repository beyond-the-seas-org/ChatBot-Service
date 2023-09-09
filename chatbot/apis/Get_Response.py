from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from itertools import groupby
import datetime

from chatbot import api
from chatbot import db
from chatbot.models.chatbot_db.chats import ChatsModel

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401


# from chatbot.chat import get_response
from chatbot.chat_gpt import get_response_gpt

class Get_chatbot_respone(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def post(self):
        user_message = request.json['user_message']
        user_id = request.json['user_id']
        print(user_message)
        response = get_response_gpt(user_message)
        print("Chatbot response: ", response)
        bot_response = {
            "bot_response": response
        }

        # Save to database
        try:

            #create new field object
            new_user_chat = ChatsModel()
            new_user_chat.user_id = user_id
            new_user_chat.msg_from = "user"
            new_user_chat.message = user_message
            new_user_chat.creation_time = datetime.datetime.now()

            db.session.add(new_user_chat)
            db.session.commit()

            #new bot chat
            new_bot_chat = ChatsModel()
            new_bot_chat.user_id = user_id
            new_bot_chat.msg_from = "bot"
            new_bot_chat.message = response
            new_bot_chat.creation_time = datetime.datetime.now()

            db.session.add(new_bot_chat)
            db.session.commit()

            return jsonify(bot_response)
        except Exception as e:
            print({"message":"exception occured in Get_chatbot_respone"})
            print(e)
            return jsonify({"message":"exception occured in Get_chatbot_respone"})

        