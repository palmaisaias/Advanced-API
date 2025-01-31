# E-commerce API

This is a factory application pattern, e-commerce API. The application runs using Flask, and all requirements can be found under `requirements.txt`. The API features limiter options as well as caching options.

## Brief Description

This e-commerce API allows for the creation of new customers. Upon creation, customers receive basic information such as name, phone, email, username, password, and role (for further access). Some routes are protected by either an authorization code or by role clearance. For this, the user receives an auth code whenever they log in, which they can use to access certain routes, place items in their cart, view their cart, and place their order. Certain routes, such as viewing all products, are unrestricted.

## Routes

### Customer Routes
- Create a new customer
- Get customer by ID
- Update a customer
- Get all customers
- Find all customers in a paginated fashion
- Log in a customer
- Delete a customer

### Order Routes
- Place an order
- Get information on a specific order by ID
- Get all orders
- Find all orders in a paginated fashion

### Product Routes
- Create a product
- Get all products
- Update a product
- Delete a product
- Find all products in a paginated fashion

### Cart Routes
- Add to cart
- Remove from cart
- Get the contents of the entire cart
- Clear the cart

## Models
- Cart model
- Cart item model
- Customer model
- Order model
- Order item model
- Product model
- Role model (included for routes protected by role)

## Schemas
- Cart item schema
- Cart schema
- Customer schema
- Order items schema
- Order schema
- Product schema
- Schema file that initializes Marshmallow

## Controllers
- Cart controller
- Customer controller
- Order controller
- Product controller

## Services
- Cart service
- Customer service
- Order service
- Product service

## Documentation
The Swagger documentation file is located under the `static` folder. The endpoint for accessing the documentation is `localhost/API/docs`.
