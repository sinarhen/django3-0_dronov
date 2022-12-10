from .models import Rubric


def my_middleware(next):
    # Some initialization
    def core_middleware(request):
        # Processing request
        response = next(request)
        # Processing response
        return response

    return core_middleware


class MyMiddleware:
    def __init__(self, next):
        self.next = next
        # Some initialization

    def __call__(self, request):
        # Request Processing
        response = self.next(request)
        # Response Processing
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Calls this func before calling next middleware
        pass

    def process_exception(self, request, exception):
        # request: HttpRequest, exception: Exception,
        pass


class RubricMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_template_response(self, request, response):
        response.context_data['rubrics'] = Rubric.objects.all()


# Context processors

def rubric(request):
    return {'rubrics': Rubric.objects.all()}