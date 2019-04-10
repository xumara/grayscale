from django.shortcuts import render
from .models import WebsiteCommon, HeaderSection, Menu, AboutSection, Project, Contact, FooterIcon, Subscription
from django.contrib import messages
# Create your views here.
def index (request):
    context = {}
    context ["common"] = WebsiteCommon.objects.last()
    context["header"] = HeaderSection.objects.last()
    context["menu_list"] = Menu.objects.all()
    context["about"] = AboutSection.objects.last()
    context["project_list"] = Project.objects.all()[:3]
    context["contact_list"] = Contact.objects.all()
    context["footer_list"] = FooterIcon.objects.all()

    if request.method == "POST":
        email = request.POST.get("email")
        Subscription.objects.create(
            email=email
        )
        messages.info(
            request,
            f"Bu {email} elave olundu. Bizi izlediyiniz ucun tesekkurler"
        )



    return render(request, "index.html", context)

