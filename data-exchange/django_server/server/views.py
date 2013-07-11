from django.http import HttpResponse


def rpc(request):

    return HttpResponse('<h1>RPC</h1>')


def rest(request):
    return HttpResponse('<h1>REST</h1>')

