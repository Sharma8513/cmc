# from background_task import background
# import requests
# from .models import Categories
# from cmc.serializers import CategoriesSerializer


# @background(schedule=60)  # Run the task every 60 seconds
# def update_Categories_data_from_api():
#     result = requests.get(
#         "https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories",
#         headers={"X-CMC_PRO_API_KEY": "88c1c4ea-5475-40fd-975b-e66489c4bf59"},
#     )
#     resu = result.json()
#     serializer = CategoriesSerializer(data=resu["data"], many=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()


# def schedule_data_update():
#     update_Categories_data_from_api(repeat=60)  # Repeat the task every 60 seconds
