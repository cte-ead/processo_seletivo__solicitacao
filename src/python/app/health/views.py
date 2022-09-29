from django.conf import settings
from django.http import HttpResponse
from django.db import connection


def health(request):
    debug = "FAIL (are active)" if not settings.DEBUG else "OK"
    
    try:
        connection.connect()
        connection_result = "OK"
    except:
        connection_result = "FAIL"
    
    redis_result = "Not tested"

    return HttpResponse(f"""
        <pre>
            Reverse proxy: OK.
            Django: OK.
            Database: {connection_result}.
            Redis: {redis_result}.
            Debug: {debug}.
        </pre>
        """)
