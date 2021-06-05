# **Webshop**

## **Content**
- [**General info**](#general-info)
  - [**Technologies**](#technologies)
  - [**Installation**](#installation)
- [**Website structure**](#website-structure)
  - [**New `py manage.py` commands**](#new--py-managepy-commands)
  - [**Subpages**](#subpages)
  - [**Apps**](#apps)
- [**Usage**](#usage)

## **General info**
![Generic badge](https://img.shields.io/badge/Python-3.9-blue.svg)
![Generic badge](https://img.shields.io/badge/Django-3.2.1-blue.svg)
![Generic badge](https://img.shields.io/badge/License-MIT-green.svg)

The project is basically a repository that I send someone if he asks me what I did as a programmer or what I can do. 

It is a cool webshop made with [Technologies](#technologies).
I was mostly focusing on Django parts

### **Technologies**
* Django framework
* MySql Database
* HTML, CSS & SCSS, Javascript
* Boostrap

### **Installation**

1. Clone repository - `git clone https://github.com/makubas/webshop-django`
2. Enter project directory - `cd webshop-django `
3. In `webshop/settings.py` change `DATABASES { 'default': { 'USER' and 'PASSWORD' } }` to your MySql root user and password, defaults are `USER: root` and `PASSWORD: root`
4. Create new MySql database - `CREATE DATABASE webshopdb;` in your mysql command line client
5. Create virtual environment in project directory (with manage.py) - `pipenv install -r requirements.txt`
6. Run it - `pipenv shell`
7. Create databases for the project - `py manage.py migrate` and `py manage.py makemigrations`
8. Run server - `python manage.py runserver`

## **Website structure**

### **New  `py manage.py` commands**
* `py manage.py createuser <amount>` -> Create user(s), it'll return each user email and password.
* `py manage.py createproduct <amount>` -> This will create user (seller) of the product(s), and then create given amount of random items.


### **Subpages**
Full list of subpages on website. All of that are registered in `app_names/urls.py`. If you are wondering what the `<uuid>` is - [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)

* `/` - Home page with listed products
* `/register` - Registration for new accounts
* `/login` - Log in to existing account
* `/logout` - Log out from account
* `/admin` - Admin panel
* `/user-me/` - Logged user general informations
  * `/user-me/create-product/` - New item creation page
  * `/user-me/selling-products/` - Products that user is currently selling
  * `/user-me/sold-products/` - List of sold products
  * `/user-me/bought-products/` - List of all bought items
  * `/user-me/cart/` - Cart with products
* `/user/<username>` - Public user page
* `/product/<uuid>/` -  Specific product page
  * `/product/<uuid>/update/` - Form for editing product informations
* `/purchase/<uuid>` - Displays informations about purchase

### **Apps**
* Profiles - user related things. User model, `/user-me` views and authentication.
* Products - showing, searching, editing products.
* Purchases - data about made purchases, carts and payments.
* Comments - product comments and stars

## **Usage**
If you made everything correctly you should see the message that the server is running, and you can connect on `http://127.0.0.1:8000`.

After you see that server is working, register your new account and check out how this works!

