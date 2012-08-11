from django.http import HttpResponse


def json_response(f):
    def wrapped(request, *args, **kwargs):
        response = f(request, *args, **kwargs)
        try:
            if issubclass(response, HttpResponse):
                return response(mimetype="application/json")
        except TypeError:
            pass
        jr = json.dumps(response)
        return HttpResponse(jr, mimetype="application/json")
    return wrapped