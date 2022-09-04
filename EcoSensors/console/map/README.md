# Tips and Hints

## Token
* Create an user with password from http://127.0.0.1:8080/admin/
* With that user, get an access and refresh token from: http://127.0.0.1:8080/token/
* POSTMAN => Key: Authorization Value: Bearer [access token]
* To test: http://127.0.0.1:8080/api/map/testToken/1/
* Define the life of the TOKEN in settings.py

## API
Example to get the measures according to a sensor ID
```
http://127.0.0.1:8080/api/map/sensor/72/?start=2022-06-08%2001:00:00&end=2022-06-08%2010:10:10
```

Example to get the measures according to a type of sensors for a delected field ID

```
http://127.0.0.1:8080/api/map/field/4/type/2/?start=2022-06-08%2001:00:00&end=2022-06-08%2010:10:10
```