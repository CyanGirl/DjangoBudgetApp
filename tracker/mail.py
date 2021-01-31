from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def sendmail(context,useremail):
    subject = f'Expenditures Details -{context["message"]} || BudgetApp'
    html_message = render_to_string('tracker/mail.html', context)
    plain_message = strip_tags(html_message)
    from_email = 'noreply.devtests@gmail.com'
    to = useremail

    try:
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        return True
    except:
        return False