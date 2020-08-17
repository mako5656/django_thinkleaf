from django.shortcuts import render
from .models import Member


def list(request):
    data = Member.objects.all()
    params = {'message': 'メンバーの一覧', 'data': data}
    return render(request, 'user/list.html', params)