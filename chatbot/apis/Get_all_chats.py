from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from itertools import groupby

from chatbot import api
from chatbot import db
from chatbot.models.chatbot_db.chats import ChatsModel

# from chatbot.chat import get_response

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401


class Get_all_chats(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def get(self, user_id):
        
        try:
            #sort in ascending order of creation_time
            chat_history = ChatsModel.query.filter_by(user_id=user_id).order_by(ChatsModel.creation_time).all()
            chat_history = [x.json() for x in chat_history]

            #create json format
            chat_history_json = []
            for chat in chat_history:
                chat_history_json.append({
                    "id": chat["id"],
                    "user_id": chat["user_id"],
                    "msg_from": chat["msg_from"],
                    "message": chat["message"],
                    "creation_time": chat["creation_time"].strftime("%Y-%m-%d %H:%M:%S")
                })

            return jsonify(chat_history_json)
        
        except Exception as e:
            print({"message":"exception occured in Get_chatbot_respone"})
            print(e)
            return jsonify({"message":"exception occured in Get_chatbot_respone"})

        