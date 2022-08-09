from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View


from .form import ContactUsForm
from .email import ContactUsEmail

# TODO: move the index.html to other views when it will be ready


class HomeView(View):

    def get(self, request, **kwargs):
        return render(request, 'contactus/index.html')

    def post(self, request, **kwargs):
        form = ContactUsForm(request.POST or None)

        if form.is_valid():
            f = form.save()
            ContactUsEmail(f.__dict__).start()
            messages.success(request, 'Your message has been successfully sent.<br>Our manager will contact you soon.')
        else:
            messages.error(request, 'Something went wrong, please try again!')

        return redirect('index')


def privacy_policy(request):
    return render(request, 'contactus/static.html')


def not_found_page(request, exception):
    return render(request, "contactus/404.html", {}, status=404)
