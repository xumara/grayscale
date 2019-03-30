from django.shortcuts import render
from .models import WebsiteCommon, HeaderSection, Menu

# Create your views here.
def index (request):
    context = {}
    context ["common"] = WebsiteCommon.objects.last()
    context["header"] = HeaderSection.objects.last()
    context["menu_list"] = Menu.objects.all()

    return render(request, "index.html", context)

