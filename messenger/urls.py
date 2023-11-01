from django.urls import path
from .views import (
    MessageTemplateView,
    MessageCreateView,
    SentMessageListView,
    MessageDetailView,
    ReceivedMessageListView,
)

urlpatterns = [
    path('messageTemplateView/messages/', MessageTemplateView.as_view(), name='message_view'),
    path('messageCreateView/', MessageCreateView.as_view(), name='message_create'),
    path('messageSentListView/', SentMessageListView.as_view(), name='sent_message_list'),
    path('messageDetailView/<uuid:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('messageReceivedListView/', ReceivedMessageListView.as_view(), name='received_message_list'),
]
