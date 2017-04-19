from django.views.generic import TemplateView
from django.conf import settings


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_jsdata(self):
        data = {
            'static': settings.STATIC_URL
        }
        if self.request.user.is_authenticated():
            user = self.request.user
            data['user'] = {
                'id': user.id,
                'email': user.email,
            }
            try:
                data['user']['username'] = user.username
            except AttributeError:
                data['user']['username'] = user.email
        return super().get_jsdata(**data)
