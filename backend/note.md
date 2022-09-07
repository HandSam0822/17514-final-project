### CORS Policy
Since we want to send request from frontend(currently http://localhost:3000)
to backend(currently http://localhost:8000), it would cause CORS.
To solve this problem, we could reference [django-cors-guide](https://www.stackhawk.com/blog/django-cors-guide/).

Basically, we need to apply cors middleware and specify which origin we trust