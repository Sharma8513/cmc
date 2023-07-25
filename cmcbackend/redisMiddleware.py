# import redis
# from django.http import JsonResponse
# import os
# from dotenv import load_dotenv

# # Load variables from .env file
# load_dotenv()

# # Create a Redis client instance
# redis_client = redis.StrictRedis(
#     host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT"), db=0
# )


# class RedisTokenMiddleware:
#     def __init__(self, get_response):
#         try:
#             self.get_response = get_response
#             redis_client.set(os.environ.get("AUTHORIZATION_TOKEN"), "valid")
#         except Exception as e:
#             print("Error in Redis", e)
#             return JsonResponse({"Error": e})

#     def __call__(self, request):
#         try:
#             # Check if the Authorization token exists in the request headers
#             auth_token = request.headers.get("Authorization")

#             # If the token does not exist, check if it is a valid token in Redis
#             if not auth_token or not redis_client.exists(auth_token):
#                 return JsonResponse({"error": "Unauthorized"}, status=401)

#             # Call the next middleware or view
#             response = self.get_response(request)
#             return response
#         except Exception as e:
#             print("Error in Authorization", e)
#             return JsonResponse({"Error": e})
