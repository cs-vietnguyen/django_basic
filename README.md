# Home test backend

# Quickstart

1.
```
docker-compose up --no-recreate -d mysql
```

Waiting ~10s for MySQL to available

2.
```
docker-compose build
```

For build core service image

3.

```
docker-compose run --no-deps --rm -p 8000:8000 core_service
```

For run docker core service container

4.

Connect to [API docs](http://0.0.0.0:8000/swagger/) for views API Documentation