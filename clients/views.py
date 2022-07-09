from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404

from clients.models import Profile
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import User, UserCreationForm, UserChangeForm
from django.views.generic import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from .forms import EditProfileForm


class ProfileView(ListView):
    template_name = 'profile_panel.html'
    model = Profile


class ProfileListView(ListView):
    template_name = 'user_profile.html'
    model = Profile


    # form_class = EditProfileForm
    # success_url = reverse_lazy("clients_urls:user_profile")


class UserReservationsView(ListView):
    template_name = 'user_reservations.html'
    model = Profile


class UserEditReservations(ListView):
    template_name = 'user_edit_reservations.html'
    model = Profile


class UserDeleteReservations(ListView):
    template_name = 'user_delete_reservations.html'
    model = Profile


class UserEditView(UpdateView, FormView):
    model = Profile
    template_name = 'user_edit_profile.html'
    form_class = EditProfileForm
    success_url = reverse_lazy("clients_urls:user_profile")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result



       # Profile.objects.create(user=user, wallet=wallet, unit_payment=unitpayment)

    # def get_context_data(self, *args, **kwargs):
    #     user = Profile.objects.all()
    #     context = super(ProfileListView, self).get_context_data(*args, **kwargs)
    #     user_page = get_object_or_404(Profile, id=self.kwargs['pk'])
    #
    #     context['user_profile'] = user_page
    #     return context
    # wallet = form.cleaned_data["wallet"]
    # unit_payment = form.cleaned_data["unit_payment"]
    # Profile.objects.create(wallet=wallet, unit_payment=unit_payment)