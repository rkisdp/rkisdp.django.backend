# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

from contextlib import suppress

# lib imports
from rest_framework import permissions, status
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveDestroyAPIView)
from rest_framework.response import Response

# project imports
from common import constants, messages
from common.gateways import notification as notification_db_gateway
from common.models import DeviceToken, Notification
from common.serializers import DeviceTokenSerializer, NotificationSerializer


class ListNotificationView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    model = Notification
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id).order_by("modified_date")


class GetDeleteNotificationView(RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    model = Notification
    serializer_class = NotificationSerializer

    def get(self, request, *args, **kwargs):
        with suppress(Notification.DoesNotExist):
            notification_entity = notification_db_gateway.get_notification(
                pk=kwargs.get("pk"), user_id=self.request.user.id, type=constants.PUSH
            )
            serializer = self.serializer_class(notification_entity)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": messages.COMMON_NOTIFICATION_NO_OBJECT}, status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, *args, **kwargs):
        with suppress(Notification.DoesNotExist):
            notification_db_gateway.get_notification(
                pk=kwargs.get("pk"), user_id=self.request.user.id, type=constants.PUSH
            ).delete()
            return Response(
                {"detail": messages.COMMON_NOTIFICATION_DELETE}, status=status.HTTP_202_ACCEPTED
            )
        return Response(
            {"detail": messages.COMMON_NOTIFICATION_NO_OBJECT}, status=status.HTTP_404_NOT_FOUND
        )


class RegisterDeviceView(CreateAPIView):

    model = DeviceToken
    serializer_class = DeviceTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user.id, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {"detail": "Device Registered", "data": serializer.data}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
