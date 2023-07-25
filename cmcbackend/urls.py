from django.urls import path
from cmcbackend import views
from cmcbackend.Schedular import schedular

# print("Starting")
schedular.start()

urlpatterns = [
    # path("", views.Currencyapi, name="currency"),
    # path("about/", views.about, name="about"),
    # path("crypto/", views.crypto, name="crypto"),
    # path("currencies/", views.currencies, name="currency"),
    # path("crypto/<int:id>", views.crypto_detail, name="crypto"),
    path("", views.index, name="index"),
    # path(
    #     "convert_currency/<str:cryptocurrency_sym>/<str:currency_code>/",
    #     views.convert_currency,
    #     name="convert",
    # ),
    # path(
    #     "convert_currency_all/<str:cryptocurrency_sym>/",
    #     views.convert_currency_all,
    #     name="convert_all",
    # ),
    # path(
    #     "cry_to_cry/<str:from_crypto_sym>/<str:to_crypto_sym>/",
    #     views.convert_crypto_to_crypto,
    # ),
    # path("convert/<str:from_sym>/<str:to_sym>/", views.convert, name="convert"),
    # path(
    #     "conversion/<str:from_crypto_sym>/<str:to_crypto_sym>/",
    #     views.conversion,
    #     name="conversion",
    # ),
    path(
        "v2/tools/price-conversion",
        views.convo,
        name="convert",
    ),
    # path("categories/", views.Categoriess, name="categories"),
    # path("update/", views.update_data, name="update"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
