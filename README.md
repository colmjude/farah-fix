# A flask starter project

Dependencies

* python 3.9+
* virtualenv
* postgres
* postgis

## Get started

I recommend working in a virtualenv. Create one with

```
mkvirtualenv <name-of-your-virtualenv>
```

### Create a DB (with postgis extension)

Create a database with

```
Createdb <name>
```

Then open DB

```
psql <name>
```

Add `postgis` extension

```
CREATE EXTENSION postgis;
```

You'll then need to update the pointer to the db in `.flaskenv`.

### Get flask running

Install python packages with

```
make init
```

Then run the application with

```
make run
```
