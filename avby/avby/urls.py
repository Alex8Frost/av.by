from django.contrib import admin
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from django_registration.forms import RegistrationFormUniqueEmail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/register/', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
         name='django_registration_register_uniq_email'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path("", include('back.urls')),
]
