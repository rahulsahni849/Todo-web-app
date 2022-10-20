from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthRequiredMiddleware(MiddlewareMixin):
    pass
#     def process_view(self, request, view_func, *view_args, **view_kwargs):
#         user = request.user
#         if user.is_authenticated:
#             return HttpResponseRedirect(reverse('todo-home'))
#         else:
#             return HttpResponseRedirect(reverse('login'))