from django.contrib import admin
from .models import Cuenta, TipoCuenta

admin.site.register([Cuenta, TipoCuenta])
