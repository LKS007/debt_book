from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the debt index.")

def detail(request, debt_id):
    return HttpResponse("You're looking at debt %s." % debt_id)

def results(request, debt_id):
    response = "You're looking at the results of debt %s."
    return HttpResponse(response % debt_id)

def vote(request, debt_id):
    return HttpResponse("You're voting on debt %s." % debt_id)