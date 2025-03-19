
# Django with GraphQ



Django with GraphQL

1. Create a Product model with the following fields:
    * name (string)
    * type (string)
    * sku (string, unique identifier)
 
The Product model is defined in the `models.py` 
 



2. Develop a product form to perform CRUD operations on products.

 
A Django form is created in `forms.py` to handle CRUD operations
 


3. Implement GraphQL mutations for:
    * Adding a new product
    * Updating an existing product
    * Deleting a product
```javascript
  mutation {
    createProduct(name: "iPhone 3s", type: "Mobile", sku: "IPHONE3s", quantity: 50) {
        product {
            name
            type
            sku
            quantity
        }
    }
}

mutation {
    updateProduct(sku: "IPHONE15", name: "iPhone 15 Pro", quantity: 100) {
        product {
            name
            type
            sku
            quantity
        }
    }
}

mutation {
    deleteProduct(sku: "IPHONE15") {
        success
        message
    }
}
```






4. Implement a GraphQL query to:
    * Fetch all products
    * Apply filters based on product type and search query
```javascript
query {
    allProducts {
        name
        type
        sku
        quantity
    }
}


query {
    allProducts(type: "Smartphone") {
        name
        type
        sku
        quantity
    }
}


query {
    allProducts(search: "iPhone") {
        name
        type
        sku
        quantity
    }
}
```

5. Create Django views/pages for:
    * Displaying a product list
    * Adding a new product
    * Updating an existing product

http://127.0.0.1:8000/graphql
http://127.0.0.1:8000/products/                                          view all products.
http://127.0.0.1:8000/products/create/                           add a new product.
http://127.0.0.1:8000/products/update/sku_value/   edit a product.
http://127.0.0.1:8000/products/delete/sku_value/    popup and delete automatically


6. Implement product deletion using the JavaScript library Swal:
    * Use swal.fire to show a confirmation popup before deleting a product.

http://127.0.0.1:8000/products/                                          view all products.



views.py       for handling product operations handle HTTP requests
forms.py      for managing products in HTML pages
urls.py 	for URL routes
schema.py for graphql Queries & Mutations
settings.py for INSTALLED_APPS and configures graphql in Django.



## Screenshots

![App Screenshot](https://i.ibb.co/tpxrhMRL/productlist.png)

![App Screenshot](https://i.ibb.co/2YdgyTjR/add-product.png)