# CodeAlpha_simple-e-commerce-store

# Electronics Store – Django E-Commerce Application

## Overview

Electronics Store is a web-based E-Commerce application developed using Django. It allows users to browse products, view details, add items to a cart, manage quantities, register/login, and place orders.

## Features

* User Registration and Login
* Product Listing and Search
* Product Details Page
* Shopping Cart Management
* Quantity Increase/Decrease
* Order Placement (Checkout)
* Admin Product Management

## Technologies Used

* Python
* Django
* SQLite
* HTML
* CSS
* Django Authentication

## Project Structure

```text
ecommerce/
│
├── store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── home.html
│   ├── product_detail.html
│   ├── cart.html
│   ├── login.html
│   └── register.html
│
├── static/css/style.css
├── media/
└── db.sqlite3
```

## Installation

```bash
pip install django pillow
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Modules

### User Module

* Register
* Login
* Logout

### Product Module

* View Products
* Product Details
* Search Products

### Cart Module

* Add to Cart
* Increase/Decrease Quantity
* Remove Items
* View Total Price

### Order Module

* Checkout
* Order Creation

## Conclusion

This project demonstrates a complete E-Commerce system using Django with user authentication, product management, shopping cart functionality, and order processing in a simple and user-friendly interface.
