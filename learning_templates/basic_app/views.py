from django.shortcuts import render

def index(request):
    my_dict = {'text':'hello world', 'number':200}
    return render(request, 'basic_app/index.html', my_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_template.html')
