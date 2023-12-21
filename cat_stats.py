from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render





def stats_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request,'cat_info.html')
    print(request.POST)
    context = {
        'cat_name': request.POST.get('cat_name', 'Undefined'),
        'cat_age': 1,
        'hapiness_level': 10,
        'satiety_level': 40,
    }
    langs = request.POST.getlist("languages", ["python"])
    return render(request, 'cat_info.html',context=context)


def cats_turn():
    cat_action =
    if cat_action == "play":
        context['hapiness_level']+15
        context['satiety_level']-10


# from django.core.handlers.wsgi import WSGIRequest
# from django.shortcuts import render

# def stats_view(request: WSGIRequest):
#     cat_name = request.POST.get()
#     cat_name = {"name": 'Vasya'}
#     cat_age = {"age": 1}
#     hapiness_level = {"hapiness_level": 10}
#     satiety_level = {"satiety_level": 40}
#     data = {"cat_name": cat_name, "cat_age": cat_age, "hapiness_level":hapiness_level, "satiety_level":satiety_level}
#     return render(request, 'cat_info.html', context=data)

    # if request.method == 'GET':
    #     return render(request,'cat_info.html')


