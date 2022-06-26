from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
def redirect_to_survey(request):
    return redirect('/survey')


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class Process_Form(View):
    def post(self, request):
        request.session['s_name'] = request.POST.get('s_name')
        request.session['s_dojo_location'] = request.POST.get('s_dojo_location')
        request.session['s_fav_language'] = request.POST.get('s_fav_language')
        request.session['s_comment'] = request.POST.get('s_comment')

        return redirect('redirect_result')


def Result(request):
    return render(request, 'result.html')


def BackSubmit(request):
    request.session.clear()
    return redirect('index')
