## Concepts that would be easily forgotten

### CORS

Need to edit settings.py in backend

```python
MIDDLEWARE = [
    ...
    # add these two line to enable cors
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]
...
# although need to avoid * for security concern, change in the future
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ["*"]
```

### axios

to retrive data from axios, use syntax like

```javascript
let res = await axios.post('http://localhost:8000/login').catch(function (error) {
  console.log(error.response.status);
  console.log('Error', error.message);
});
// res.data() is the json object that we could use
```

### .env

In react app, to access varaible set in .env, you need to

1. set variable name with the prefix of `REACT_APP_`
2. Restart the programming
3. In your js code, use let x = process.env.REACT*APP*{your var} to get environment variable

### reference

[Flat icon in replace of Reacticon](https://www.flaticon.com/)
Maybe the change of jsconfig.json makes the package unable to find bootstrap?

[Add config of Eslint and prettier](https://dev.to/knowankit/setup-eslint-and-prettier-in-react-app-357b)

[sidebar](https://github.com/briancodex/react-sidebar-v1)
