import secret
from django.core.checks import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from forms import FeedbackForm, MailingForm


def feedback(request):
    """Обратная связь"""
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        try:
            if form.is_valid():
                mail = send_mail(form.cleaned_data["subject"], form.cleaned_data["content"], secret.FEEDBACK_EMAIL,
                                 [secret.EMAIL_HOST_USER], fail_silently=False)
                if mail:
                    return redirect("/")
            else:
                messages.success("Произошла ошибка, проверьте ввод данных!")
        except Exception as e:
            return HttpResponseBadRequest("Попробуйте снова!")
    else:
        form = FeedbackForm()
    return render(request, "mailing/mail_send.html", {"form": form})


def mailing(request):
    """Рассылка"""
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            try:
                mail = send_mail('xifOO', 'Вы подписались на рассылку', secret.EMAIL_HOST_USER,
                                 [form.cleaned_data['email']], fail_silently=False)
                if mail:
                    return redirect('/')
                else:
                    messages.success(request, 'Произошла ошибка')
            except Exception as e:
                return HttpResponseBadRequest("Попробуйте снова!")
    else:
        form = MailingForm()
    return render(request, 'mailing/mailing.html', {'form': form})