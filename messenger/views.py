from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.conf import settings
from django.http import HttpResponseNotFound
from pages.models import (
    MessageBox
)

User = settings.AUTH_USER_MODEL

class MessageTemplateView(LoginRequiredMixin, generic.TemplateView):

    template_name = 'messenger/message_view.html'

class MessageCreateView(LoginRequiredMixin, generic.CreateView):

    model = MessageBox
    template_name = 'messenger/message_create.html'

    fields = ('receiver', 'subject', 'content', 'attachment', )

    def get_success_url(self):
        return self.request.GET.get('next')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super(MessageCreateView, self).form_valid(form)

class SentMessageListView(LoginRequiredMixin, generic.ListView):

    model = MessageBox
    template_name = 'messenger/sent_message_list.html'
    context_object_name = 'mss'

    def get_queryset(self):
        return MessageBox.objects.filter(sender=self.request.user)
    
class MessageDetailView(LoginRequiredMixin, generic.DetailView):

    model = MessageBox
    template_name = 'messenger/message_detail.html'

    def get_queryset(self):
        return MessageBox.objects.filter(sender=self.request.user) | MessageBox.objects.filter(receiver=self.request.user)
    
class ReceivedMessageListView(LoginRequiredMixin, generic.ListView):

    model = MessageBox
    template_name = 'messenger/received_message_list.html'
    context_object_name = 'mrs'

    def get_queryset(self):
        return MessageBox.objects.filter(receiver=self.request.user)


