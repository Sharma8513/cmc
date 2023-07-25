import requests

# 88c1c4ea-5475-40fd-975b-e66489c4bf59

# response = requests.get("http://127.0.0.1:8000/crypto")
response = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories",
    headers={"X-CMC_PRO_API_KEY": "88c1c4ea-5475-40fd-975b-e66489c4bf59"},  # catagories
)

#    https://pro-api.coinmarketcap.com/v2/cryptocurrency/info                  #metadata


print(response.json())
