# MyCart

Command-line interface for E-commerce app


## Pre-requirement

- python 3.6

### Setup project

Create virtual environment and install requirements

```sh
➜  MyCart git:(main) ✗ python3.6 -m venv env
➜  MyCart git:(main) ✗ source env/bin/activate
(env) ➜  MyCart git:(main) ✗ pip install -r requirements.txt
(env) ➜  MyCart git:(main) ✗ python setup.py install
```


Now, application will be available on command line

```sh
(env) ➜  MyCart git:(main) ✗ mycart        
Usage: mycart [OPTIONS] COMMAND [ARGS]...

  MyCart, An E-commerce cli application

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  add-item     Add new product into cart
  bill         Create bill for your cart items
  category     Manage category
  dropdb       Clear/Delete database
  initdb       Initialize database
  product      Manage products
  remove-item  Remove product from cart
  user         Manage user

```

### Initialise database
```shell
(env) ➜  MyCart git:(main) ✗ mycart initdb          
MyCart
--------------------------------------------------------------------------------
User login or Create new account to MyCart
Initialized the database
(env) ➜  MyCart git:(main) ✗ 


```

### Use commands to manage cart
```shell
(env) ➜  MyCart git:(main) ✗ mycart bill --help           
Usage: mycart bill [OPTIONS]

  Create bill for your cart items

Options:
  --help  Show this message and exit.
(env) ➜  MyCart git:(main) ✗ mycart bill            


MyCart 							 Login as: db [ADMIN]
--------------------------------------------------------------------------------
Categories
+--------+
|  Name  |
+--------+
| Books  |
| Mobile |
+--------+
Products
+---------------+---------+
|     Name      |  Price  |
+---------------+---------+
| The Alchemist | 1000.0  |
|    OnePlus    | 20000.0 |
+---------------+---------+
Cart
+---------------+---------+
|     Name      |  Price  |
+---------------+---------+
| The Alchemist | 1000.0  |
|    OnePlus    | 20000.0 |
+---------------+---------+
--------------------------------------------------------------------------------
Bill : 			PURCHASE ORDER OF MINIMUM 10000/-, AND GET DISCOUNT!!!
 	Total : 	21000.0
 	Discount :	500.0
			--------
			20500.0
(env) ➜  MyCart git:(main) ✗ 

```


## Run test for application
```shell
(env) ➜  MyCart git:(main) ✗ pytest
============================= test session starts ==============================
platform linux -- Python 3.6.12, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: /home/db/Documents/Gaurav/github.com/MyCart, configfile: pytest.ini, testpaths: tests
collected 13 items                                                             

tests/test_controller_cart.py ..
tests/test_controller_category.py ...
tests/test_controller_product.py ...
tests/test_controller_user.py .....

============================= 13 passed in 21.99s ==============================
(env) ➜  MyCart git:(main) ✗ 
```