from django.conf.urls import url, include
from api.invoice.v1 import urls as invoice


app_name = "api"
urlpatterns = [
    url(r'^invoice/', include(invoice, namespace="invoice")),
]
