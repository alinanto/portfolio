from django.http import HttpResponseForbidden


class MartorAdminUploadOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/martor/uploader/'):
            if not request.user.is_authenticated or not request.user.is_staff:
                return HttpResponseForbidden('Forbidden')

        return self.get_response(request)