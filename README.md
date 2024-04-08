# Spacey Capital API 🚀

This project provides a RESTful API for managing employees, products, customers, and bills. It also includes analytics on sales data.

## Table of Contents 📚

- Models
- Views
- URLs

## Models 📦

The project includes the following models:

- `Employee`
- `Product`
- `Bill`
- `Customer`

## Views 👀

### Employee Views 👥

- `EmployeeListCreate`: This view is used to create and retrieve the employee details.
- `EmployeeRetrieveUpdateDestroy`: This view is used to retrieve, update, and delete the employee details.
- `EmployeePasswordUpdate`: This view is used by the employee to update their password without changing the other fields.

### Product Views 🛍️

- `ProductListCreate`: This view is used to create and retrieve the product details.
- `ProductRetrieveUpdateDestroy`: This view is used to retrieve, update, and delete the product details.

### Customer Views 🧑‍💼

- `CustomerListCreate`: This view is used to create and retrieve the customer details.
- `CustomerRetrieveUpdateDestroy`: This view is used to retrieve, update, and delete the customer details.

### Bill Views 💵

- `BillListCreate`: This view is used to create and retrieve the bill details. It also calculates the total amount of the bill (including the discount) and deducts the stock of the product.
- `BillRetrieveUpdateDestroy`: This view is used to retrieve, update, and delete the bill details.

### Analytics 📊

- `Analytics`: This view is used to generate analytics on the sales data. It generates the top 5 selling products by the REVENUE generated, the employee who has generated the most REVENUE, the top 5 selling products by the QUANTITY sold, and the employee who has sold the most QUANTITY.

## URLs 🌐

The project includes the following URLs:

- Employees API: `/employees/`, `/employees/<int:pk>/`, `/employees/<int:pk>/password/`
- Customers API: `/customers/`, `/customers/<int:pk>/`
- Products API: `/products/`, `/products/<int:pk>/`
- Bills API: `/bills/`, `/bills/<int:pk>/`
- Analytics API: `/analytics/`
- JWT: `/token/get/`, `/token/refresh/`
- DRF Spectacular URLs: `/api/schema/`, `/api/schema/redoc/`

