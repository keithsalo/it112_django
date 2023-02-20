from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Candy
from cars.models import Car2


# def home(request):
#     return HttpResponse("Hello,  New User!")


# def cars(request):
#     return HttpResponse("Hello ass User!")


# def candy(request):
#     candy = Candy.objects.all()
#     return HttpResponse(f"Number of candy: { candy.count()}")


#
# def candy(request):
#     candy = Candy.objects.all()
#     return render(
#         request,
#         'cars/candy.html', {'candy': candy})

def hello_there(request):
    username = request.GET.get("user_name", "Stranger")
    return render(
        request, 'cars/greeting.html', {'username': username, })


def car2(request):
    car = Car2.objects.all()
    return render(
        request,
        'cars/cars.html', {'car': car})


def car_detail(request):
    detail = Car2.objects.values()
    return render(request, "cars/car_detail.html", {"detail": detail})


# def candy(request, candy):
#     candy = Candy.objects.all()
#     return render(request, 'cars/candy.html',  {'candy': candy, })
