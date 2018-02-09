from django.http import JsonResponse

from .models import Text


def upload_text(request):
    string = request.GET.get('string')
    Text.objects.create(string=string)
    return JsonResponse({'message': 'Текст отправлен!'})


def get_text(request):
    lst = []
    for text in Text.objects.all():
        lst.append(text.string)
    return JsonResponse({'list': lst})
