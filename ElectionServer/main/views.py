from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import UserModel
from choice.models import ChoiceModel
from .serializers import UserSerializer
from election.models import ElectionModel

        
class UserModelView(ModelViewSet):
    queryset: UserModel = UserModel.objects.all()
    serializer_class: UserSerializer = UserSerializer
    
    @action(
        methods=['POST'],
        detail=False
    )
    def post_user_election(self, request: HttpRequest) -> Response:
        data: dict = request.POST
                
        id_card: str = data['id_card']
        election: str = data['election'][0]
        choice: str = data['choice'][0]
        
        user: UserModel = UserModel.objects.select_related('election').filter(id_card=id_card).first()
                
        if user:
            if user.election.id == int(election):
                return Response({'response': f'Пользователь уже учавствует в этом голосовании "{user.election.name}"'})

        try:
            election: ElectionModel = ElectionModel.objects.get(pk=election)
            choice: ChoiceModel = ChoiceModel.objects.get(pk=choice)
            
            UserModel.objects.create(id_card=id_card, election=election, choice=choice).save()
        except Exception as er:
            return Response({'response': er.args[0]})
        
        return Response({'response': 'Запись добавлена'})

    @action(
        methods=['GET'],
        detail=False
    )
    def get_user(self, request: HttpRequest) -> Response:
        data: dict = request.GET
        
        user_card_id: str | None = data.get('card_id')
        
        try:
            user: UserModel = UserModel.objects.select_related('election').select_related('choice').get(pk=user_card_id)
        except Exception:
            return Response({'response': 'Такого пользователя не существует или вы не передали параметр'})
        
        data_user = {
            'card_id': user.id_card,
            'election': user.election.name,
            'choice': user.choice.name
        }
        
        return Response({'response': {'user_info': data_user}})