from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError


def say_hello(request):
    try:
        message = EmailMessage("subject", "message", "from@moshby.com", ["john@moshby.com"])
        message.attach_file("playground/static/images/dog.jpg")
        message.send()
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Mosh"})
