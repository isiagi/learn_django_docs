from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.


def index(request):
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in lastest_question_list])
    # return HttpResponse(output)
    template = loader.get_template("polls/index.html")
    context = {"lastest_question_list": lastest_question_list}
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question" : question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)