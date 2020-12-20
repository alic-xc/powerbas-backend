
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views import generic
from .forms import LoginForm


class HomepageView(generic.TemplateView):
    template_name = 'dashboard/homepage.html'


class LoginView(generic.FormView):
    template_name = 'books/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        else:
            messages.error(self.request, "No account found. Please check login credentials and try again")
            return super().form_invalid(form)

        return super().form_valid(form)


class DashboardView(generic.TemplateView):
    template_name = ''
