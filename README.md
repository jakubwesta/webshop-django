# **Webshop**

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

The project is basically a repository that I send someone if he asks me what I did as a programmer or what I can do. 

It is a cool webshop made with [Technologies](#technologies). I was mostly focusing on Django parts, but of course every website should look cool so I also added (and learned) React.

### **Technologies**
* Django framework
* MySql Database
* HTML, CSS & SCSS, Javascript
* Boostrap
* React (javascript)

### **Installation**

<summary>Using pipenv: </summary>


1. Clone repository - `git clone https://github.com/makubas/webshop-django`
2. Enter project directory - `cd webshop-django `
3. In `webshop/settings.py` change `DATABASES { 'default': { 'USER' and 'PASSWORD' } }` to your MySql root user and password, defaults are `USER: root and PASSWORD: root`
4. Create new MySql database - `CREATE DATABASE webshopdb;` in your mysql command line client
5. Create virtual environment in project directory (with manage.py) - `pipenv install -r requirements.txt`
6. Run it - `pipenv shell`
7. Create databases for the project - `py manage.py migrate` and `py manage.py makemigrations`
8. Run server - `python manage.py runserver`


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

## **Website structure**

### **New  `py manage.py` commands**
* `py manage.py createuser <amount>` -> Create user(s), it'll return each user email and password.
* `py manage.py createproduct <amount>` -> This will create user (seller) of the product(s), and than create given amount of random items.

### **User roles**
* **Guest**: Someone who is on the website without being logged in.
* **User**: Normal user logged in.
* **Certified User**: User can advance to certified by having at least 100 sold products and at least 4 stars rating.
* **Admin**: User made with `py manage.py createsuperuser`, able to modify everything in database.

### **Subpages**
Full list of subpages on website with role required to acces it. All of that are registered in `app_names/urls.py`. If you are wondering what the `<uuid>` is - [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)

* `/` - **User** - Home page with listed products
* `/register` - **Guest** - Registration for new accounts
* `/login` - **Guest** - Log in to existing account
* `/logout` - **User** - Log out from account
* `/admin` - **Admin** - Admin panel
* `/user-me/` - **User** - Logged user general informations
  * `/user-me/create-product/` - **User** - New item creation page
  * `/user-me/selling-products/` - **User** - Products that user is currently selling
  * `/user-me/sold-products/ - **User** - List of sold products
  * `/user-me/bought-products/` - **User** - List of all bought items
  * `/user-me/cart/` - **User** - Cart with products
* `/user/<username>` - **Guest** - Public user page
* `/product/<uuid>/` - **Guest** - Specific product page
  * `/product/<uuid>/update/` - **User** - Form for editing product informations 
* `/purchase/<uuid>` - **User** - Displays informations about purchase

### **Apps**
* Profiles - handling user related things. User model, `/user-me` views and authentication.
* Products - responsible for showing, searching, editing products and other related things.
* Purchases - Contains data about made purchases, carts and payments.

## **Usage**
If you made everything correctly you should see the message that the server is running and you can connect on `localhost:8000`.

After you see that server is working, register your new account and check out how this works!

