from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

class GetFlights(APIView):

    def post(self, request, *args, **kwargs):
        date = datetime.datetime.strptime(request.data['date'], '%Y-%m-%d').date()

        # TODO: find city

        # TODO: find flight to nis

        return Response({'date': date.strftime('%Y/%m/%d')})
