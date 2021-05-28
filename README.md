# **Webshop**

<style>
.guest {color:#6e6e6e; font-family: Comic Sans MS; padding: 7px;}
.user {color:#179637; font-family: Comic Sans MS; padding: 7px;}
.cert-user {color:#199c95; font-family: Comic Sans MS; padding: 7px;}
.admin {color:#b01a2e; font-family: Comic Sans MS; padding: 7px;}
</style>

## **Content**
- [**General info**](#general-info)
  - [**Technologies**](#technologies)
  - [**Installation**](#installation)
- [**Usage**](#usage)
  - [**How can you quickly test it out**](#how-can-you-quickly-test-it-out)
  - [**Important commands**](#important-commands)
  - [**User roles**](#user-roles)


## **General info**
![Generic badge](https://img.shields.io/badge/Python-3.9-blue.svg)
![Generic badge](https://img.shields.io/badge/Django-3.2.1-blue.svg)
![Generic badge](https://img.shields.io/badge/License-MIT-green.svg)

This project is an example of a webshop made with django with connection to MySql database. Shop have implemented systems of:

* Users system
* Creating products
* Buy and sell dashboard
* Searching
* Cart & checkout
* Product and user rating
* And few more...

### **Technologies**
* Django Framework
* MySql Database
* HTML5, CSS & SCSS, Javascript
* Boostrap
* React

### **Installation**

<details>
<summary>Using pipenv</summary>

1. Clone repository - `git clone https://github.com/makubas/webshop-django`
2. Enter project directory - `cd webshop-django `
3. Create virtual environment - `pipenv install -r requirements.txt`
4. Run it - `pipenv shell`
5. Create databases for the project - `python manage.py migrate`
6. Run server - `python manage.py runserver`

</details>
<details>
<summary>Using docker</summary>

1. Clone repository - `git clone https://github.com/makubas/webshop-django`
2. Enter project directory - `cd webshop-django`
3. Open the settings.py file under `/webshop` and change `DATABASES/default/host from 'localhost' to 'db'`
4. Build docker services - `docker-compose build`
5. Create database - `docker-compose up -d db`
6. Run server - `docker-compose up web`

</details>

---

## **Usage**
If you made everything correctly you should see the message that the server is running and you can connect on `localhost:8000`.

After you are see that server is working, register your new account and check out how this works!

If you want to make multiple things at once, run those commands:

### **How can you quickly test it out**

### **Important  `py manage.py` commands**
* `py manage.py createuser <amount>` -> Create user(s), it'll return each user email and password.
* `py manage.py createproduct <amount>` -> This will create user (seller) of the product(s), and than create given amount of random items.

### **User roles**
* <span class="guest">**Guest**</span>: Someone who is on the website without being logged in.
* <span class="user">**User**</span>: Normal user logged in.
* <span class="cert-user">**Certified User**</span>: User can advance to certified by having at least 100 sold products and at least 4 stars rating.
* <span class="admin">**Admin**</span>: User made with `py manage.py createsuperuser`, able to modify everything in database.

## **Website structure**

Full list of subpages on website with role required to acces it:

* `/` <span class="user">**User**</span> Home page with listed products
* `/register` <span class="guest">**Guest**</span> Registration for new accounts
* `/login` <span class="guest">**Guest**</span> Log in to existing account
* `/logout` <span class="user">**User**</span> Log out from account
* `/admin` <span class="admin">**Admin**</span> Admin panel
* `/user-me/` <span class="user">**User**</span> Logged user general informations
  * `/user-me/create-product/` <span class="user">**User**</span> New item creation page
  * `/user-me/selling-products/` <span class="user">**User**</span> Products that user is currently selling
  * `/user-me/sold-products/` <span class="user">**User**</span> List of sold products
  * `/user-me/bought-products/` <span class="user">**User**</span> List of all bought items
  * `/user-me/cart/` <span class="user">**User**</span> Cart with products
* `/user/<username>` <span class="guest">**Guest**</span> Public user page
* `/product/<uuid>/` <span class="guest">**Guest**</span> Specific product page
  * `/product/<uuid>/update/` <span class="user">**User**</span> Form for editing product informations 
* `/purchase/<uuid>` <span class="user">**User**</span> Displays informations about purchase


