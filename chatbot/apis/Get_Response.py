from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from itertools import groupby

from chatbot import api
from chatbot.chat import get_response

class Get_chatbot_respone(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):
        user_message = request.json['user_message']
        print(user_message)
        response = get_response(user_message)
        bot_response = {
            "bot_response": response
        }

        return jsonify(bot_response)

        