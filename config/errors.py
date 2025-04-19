from django.shortcuts import render

from django.views import View


class PageNotFoundView(View):
    template_name = '404.html'
    status_code = 404

    def get(self, request, exception=None):
        return render(request, self.template_name, status=self.status_code)
