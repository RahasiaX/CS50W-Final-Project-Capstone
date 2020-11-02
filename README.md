# HarvardX CS50W: Web Programming with Python and JavaScript

Project video: https://youtu.be/I060MD4rBBY

## REQUIREMENTS

The final project is our opportunity to design and implement a dynamic website of our own. So long as our final project draws upon Harvard CS50W's lessons, the nature of our website will be entirely up to us.

In this project, we are asked to build a web application of our own. The nature of the application is up to us, subject to a few requirements:

- Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
- Your web application must be mobile-responsive.
- In a README.md in your project’s main directory, include a short writeup describing your project, what’s contained in each file you created, and (optionally) any other additional information the staff should know about your project. This file should also provide your justification for why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.
- If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to a requirements.txt file!

Beyond these requirements, the design, look, and feel of the website are up to you!


## SNEAKER CLUB

The website I made is called Sneaker Club. It is an e-commerce website that sells popular sneakers from the biggest sneaker brands.

The reason I went for an e-commerce website is that I used to run a webshop myself. Back then I used a template on Shopify to make the website. However, I soon figured out that most templates are very limited feature-wise, so eventually I tried to customize my webshop by adding custom blocks.

With this website, I wanted to challenge myself and see how easy/hard it is to implement many of the common features that all the big websites use, from a filter system to a working payment processor.

### Features
- Responsive navigation bar
- As-You-Type search bar
- Shoe filter (including clear all filters button)
- Cart
- Checkout with Paypal payments
- Shoe size selecter
- Shoe recommendations on product page
- Pop-up size guide


## FILES

### capstone.js
This js files contains most of the javascript used on the website. Some of features done with javascript:
- Shoe filter
- Search bar
- Dropdowns on product pages
- Shoe selector
- Add-to-cart button

### styles.css
All the css for the entire website.

### templates
- cart.html
- checkout.html
- index.html
- layout.html
- login.html
- product_page.html
- register.html
- sneakers.html

### filters.py
Contains the filter models and filter choices.

### models.py
Contains all the User, Shoe and Order models.


## PROJECT LEARNINGS
This project has been a lot of fun. It's far from perfect, but I have learned so much from trying/failing and adding many features on top of the features we have learned in this course up until this project.

My main goal for this final project was to get a better understanding not only from the back-end, but also the front-end. I spent a lot of time digging into many different Django packages and trying out different styling methods with CSS.

Thanks to this final project, I have learned the following:

### Django
- Filtering system by using the django-filter package.
- Models:
  - How to build a set of models for products with multiple variations. In this case, selling shoes with multiple sizes, but also different prices for each size.
  - Using meta's within the models.
  - Using tuples within model classes.
- Template tag filtering.

### Javascript
- Use of fetch and how to process/use the data.
- How to call a certain div/block/tag and change/use its properties.
- Cart showing number of items in navigation bar
- As-you-type search bar
- Adding Paypal payments and using website data

### Python
- Dictionaries and Sets operations.
- Try/Except
- HttpResponses/JsonResponses

### HTML/CSS
- Using font-awesome icons
- Using bootstrap
- Using modal dialogs
- Using flexbox to align divs next to eachother while being responsive.
- Making an image slider