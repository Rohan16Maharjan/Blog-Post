from django.shortcuts import render, redirect
from .models import Home as Home1, About as About1, Contact,Home2
from .forms import ContactForm

# Create your views here.
def Home(request):
    home = Home1.objects.all()
    home2 = Home2.objects.all()
    context = {"home": home,'home2':home2}
    return render(request, "BlogApp/home.html", context)


def Detail(request, id):
    h = Home1.objects.get(id=id)
    context = {"h": h}
    return render(request, "BlogApp/detail.html", context)

def Detail1(request, id):
    h2 = Home2.objects.get(id=id)
    context = {"h2": h2}
    return render(request, "BlogApp/detail1.html", context)


def About(request):
    abo = About1.objects.all()
    context = {"abo": abo}
    return render(request, "BlogApp/about.html", context)


def Contact(request):
    cont = ContactForm()
    if request.method == "POST":
        cont = ContactForm(request.POST)
        if cont.is_valid():
            cont.save()
            return redirect("Home")
    context = {"cont": cont}
    return render(request, "BlogApp/contact.html", context)
