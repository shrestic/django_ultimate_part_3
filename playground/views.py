from django.shortcuts import render
from django.core.mail import BadHeaderError
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        message = BaseEmailMessage(
            context={"name": "Mosh"},
            template_name="emails/hello.html",
        )
        message.send(to=["john@moshby.com"])
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Mosh"})
