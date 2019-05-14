from django.http import HttpResponse

from TestModel.models import Test


def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>Data Successfully Added</p>")


def testdb1(request):

    response = ""

    response1 = ""

    object_list = Test.objects.all()

    response2 = Test.objects.filter(id=1)

    response3 = Test.objects.get(id=1)

    print(Test.objects.order_by('name')[0:2])

    print(Test.objects.order_by("id"))

    print(Test.objects.filter(name="runoob").order_by("id"))

    for var in object_list:
        response1 += var.name + " "

    for var in object_list:
        response += var.name + " "

    # response = response1 + " response2" + " 111"  # response2.name + " response3" + response3.name

    return HttpResponse("<p>" + response + "</p>")
