# Flask

## Project Structure

Create a directory structure:
```console
myproject
   env
   static
   templates
   app.py
```

## Virtual ENV


```console
cd myproject
$ virtualenv env
$ source env/bin/activate
```

## Install Flask

```console
(env) $ python3 -m pip install flask
(env) $ python3 -m pip install Flask-SQLAlchemy
```

## Run Server

```console
(env) $ python3 app.py
```

## Models

Create a models.py file, then run

```console
db.create_all()```

## References

https://www.youtube.com/watch?v=Z1RJmh_OqeA

https://github.com/jakerieger/FlaskIntroduction
