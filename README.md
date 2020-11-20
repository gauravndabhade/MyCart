# MyCart

Commandline interface for E-commerce app


## Prerequirement

- python 3.6

## Setup project

Create virtual environment and install requirements

```sh
$ python3.6 -m venv env
$ source env/bin/activate
(env) $
(env) $ pip install -r requirements.txt
(env) $ python setup.py install
```


Now, application will be available on command line

```sh
(env) $ mycart
Usage: mycart [OPTIONS] COMMAND [ARGS]...

  A Product Search and MyCart CLI

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  add-item     Create new product
  bill         Create bill for your cart items
  category     Get all category from your cart
  dropdb       Clear database
  initdb       Initialize database
  product      Get all products from your cart
  remove-item  Remove product
  user
```

Run test for application
```sh
(env) $ pytest 
```