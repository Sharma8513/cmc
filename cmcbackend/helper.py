from .models import CryptoCoins, Currency
import datetime
from decimal import Decimal


def helper(request):
    response = {
        "status": {
            "timestamp": None,
            "error_code": None,
            "error_message": None,
            "elapsed": None,
            "credit_count": None,
            "notice": "",
        }
    }

    try:
        from_crypto = request.GET.get("symbol")
        if not from_crypto:
            return error(response, "Value must contain symbol")
        from_crypto = from_crypto.upper()

        amount = request.GET.get("amount")
        if not amount:
            return error(response, "Amount is required")

        try:
            amount = float(amount)
        except ValueError:
            return error(response, "Amount must be a number")

        to_convert = request.GET.get("convert")
        if not to_convert:
            to_convert = "USD"
        to_convert = to_convert.upper()

        got_symbols = list(to_convert.split(","))
        from_crypto_data = CryptoCoins.objects.filter(
            symbol=from_crypto, is_active=True
        ).first()

        if not from_crypto_data:
            return error(response, "Invalid Crypto symbol")

        to_if_crypto = CryptoCoins.objects.filter(
            symbol__in=got_symbols, is_active=True
        ).values()
        cryptos = set(to_if_crypto.values_list("symbol", flat=True))
        currenys_hold = list(filter(lambda x: x not in cryptos, got_symbols))

        to_if_currency = Currency.objects.filter(code__in=currenys_hold).values()
        currency_true = set(to_if_currency.values_list("code", flat=True))
        invalid_symbols = list(filter(lambda x: x not in currency_true, currenys_hold))

        if invalid_symbols:
            message = 'Invalid value for "convert": "' + str(invalid_symbols) + '"'
            return error(response, message)

        response["data"] = {
            "last_updated": from_crypto_data.last_updated,
            "name": from_crypto_data.name,
            "symbol": from_crypto_data.symbol,
            "amount": amount,
            "quotes": {},
        }

        for data in to_if_crypto:
            response["data"]["quotes"][data["symbol"]] = {
                "price": float(from_crypto_data.price) * amount / float(data["price"]),
                "last_updated": data["last_updated"],
            }

        for data in to_if_currency:
            response["data"]["quotes"][data["code"]] = {
                "price": float(from_crypto_data.price) * amount * float(data["value"]),
                "last_updated": data["last_updated"],
            }

        response["status"]["error_code"] = 0
        response["status"]["error_message"] = ""
        response["status"]["elapsed"] = 20
        response["status"]["credit_count"] = len(cryptos) + len(currency_true)
        response["status"]["timestamp"] = datetime.datetime.utcnow()

    except Exception as e:
        print(e, "error")
        response["status"]["error_code"] = 400
        response["status"]["error_message"] = str(e)
        response["status"]["elapsed"] = 0
        response["status"]["credit_count"] = 0
        response["status"]["timestamp"] = datetime.datetime.utcnow()

    return response


def error(response, message):
    response["status"]["error_code"] = 400
    response["status"]["error_message"] = message
    response["status"]["elapsed"] = 0
    response["status"]["credit_count"] = 0
    response["status"]["notice"] = None
    response["status"]["timestamp"] = datetime.datetime.utcnow()
    return response


# from .models import CryptoCoins, Currency
# import datetime


# def helper(request):
#     response = {
#         "status": {
#             "timestamp": None,
#             "error_code": None,
#             "error_message": None,
#             "elapsed": None,
#             "credit_count": None,
#             "notice": "",
#         }
#     }
#     try:
#         from_crypto = request.GET.get("symbol")
#         if not from_crypto:
#             return error(response, "Value must contain symbol")

#         from_crypto = from_crypto.upper()
#         amount = request.GET.get("amount")
#         if not amount:
#             return error(response, "Amount is required")

#         try:
#             amount = float(amount)
#         except ValueError:
#             return error(response, "Amount must be a valid number")

#         to_convert = request.GET.get("convert", "USD")
#         got_symbols = list(map(str.upper, to_convert.split(",")))
#         # Fetch CryptoCoins data for 'from_crypto'
#         try:
#             from_crypto_data = CryptoCoins.objects.get(
#                 symbol=from_crypto, is_active=True
#             )
#         except CryptoCoins.DoesNotExist:
#             return error(response, "Invalid Crypto symbol")

#         to_convert_cryptos = CryptoCoins.objects.filter(
#             symbol__in=got_symbols, is_active=True
#         )
#         print(to_convert_cryptos)
#         cryptos_data = to_convert_cryptos.values("symbol", "price")

#         currency_symbols = set(got_symbols) - set(
#             cryptos_data.values_list("symbol", flat=True)
#         )
#         to_convert_currencies = Currency.objects.filter(
#             code__in=currency_symbols
#         ).values("code", "value")

#         response["data"] = {
#             "last_updated": from_crypto_data.last_updated,
#             "name": from_crypto_data.name,
#             "symbol": from_crypto_data.symbol,
#             "amount": amount,
#             "quotes": {},
#         }

#         # Calculate quotes for cryptocurrencies
#         for data in cryptos_data:
#             response["data"]["quotes"][data["symbol"]] = {
#                 "price": float(from_crypto_data.price) * amount / float(data["price"]),
#                 "last_updated": data["last_updated"],
#             }

#         # Calculate quotes for currencies
#         for data in to_convert_currencies:
#             response["data"]["quotes"][data["code"]] = {
#                 "price": float(from_crypto_data.price) * amount * float(data["value"]),
#                 "last_updated": from_crypto_data.last_updated,
#             }
#         response = StatusSet(
#             response, 0, "", len(cryptos_data) + len(to_convert_currencies), 0, ""
#         )

#     except Exception as e:
#         response = error(response, str(e))

#     return response


# def error(response, message):
#     response["status"]["error_code"] = 400
#     response["status"]["error_message"] = message
#     response["status"]["elapsed"] = 0
#     response["status"]["credit_count"] = 0
#     response["status"]["notice"] = None
#     response["status"]["timestamp"] = datetime.datetime.utcnow()
#     return response


# def StatusSet(response, code, message, credit_count, elapsed, notice):
#     response["status"]["error_code"] = code
#     response["status"]["error_message"] = message
#     response["status"]["elapsed"] = elapsed
#     response["status"]["credit_count"] = credit_count
#     response["status"]["notice"] = notice
#     response["status"]["timestamp"] = datetime.datetime.utcnow()
#     return response


# from .models import CryptoCoins, Currency
# import datetime
# from decimal import Decimal


# def helper(request):
#     response = {
#         "status": {
#             "timestamp": None,
#             "error_code": None,
#             "error_message": None,
#             "elapsed": None,
#             "credit_count": None,
#             "notice": "",
#         }
#     }
#     try:
#         from_crypto = request.GET.get("symbol")
#         if from_crypto is None:
#             message = "Value must contain symbol"
#             return error(response, message)
#         from_crypto = from_crypto.upper()
#         amount = request.GET.get("amount")
#         # print(amount)
#         if not amount:
#             return error(response, "Amount is required")

#         try:
#             amount = float(amount)
#         except ValueError:
#             return error(response, "Invalid amount format")
#         # except Exception
#         to_convert = request.GET.get("convert")
#         # print(to_convert)
#         if to_convert is None:
#             to_convert = "USD"
#         to_convert = to_convert.upper()
#         # message = "Value must contain convert"
#         # return error(response, message)
#         got_symbols = list(to_convert.split(","))
#         # print(from_crypto)
#         from_crypto_data = []
#         try:
#             from_crypto_data = CryptoCoins.objects.get(
#                 symbol=from_crypto, is_active=True
#             )
#         except Exception as e:
#             return error(response, "Invalid Crypto symbol")
#         # got_symbols = CryptoCoins.objects.filter(is_active=Truegot_symbol)
#         to_if_crypto = CryptoCoins.objects.filter(symbol__in=got_symbols).values()
#         cryptos = to_if_crypto.values_list("symbol", flat=True)
#         to_if_crypto = to.filter(symbol__in=got_symbols,is_active=True).values()
#         currenys_hold = list(filter(lambda x: x not in cryptos, got_symbols))
#         to_if_currency = Currency.objects.filter(code__in=currenys_hold).values()
#         # currency_true2 = to_if_currency.values_dict("code", flat=True)
#         # print(currency_true2)
#         currency_true = to_if_currency.values_list("code", flat=True)
#         invalid_symbols = list(filter(lambda x: x not in currency_true, currenys_hold))
#         # print(invalid_symbols)
#         if len(invalid_symbols):
#             message = 'Invalid value for "convert": "' + str(invalid_symbols) + '"'
#             return error(response, message)
#         response["data"] = {
#             "last_updated": from_crypto_data.last_updated,
#             "name": from_crypto_data.name,
#             "symbol": from_crypto_data.symbol,
#             "amount": amount,
#             "quotes": {},
#             # "price": from_crypto_data.price,
#         }
#         # print(to_if_crypto, cryptos, currency_true)
#         # print()
#         for data in to_if_crypto:
#             # dataCon = to_if_crypto.filter(symbol=symbol).values()
#             # print(from_crypto_data.price)
#             response["data"]["quotes"][data["symbol"]] = {
#                 "price": (
#                     float(from_crypto_data.price) * amount / float(data["price"])
#                 ),
#                 "last_updated": data["last_updated"],
#             }
#             # response["data"]["quotes"][data["symbol"]] = temp
#         for data in to_if_currency:
#             response["data"]["quotes"][data["code"]] = {
#                 "price": (
#                     float(from_crypto_data.price) * amount * float(data["value"])
#                 ),
#                 "last_updated": data["last_updated"],
#             }
#             # response["data"]["quotes"][data["code"]] = temp
#         response["status"]["error_code"] = 0
#         response["status"]["error_message"] = ""
#         response["status"]["elapsed"] = 20
#         response["status"]["credit_count"] = cryptos.__len__() + currency_true.__len__()
#         response["status"]["timestamp"] = datetime.datetime.utcnow()
#     except Exception as e:
#         print(e, "error")
#         response["status"]["error_code"] = 400
#         response["status"]["error_message"] = e
#         response["status"]["elapsed"] = 0
#         response["status"]["credit_count"] = 0
#         response["status"]["timestamp"] = datetime.datetime.utcnow()

#     return response


# def error(response, message):
#     response["status"]["error_code"] = 400
#     response["status"]["error_message"] = message
#     response["status"]["elapsed"] = 0
#     response["status"]["credit_count"] = 0
#     response["status"]["notice"] = None
#     response["status"]["timestamp"] = datetime.datetime.utcnow()
#     return response
