from djoser.views import UserViewSet
from rest_framework.decorators import action
from djoser import signals
from djoser.conf import settings
from djoser.compat import get_user_email
from rest_framework.response import Response
from rest_framework import status


class CustomUserViewSet(UserViewSet):
    @action(["post"], detail=False)
    def activation(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user.is_active = True
        user.save()

        signals.user_activated.send(
            sender=self.__class__, user=user, request=self.request
        )

        if settings.SEND_CONFIRMATION_EMAIL:
            context = {"user": user}
            to = [get_user_email(user)]
            print('asdfasdfasdfwxr23x')
            settings.EMAIL.confirmation(self.request, context).send(to)

        return Response(status=status.HTTP_204_NO_CONTENT)
