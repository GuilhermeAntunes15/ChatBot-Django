from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


chatbot = ChatBot(
    'Charlie',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)


chatbot.train("chatterbot.corpus.portuguese")
chatbot.train("chatterbot.corpus.portuguese.greetings")
chatbot.train("chatterbot.corpus.portuguese.conversations")
'''
chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.english.greetings")
chatbot.train("chatterbot.corpus.english.conversations")'''


@csrf_exempt
def get_response(request):
    response = {'status': None}

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data['message']

        chat_response = chatbot.get_response(message).text
        response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
        response['status'] = 'ok'

    else:
        response['error'] = 'no post data found'

    return HttpResponse(
        json.dumps(response),
            content_type="application/json"
        )


def bot(request, template_name='chatbot.html'):
    context = {'title': 'Chatbot '}
    return render(request, template_name, context)