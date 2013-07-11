import datetime
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from server.service import FooService

service = FooService()


def overview(request):
    response = HttpResponse()
    response.write("The following methods are available:<ul>")

    import urls
    for p in urls.urlpatterns:
        pattern = p.regex.pattern
        if pattern.startswith('^rest'):
            href = pattern.replace('^', '').replace('$', '')
            response.write('<li><a href="/%s">%s</a></li>' % (href, href))

    response.write("</ul>")
    return response


class PingView(APIView):
    def get(self, request, format=None):
        result = service.ping()
        return Response(data={'msg': result})

    def post(self, request, format=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class BalanceView(APIView):
    def get(self, request, format=None):
        msisdn = request.GET.get('msisdn', None)
        result = service.balance(msisdn)

        # temp fix for the date
        result['valid_until'] = None

        return Response(data=result)


class PortinView(APIView):
    def post(self, request, format=None):
        msisdn = request.POST.get('msisdn', None)
        result = service.portin(msisdn)
        return Response(data=result)


class PortoutView(APIView):
    def post(self, request, format=None):
        msisdn = request.POST.get('msisdn', None)
        result = service.portout(msisdn)
        return Response(data=result)


class AddcreditView(APIView):
    def post(self, request, format=None):
        if request.DATA:
            msisdn = request.DATA.get('msisdn', None)
            amount = request.DATA.get('amount', 10)
        else:
            msisdn = None
            amount = 10

        result = service.addcredit(msisdn, amount)
        return Response(data=result.__dict__)

