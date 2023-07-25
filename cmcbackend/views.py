from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import CryptoCoins, Currency
from rest_framework.decorators import api_view
import requests
import currencyapicom
from .helper import helper

# from .redisMiddleware import RedisTokenMiddleware
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


def update_currency_data():
    try:
        client = currencyapicom.Client(os.environ.get("CURRENCY_API_KEY"))
        result = client.latest()
        new_data = result["data"]

        # Create new instances for bulk_create
        new_instances = []
        for currency_code, currency_info in new_data.items():
            currency_instance, _ = Currency.objects.get_or_create(
                code=currency_info["code"]
            )
            currency_instance.value = currency_info["value"]
            currency_instance.save()
            new_instances.append(currency_instance)

        # Bulk create new instances
        Currency.objects.bulk_create(new_instances, ignore_conflicts=True)
        print("updated currency")
        return HttpResponse("Data updated successfully.")
    except Exception as e:
        print("Error in update_currency_data", e)
        return JsonResponse({"Error": e})


def update_coins_data():
    try:
        result = requests.get(
            "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=30",
            headers={"X-CMC_PRO_API_KEY": os.environ.get("X-CMC_PRO_API_KEY")},
        )
        response_data = result.json()
        new_data = response_data["data"]

        # Create new instances for bulk_create
        new_instances = []
        for item in new_data:
            try:
                # Try to get the existing instance based on the 'id'
                existing_instance = CryptoCoins.objects.get(id=item["id"])

                # If the instance exists, update its attributes with the new data
                existing_instance.name = item["name"]
                existing_instance.symbol = item["symbol"]
                existing_instance.last_updated = item["last_updated"]
                existing_instance.date_added = item["date_added"]
                existing_instance.price = item["quote"]["USD"]["price"]
                existing_instance.save()
            except CryptoCoins.DoesNotExist:
                # If the instance does not exist, create a new one
                new_instance = CryptoCoins(
                    id=item["id"],
                    name=item["name"],
                    symbol=item["symbol"],
                    last_updated=item["last_updated"],
                    date_added=item["date_added"],
                    price=item["quote"]["USD"]["price"],
                )
                new_instance.save()
                new_instances.append(new_instance)

        # Bulk create new instances
        CryptoCoins.objects.bulk_create(new_instances, ignore_conflicts=True)
        print("updated Listings")
        return HttpResponse("Data updated successfully.")
    except Exception as e:
        print("Error in update_coins_data", e)
        return JsonResponse({"Error": e})


# @RedisTokenMiddleware
@api_view(["Get"])
def convo(request):
    try:
        res = helper(request)
        return JsonResponse(res)
    except Exception as e:
        print(e)
        return JsonResponse({"error": "Something went wrong", e: e})


@api_view(["Get"])
def index(request, format=None):
    try:
        if request.method == "GET":
            return HttpResponse("Antier CMC Backend is running!!")
    except Exception as e:
        print("Error:", e)
        return JsonResponse({"Error": e})


# @api_view(["GET"])
# def Schedular(request, format=None):
#     obj = CryptoCoins.objects.all()
#     context = {
#         "obj": obj,
#     }
#     if request.method == "GET":
#         scheduler = BackgroundScheduler()
#         scheduler.add_job(
#             update_coins_data, "interval", seconds=100000000
#         )  # Update data every 60 second
#         scheduler.add_job(update_currency_data, "interval", seconds=1000000000)
#         scheduler.start()
#         return render(request, "index.html", context)


# @api_view(["GET"])
# def Schedular(request, format=None):
#     obj = CryptoCoins.objects.all()
#     context = {
#         "obj": obj,
#     }
#     if request.method == "GET":
#         scheduler = BackgroundScheduler()
#         scheduler.add_job(
#             update_coins_data, "interval", seconds=100000000
#         )  # Update data every 1 second
#         scheduler.add_job(update_currency_data, "interval", seconds=10000000)
#         scheduler.start()
#         return render(request, "index.html", context)
#         # return Response("Data update scheduled", status=status.HTTP_200_OK)


# def update_coins_data():
#     result = requests.get(
#         "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=30",
#         headers={"X-CMC_PRO_API_KEY": "18b16821-0b79-4781-85eb-be39bb82f5b2"},
#     )
#     response_data = result.json()
#     new_data = response_data["data"]

#     # Create new instances for bulk_create
#     new_instances = []
#     for item in new_data:
#         new_instance = CryptoCoins.objects(
#             id=item["id"],
#             name=item["name"],
#             symbol=item["symbol"],
#             last_updated=item["last_updated"],
#             date_added=item["date_added"],
#             price=item["quote"]["USD"]["price"],
#         )
#         new_instance.save()
#         new_instances.append(new_instance)
#     # new_instances.save()

#     # Bulk create new instances
#     CryptoCoins.objects.bulk_create(new_instances, ignore_conflicts=True)
#     print("updated Listings")
#     return HttpResponse("Data updated successfully.")


# @api_view(["GET"])
# def currencies(request, format=None):
#     if request.method == "GET":
#         client = currencyapicom.Client("euaCM6F7vc12zNB8hQCKXJHuX7zJqLcO0GMitChs")
#         result = client.latest()
#         # response_data = json.loads(result)
#         new_data = result["data"]
#         # resu = []
#         # for item in new_data:
#         #     resu.append(item)

#         serializer = CurrencySerializer(data=list(new_data.values()), many=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(result, status=status.HTTP_201_CREATED)


# @api_view(["GET"])
# def Currencyapi(request, format=None):
#     obj = Currency.objects.all()
#     context = {
#         "obj": obj,
#     }
#     if request.method == "GET":
#         scheduler = BackgroundScheduler()
#         scheduler.add_job(
#             update_currency_data, "interval", seconds=1000000000
#         )  # Update data every 1 second
#         scheduler.start()
#         return render(request, "index.html", context)
#         # return Response("Data update scheduled", status=status.HTTP_200_OK)


# @api_view(["GET"])
# def CryptoCoinss(request, format=None):
#     if request.method == "GET":
#         result = requests.get(
#             "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit=10",
#             headers={"X-CMC_PRO_API_KEY": "88c1c4ea-5475-40fd-975b-e66489c4bf59"},
#         )
#         resu = result.json()
#         new_data = resu["data"]
#         for item in new_data:
#             price = item["quote"]["USD"]["price"]
#             item["price"] = price

#         serializer = CryptoCoinsSerializer(data=new_data, many=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(result, status=status.HTTP_201_CREATED)


# def convert_currency(request, cryptocurrency_sym, currency_code):
#     try:
#         cryptocurrency = Listings.objects.get(symbol=cryptocurrency_sym)
#         currency = Currency.objects.get(code=currency_code)
#         conversion_rate = currency.value
#         converted_price = cryptocurrency.price * conversion_rate

#         response = {
#             "cryptocurrency_id": cryptocurrency_sym,
#             "cryptocurrency_name": cryptocurrency.name,
#             "cryptocurrency_symbol": cryptocurrency.symbol,
#             "currency_code": currency_code,
#             "conversion_rate": conversion_rate,
#             "converted_price": converted_price,
#         }

#         return JsonResponse(response)
#     except (Listings.DoesNotExist, Currency.DoesNotExist):
#         return JsonResponse({"error": "Invalid cryptocurrency or currency code"})


# def convert_currency(request, cryptocurrency_sym, currency_code):
#     try:
#         currenty = list(currency_code.split(","))
#         cryptocurrency = CryptoCoins.objects.get(
#             symbol=cryptocurrency_sym, is_active=True
#         )
#         currencies = Currency.objects.filter(code__in=currenty)
#         response = {"data": []}

#         for currency in currencies:
#             print(currency.code)
#             conversion_rate = currency.value
#             converted_price = cryptocurrency.price * conversion_rate

#             currency_data = {
#                 "cryptocurrency_id": cryptocurrency_sym,
#                 "cryptocurrency_name": cryptocurrency.name,
#                 "cryptocurrency_symbol": cryptocurrency.symbol,
#                 "currency_code": currency.code,
#                 "converted_price": converted_price,
#             }
#             response["data"].append(currency_data)

#         return JsonResponse(response)

#     except Exception as e:
#         print(e)
#         return JsonResponse({"error": "Invalid cryptocurrency or currency code"})


# from django.core.serializers import serialize


# def convert_currency_all(request, cryptocurrency_sym):
#     try:
#         # listdatacrypto = list(cryptocurrency_sym.split(","))
#         # print(listdatacrypto)
#         # listdata = list(currency_code.split(","))
#         data = request.GET.get("data")
#         data2 = request.GET.get("data2")
#         print(data, data2)
#         damara = Q(symbol=cryptocurrency_sym)
#         damara.AND = Q(is_active=True)
#         # seridata = serialize("json", damara)
#         # seridata = json.loads(seridata)
#         cryptocurrency = CryptoCoins.objects.get(damara)
#         currency = Currency.objects.all()
#         temp = CryptoCoins.objects.all()
#         # print(list(cryptocurrency))
#         print(len(temp))
#         print(type(temp) == QuerySet)
#         print(type(cryptocurrency))
#         responseData = {
#             "data": {
#                 "id": cryptocurrency_sym,
#                 "name": cryptocurrency.name,
#                 "symbol": cryptocurrency.symbol,
#                 "quote": {},
#             }
#         }
#         # for crypto in cryptocurrency:
#         #     tempResponse = crypto
#         #     tempResponse["data"] = []
#         for dam in currency:
#             # print(dam)
#             conversion_rate = dam.value
#             converted_price = cryptocurrency.price * conversion_rate

#             response = {
#                 # "currency_code": dam.code,
#                 "conversion_rate": conversion_rate,
#                 "price": converted_price,
#             }
#             responseData["data"]["quote"][dam.code] = response
#         # responseData["data"].append(tempResponse)

#         return JsonResponse(responseData)
#     # except (Listings.DoesNotExist, Currency.DoesNotExist):
#     #     return JsonResponse({"error": "Invalid cryptocurrency or currency code"})
#     except Exception as e:
#         print(e)
#         return JsonResponse(
#             {"error": "Invalid cryptocurrency or currency code", "e": e}
#         )


# def convert_crypto_to_crypto(request, from_crypto_sym, to_crypto_sym):
#     try:
#         from_crypto = CryptoCoins.objects.get(symbol=from_crypto_sym, is_active=True)
#         to_crypto_symbols = to_crypto_sym.split(",")

#         response = {
#             "from_crypto_id": from_crypto_sym,
#             "cryptocurrency_name": from_crypto.name,
#             "cryptocurrency_symbol": from_crypto.symbol,
#             "conversion_rates": {},
#         }

#         for to_symbol in to_crypto_symbols:
#             try:
#                 to_crypto = CryptoCoins.objects.get(symbol=to_symbol)
#                 conversion_rate = from_crypto.price / to_crypto.price

#                 response["conversion_rates"][to_symbol] = conversion_rate
#                 # response["cryptocurrency_name1"] = to_crypto.name
#                 # response["cryptocurrency_symbol1"] = to_crypto.symbol

#             except CryptoCoins.DoesNotExist:
#                 response["conversion_rates"][to_symbol] = "Invalid cryptocurrency ID"

#         return JsonResponse(response)
#     except CryptoCoins.DoesNotExist:
#         return JsonResponse({"error": "Invalid cryptocurrency ID"})


# def convert(request, from_sym, to_sym):
#     try:
#         from_crypto = CryptoCoins.objects.get(symbol=from_sym, is_active=True)
#         if "," in to_sym:
#             to_crypto_symbols = to_sym.split(",")
#             response = {
#                 "from_crypto_id": from_sym,
#                 "cryptocurrency_name": from_crypto.name,
#                 "cryptocurrency_symbol": from_crypto.symbol,
#                 "conversion_rates": {},
#             }

#             for to_symbol in to_crypto_symbols:
#                 try:
#                     to_crypto = CryptoCoins.objects.get(symbol=to_symbol)
#                     conversion_rate = from_crypto.price / to_crypto.price
#                     response["conversion_rates"][to_symbol] = conversion_rate
#                 except CryptoCoins.DoesNotExist:
#                     response["conversion_rates"][
#                         to_symbol
#                     ] = "Invalid cryptocurrency ID"

#         else:
#             currencies = Currency.objects.filter(code=to_sym)
#             response = {"data": []}

#             for currency in currencies:
#                 conversion_rate = currency.value
#                 converted_price = from_crypto.price * conversion_rate

#                 currency_data = {
#                     "cryptocurrency_id": from_sym,
#                     "cryptocurrency_name": from_crypto.name,
#                     "cryptocurrency_symbol": from_crypto.symbol,
#                     "currency_code": currency.code,
#                     "converted_price": converted_price,
#                 }
#                 response["data"].append(currency_data)

#         return JsonResponse(response)

#     except CryptoCoins.DoesNotExist:
#         return JsonResponse({"error": "Invalid cryptocurrency ID"})
#     except Currency.DoesNotExist:
#         return JsonResponse({"error": "Invalid currency code"})


# def conversion(request, from_crypto_sym, to_crypto_sym):
#     try:
#         from_crypto = CryptoCoins.objects.get(symbol=from_crypto_sym, is_active=True)
#         to_crypto_symbols = to_crypto_sym.split(",")

#         response = {
#             "from_crypto_id": from_crypto_sym,
#             "cryptocurrency_name": from_crypto.name,
#             "cryptocurrency_symbol": from_crypto.symbol,
#             "conversion_rates": {},
#         }

#         for to_symbol in to_crypto_symbols:
#             try:
#                 to_crypto = CryptoCoins.objects.get(symbol=to_symbol)
#                 conversion_rate = from_crypto.price / to_crypto.price

#                 response["conversion_rates"][to_symbol] = conversion_rate
#                 # response["cryptocurrency_name1"] = to_crypto.name
#                 # response["cryptocurrency_symbol1"] = to_crypto.symbol

#             except:
#                 to_currency = Currency.objects.get(code=to_symbol)
#                 conversion_rate = to_currency.value
#                 converted_price = from_crypto.price * conversion_rate
#                 response["conversion_rates"][to_symbol] = converted_price

#         return JsonResponse(response)
#     except:
#         return JsonResponse({"error": "Invalid cryptocurrency ID"})


# @api_view(["GET"])
# def Categoriess(request, format=None):
#     obj = Categories.objects.all()
#     context = {
#         "obj": obj,
#     }
#     if request.method == "GET":
#         scheduler = BackgroundScheduler()
#         scheduler.add_job(
#             update_data, "interval", seconds=5
#         )  # Update data every 1 second
#         scheduler.start()
#         # return render(request, "index.html", context)
#         return Response("Data update scheduled", status=status.HTTP_200_OK)


# def update_data():
#     # Retrieve the existing data from the database (based on your specific criteria)
#     existing_data = Categories.objects.all()
#     result = requests.get(
#         "https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories",
#         headers={"X-CMC_PRO_API_KEY": "88c1c4ea-5475-40fd-975b-e66489c4bf59"},
#     )
#     resu = result.json()
#     new_data = resu["data"]
#     # Deserialize the incoming data using the serializer
#     new_instances = [Categories(**item) for item in new_data]
#     for instance in new_instances:
#         instance.save()

#     # Perform bulk update or create
#     resu = Categories.objects.bulk_create(new_instances, ignore_conflicts=True)
#     print("updated")
#     return HttpResponse("Data updated successfully.")


# @api_view(["GET"])
# def Cryptocurrencies(request, format=None):
#     obj = Cryptocurrency.objects.all()
#     context = {
#         "obj": obj,
#     }
#     if request.method == "GET":
#         scheduler = BackgroundScheduler()
#         scheduler.add_job(
#             update_data_Crypto, "interval", seconds=200
#         )  # Update data every 1 second
#         scheduler.start()
#         # return render(request, "index.html", context)
#         return Response("Data update scheduled", status=status.HTTP_200_OK)


# def update_data_Crypto():
#     # Retrieve the existing data from the database (based on your specific criteria)
#     existing_data = Cryptocurrency.objects.all()
#     result = requests.get(
#         "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
#         headers={"X-CMC_PRO_API_KEY": "18b16821-0b79-4781-85eb-be39bb82f5b2"},
#     )
#     print(json.dumps(result))
#     resu = result.json()

#     new_data = resu["data"]
#     # print(new_data)
#     # Deserialize the incoming data using the serializer
#     new_instances = [Cryptocurrency(**item) for item in new_data]
#     for instance in new_instances:
#         instance.save()

#     # Perform bulk update or create
#     resu = Cryptocurrency.objects.bulk_create(new_instances, ignore_conflicts=True)
#     print("updated")
#     return HttpResponse("Data updated successfully.")


# @api_view(["GET"])
# def Categoriess(request, format=None):
#     if request.method == "GET":
#         result = requests.get(
#             "https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories",
#             headers={"X-CMC_PRO_API_KEY": "88c1c4ea-5475-40fd-975b-e66489c4bf59"},
#         )
#         resu = result.json()
#         serializer = CategoriesSerializer(data=resu["data"], many=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(result, status=status.HTTP_201_CREATED)


# @api_view(["GET", "POST"])
# # Create your views here.
# def index(request):
#     obj = Cryptos.objects.all()
#     context = {
#         "obj": obj,
#     }

#     return render(request, "index.html", context)
#     # return HttpResponse("this is my New CoinMarketCap page")


# def about(request):
#     return HttpResponse("this is my CMC about page")


# @api_view(["GET", "POST"])
# def crypto(request, format=None):
#     if request.method == "GET":
#         cryptos = Cryptos.objects.all()
#         serializer = CryptoSerializer(cryptos, many=True)
#         return Response(serializer.data)

#     if request.method == "POST":
#         result = requests.get(
#             "https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories",
#             headers={"X-CMC_PRO_API_KEY": "88c1c4ea-5475-40fd-975b-e66489c4bf59"},
#         )
#         serializer = CryptoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(["GET", "PUT", "DELETE"])
# def crypto_detail(request, id, format=None):
#     try:
#         crypto = Cryptos.objects.get(pk=id)
#     except Cryptos.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = CryptoSerializer(crypto)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = CryptoSerializer(crypto, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         crypto.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
