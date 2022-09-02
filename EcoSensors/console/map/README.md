# Tips and Hints

## Token
* Create an user with password from http://127.0.0.1:8080/admin/
* With that user, get an access and refresh token from: http://127.0.0.1:8080/token/
* POSTMAN => Key: Authorization Value: Bearer [access token]
* To test: http://127.0.0.1:8080/api/map/testToken/1/
* Define the life of the TOKEN in settings.py