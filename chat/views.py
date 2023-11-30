from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ConversationSerializer
import os
import openai
from dotenv import load_dotenv
from .models import Conversation

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

class ChatbotView(APIView):
    permission_classes = [IsAuthenticated] 
    serializer_class = ConversationSerializer

    def get(self, request):
        conversations = Conversation.objects.filter(user=request.user)
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)

    def post(self, request):
        prompt = request.data.get('prompt')
        if prompt:
            session_conversations = Conversation.objects.filter(user=request.user)
            previous_conversations = "\n".join([f"User: {c.prompt}\nAI: {c.response}" for c in session_conversations])
            prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

            model_engine = "text-davinci-003"
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_with_previous,
                max_tokens=1024,
                n=5,
                stop=None,
                temperature=0.5,
            )
            response = completions.choices[0].text.strip()

            conversation = {'prompt': prompt, 'response': response}
            serializer = ConversationSerializer(data=conversation)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)