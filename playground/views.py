from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError


def say_hello(request):
    try:
        # send_mail("Subject here", "Here is the message.", "info@moshby.com", ["bob@moshby.com"])
        mail_admins("Subject here", "Here is the message.",html_message="<h1>HTML Message</h1>")
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Mosh"})
