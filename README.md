# URBAN Designer

The live website can be viewed [here](https://xxxx.com/)      
<img src="xxxxx" alt="mockup" target="_blank" rel="noopener" width="850">

---
## Table of Contents
1. [**Why This Project**](#why-this-project) 
2. [**UX**](#ux)
    - [**Why This Project**](#why-this-project) 
    - [**User Stories**](#user-stories)
    - [**Design**](#desing)
    - [**Wireframes**](#wireframes)
    - [**Database Schema**](#database-schema)
3. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
4. [**Technologies Used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Libraries and Frameworks**](#libraries-and-frameworks)
    - [**Tools**](#tools)
    - [**Databases**](#databases)
    - [**Version Control**](#version-control)
    - [**Hosting**](#hosting)
5. [**Testing**](#testing)
    - [**Code Validation**](#code-validation)
    - [**Automated Testing**](#automated-testing)
    - [**Manual User Testing**](#manual-user-testing)
    - [**Interesting Bugs Or Problems**](#interesting-bugs-or-problems)
6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)
7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Acknowledgements**](#acknowledgements)
---

**URBAN Designer** is Franco Faura Tellez UX Designer first e-commerce website. 
He also has a Behance profile where he is always very active in updating new content. 
With this page, he will be able to offer customers the possibility to buy his services packages. 
The site includes a page for his services nut also his biography, portafolio and cv where people will be able to know more about him 
and his work and also a get in touch area to make contact with potential customers.

---

## UX
### Why This Project
The aim of this project is to create a Full Stack web app to fully demonstrate the learnings throughout the course. 
A pass in this project is required to pass the course and obtain certification. 
The site will use Python and the Django Framework with a back-end db (PostgreSQL) for the back-end stack. 
Bootstrap 4 and HTML will be used on the front-end stack.
### Audience
- People who works with UX design
- People who want to get acquainted with UX design
- People who want to buy a UX design service package

### User Stories 
<details>
<summary>Click to see - User Stories Table</summary>

&nbsp;


User story ID | As a | Want to be able to... | So that I can...
--------------|---------|------------------------|-----------------
|             ||        **Viewing and Navegation**            ||
1 - | Shopper | View a list of services | Select some to purchase
2 - | Shopper | View individual services details | Identify the price, description, service rating, service duration, etc
3 - | Shopper | Easily view the total of my purchase at any time | See how much I want to spend
|             || **Registration and User accounts** ||
4 - | Site user | Easily register for an account | Have a personal account to be able to view my profile
5 - | Site user | Easily login or logout	|  Access my personal account information
6 - | Site user | Easily recover my password in case I forget  | Recover access to my account
7 - | Site user | Receive an email confirmation after registering | Verify that my account registration was successful
8 - | Site user | Have a personalized user profile | View my personal order history and order confirmations, and save my payment information
|             || **Purchasing and Checkout** ||
9 -	| Site user | Search for a specific service example from the portafolio	| Find a specific service example from the portafolio I would like to purchase 
10 - | Site user | Easily see what I have search for and the number of results | Quickly decide whether the service I want is available
|             || **Purchasing and Checkout** ||
11 - | Shopper |	Easily select the service when purchasing it. |	Ensure I do not accidentally select the wrong  service
12 - | Shopper |	View items in my bag to be bought	| Identify the total cost of my purchase and all services I will receive
13 - | Shopper | Adjust the number of services in my bag |	Easily make changes to my purchase before checkout
14 - | Shopper |	Easily enter my payment information	| Check out quickly and with no hassles
15 - | Shopper |	Feel my personal and payment information is safe and secure	| Confidently provide the needed information to make a purchase
16 - | Shopper |	View an order confirmation after checkout	| Verify that I haven't created any mistakes
17 - | Shopper |Receive an email confirmation after checking out |	Keep the proof of what I've purchased for my records
|             || **Admin and Store Management** ||           |
18 - | Store Owner | Add an service	| Add new services in my web-shop
19 - | Store Owner | Edit/Update an service	| Change title, prices and description of services
20 - | Store Owner | Delete a service |	Remove services that are not available
</details>

### Design
##### Framework
- [Bootstrap](https://www.bootstrapcdn.com/), front-end framework is chosen for this project for its modern interface, ease of use and ability to be easily customized. 
It is used for creating features such as navbar, cards, forms, modals, as well as for the layout.
- [JQuery](https://jquery.com/) is used for initializing some Bootstrap components, as well as for custom functions, DOM manipulation.
#### Colour Scheme
One of the main goals in UI was to focus user's attention on the UX designer and his services. Therefore **clean**  but **emotives** colors and **different shades** of 
one colour were mostly used accross the website's design.   
Different shades of grey colour and shadows allow us to create clean and neat backgrounds and volume effect accross the website.   
 
![Color Palette](wireframes/colour-palette.png) ASK FRANCO!
#### Typography
There are three fonts used across the project that I find a good combination: 
- [Open Sans](https://fonts.google.com/specimen/Open+Sans) used as the main body font, popular modern sans-serif typeface providing good readability.
- [Marko One](https://fonts.google.com/specimen/Marko+One) - elegant, decorative and eye-catching font, used mostly for headings.  
- [Sawarabi Mincho](https://fonts.google.com/specimen/Sawarabi+Mincho) - clean and simple font, perfectly fit to the "Art of Tea" and "East culture" theme, used for navbar elements and some headings.
#### Icons
Icons are used widely, as they are good attention grabbers. They help users to find and scan content quickly and easily. Another advantage of using them is to help to break language barriers. They create more user-friendly experience for people with non-native English by giving the visual clue about the subject.   
- I used [FontAwesome](https://fontawesome.com/) as the main icon library across the project (e.g. for social media links, forms, cart, search and user icons in navigation).

### Wireframes
[Balsamiq Wireframes](https://balsamiq.com/) tool was used to create all wireframes for the project.   
Original wireframes for desktop, tablet and mobile can be found [here](https://xxxxx).
**Note:** The website was changed and evolved through the development process and several improvements were applied.
The wireframes served as guidelines but some details such as positioning, placement of images, buttons and other refinements diverge from the original wireframes.   

### Database Schema
During the development phase I worked with **sqlite3** database which is installed with Django.   
For deployment(production), a **PostgreSQL** database is provided by Heroku as an add-on.
- The **User model** used in this project is provided by Django as a part of defaults `django.contrib.auth.models`. More information about Django’s authentication system can be found [here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>
---

## Features
URBANO D'sign website is composed by eight applications: `landing`, `about`, `Portafolio`, `Blog`, `services`, `shopping bag`, `checkout`, `profiles`.

### Existing Features     TO BE MODIFIED
#### Navbar
- **logo**, that is clickable and redirects to the landing page and also a small paragraph about the company
- **quick links** to the main pages
- **contact information** that contains address, phone number and email

#### Landing (home) pag

The landing page serves to attract new users to the business, to give a clear understanding about that and to attract users to use the website's functionality (book ceremony/buy products). 
Smooth animation on scroll is apllied to almost all sections of the page(mostly to images and icons). Tha landing page consists of 9 sections:
#### About page
#### Portafolio page
#### Login/Register page
#### Services packages page
#### Service details page
#### Shopping bag page
#### Checkout page
#### Checkout Success page
#### Profile page
#### Order History
#### Admin product managment
#### Django-allauth features
##### Sign Up
##### Login
##### Forgot password
##### Logout
#### 404 and 500 error pages
Custom 404 and 500 pages contain heading, short information about the error and a button "Back Home". As well as that, they display navbar that allows users to come back easily to any page if they got lost.

### Features Left to Implement
There are some features that I considered were of secondary importance and I have not implemented them yet due to time constraints, but intend to do so in future when I will be able to dedicate more time to them. Most of these features are displayed in my [original wireframes](https://github.com/irinatu17/Art-of-Tea/tree/master/wireframes).
#### Star based  Rating and Reviews
This will be the first priority feature I would like to implement in future. Users would be able to create, edit and delete their reviews for products and services. Rating would be displayd as stars(0-5) in the product details and service details pages. Also, in the landing page reviews section, the static reviews would be replaced with the real ones, displaying up to 5 random reviews from the database.
####  Social account login (Google and Facebook)
This feature allows users to login using social networks accounts, Google and Facebook, that would enhance user experience and make the login process easier.

Other small features are also considered to be implemented in feature, such as **Back to Top button** or/and **Pagination** in products, **Scroll down button** on the landing page, **Sorting products** by price/name, **Discout system**.     
I would also like to add **more products** to the store.

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>
---

## Technologies Used

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/) 
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - templating language for Python, to display back-end data in HTML.

### Libraries and Frameworks
- [Django](https://www.djangoproject.com/) - Python framework for building the project.
- [Bootstrap](https://www.bootstrapcdn.com/) - as the front-end framework for layout and design.
- [Google Fonts](https://fonts.google.com/) - to import fonts.
- [FontAwesome](https://fontawesome.com/) - to provide icons used across the project. 
- [JQuery](https://jquery.com/) - to simplify DOM manipulation and to initialize Bootstrap functions.
- [Gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server to enable deployment to Heroku.
- [Psycopg2](https://pypi.org/project/psycopg2/) - to enable the PostgreSQL database to function with Django.
- [Stripe](https://stripe.com/ie) - to handle financial transactions.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - to style Django forms.

### Tools
- [GitPod](https://www.gitpod.io/) - an online IDE for developing this project.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [AWS S3 Bucket](https://aws.amazon.com/) -  to store static and media files in prodcution.
- [WhiteNoise](http://whitenoise.evans.io/en/stable/) - to store static files during develompment.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for compatibility with AWS.
- [Travis](https://travis-ci.org/) - for integration testing.
- [TinyPng](https://tinypng.com/) - for compressing images.
- [ImgBB](https://imgbb.com/) - to host images used in README and also services/products images to provide URLs.
- [GIMP2](https://www.gimp.org/) - for editing and resizing images.
- [Balsamiq](https://balsamiq.com/) - to create wireframes.
- [Coolors.co](https://coolors.co/) - to create colour palette used in the README.

### Databases
- [SQlite3](https://www.sqlite.org/index.html) - a development database.
- [PostgreSQL](https://www.postgresql.org/) - a production database.

### Version Control
- [**GitHub**](https://github.com/) - as a remote repository to push and store the committed changes to my project from Git.

### Hosting
- [**Heroku**](https://www.heroku.com/) - as the hosting platform to deploy my app.

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---
## Testing
Testing information can be found in a separate [TESTING.md](https://github.com/irinatu17/Art-of-Tea/blob/master/TESTING.md) file

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Deployment
The Art of Tea project was developed using the [GitPod](https://www.gitpod.io/) online IDE and
using Git & GitHub for version control. It is hosted on the [Heroku](https://heroku.com/) platform, with static files on WhiteNoise and user-uploaded images being hosted in AWS S3 Basket.
### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE of your choice (I used [GitPod](https://www.gitpod.io/) for creating this project)
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python3](https://www.python.org/download/releases/3.0/)    

Apart from that, you also need to create accounts with the following services:
- [Stripe](https://stripe.com/en-ie)
- [AWS](https://aws.amazon.com/) to setup the [S3 basket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- [Gmail](https://mail.google.com/)

#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:   
`git clone https://github.com/irinatu17/Art-of-Tea`    
Alternatively, you can save a copy of this repository by clicking the green button **Clone or download** , then **Download Zip** button, and after extract the Zip file to your folder.      
In the terminal window of your local IDE change the directory (CD) to the correct file location (directory that you have just created).       

Note: You can read more information about the cloning process on the [GitHub Help page](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).   

2. Set up environment variables.     
Note, that this process will be different depending on IDE you use.   
In this it was done using the following way:      
    - Create `.env` file in the root directory.
    - Add `.env` to the `.gitignore` file in your project's root directory
    - In `.env` file set environment variables with the following syntax:     
    ```bash 
    import os  
    os.environ["DEVELOPMENT"] = "True"    
    os.environ["SECRET_KEY"] = "<Your Secret key>"    
    os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
    os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
    os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"    
    os.environ["GOOGLE_MAP_KEY"] = "<Your Google Map key>" 
     ```
       
Read more about how to set up the Stripe keys in the [Stripe Documentation](https://stripe.com/docs/keys)
    
3. Install all requirements from the **requirements.txt** file putting this command into your terminal:     
`pip3 install -r requirements.txt`     
4. In the terminal in your IDE migrate the models to crete a database using the following commands:    
`python3 manage.py makemigrations`     
`python3 manage.py migrate`     
5. Load the data fixtures(**categories**, **products**, **itinerary**, **itinerary_items**, **events**) in that order into the database using the following command:    
`python3 manage.py loaddata <fixture_name>`        
6. Create a superuser to have an access to the the admin panel(you need to follow the instructions then and insert username,email and password):    
`python3 manage.py createsuperuser`   
7. You will now be able to run the application using the following command:     
`python3 manage.py runserver`     
8. To access the admin panel, you can add the `/admin` path at the end of the url link and login using your superuser credentials.

### Heroku Deployment
*To start Heroku Deployment process, you need to clone the project as described in the [Local deployment](#local-deployment) section above.*     
To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:    
1. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:    
`pip3 freeze > requirements.txt`    
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:      
`web: gunicorn art_of_tea.wsgi:application`    
3. `git add`, `git commit` and `git push` these files to GitHub repository.     
NOTE: these 1-3 steps already done in this project and included in the GitHub repository, but illistrated here as they are required for the successfull deployment to Heroku.        
As well as that, other things that are required for the Heroku deployment and have to be installed: **gunicorn** (WSGI HTTP Server), **dj-database-url** for database connection and **Psycopg** (PostgreSQL driver for Python). All of the mentioned above are *already installed* in this project in the requirements.txt file.     
4. On the [Heroku](https://heroku.com/) website you need to create a **new app**, assigne a name (must be unique),set a region to the closest to you(for my project I set Europe) and click **Create app**.   
5. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type `postgres`), select **Hobby Dev — Free** and click **Provision** button to add it to your project.     
6. In Heroku **Settings** click on **Reveal Config Vars**.   
7. Set the following config variables there:     

| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| DATABASE_URL| `<your postgres database url>`  |
| EMAIL_HOST_PASS | `<your email password(generated by Gmail)>` |
| EMAIL_HOST_USER| `<your email address>`  |
| GOOGLE_MAP_KEY| `<your google map key>`  |
| SECRET_KEY | `<your secret key>`  |
| STRIPE_PUBLIC_KEY| `<your stripe public key>`  |
| STRIPE_SECRET_KEY| `<your stripe secret key>`  |
| STRIPE_WH_SECRET| `<your stripe wh key>`  |
| USE_AWS | `True`  |

Note: More about Google Map key settings can be found [here](#google-maps-api-key-set-up).
     
8. Copy **DATABASE_URL's value**(Postrgres database URL) from the Convig Vars and temporary paste it into the default database in **settings.py**.     
You can temporary comment out the current database settings code and just paste the following in the settings.py:   
```bash 
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
  ```
Important Note: that's just temporary set up, this URL **should not be committed and published to GitHub** for security reasons, so make sure not to commit your changes to Git while the URL is in the settings.py.     
9. Migrate the database models to the Postgres database using the following commands in the terminal:    
`python3 manage.py makemigrations`     
`python3 manage.py migrate`     
10. Load the data fixtures(**categories**, **products**, **itinerary**, **itinerary_items**, **events**) into the  Postgres database using the following command:     
`python3 manage.py loaddata <fixture_name>`      
11. Create a **superuser** for the Postgres database by running the following command(*you need to follow the instructions and inserting username,email and password*):      
`python3 manage.py createsuperuser`     
12. You need to remove your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.    
Note: for production you get the environment variable 'DATABASE_URL' from the Heroku Config Vars and use Postgress database, while for development you use the SQLite as a default database.     
13. Add your Heroku app URL to **ALLOWED_HOSTS** in the settings.py file.
14. You can connect Heroku to GitHub to automatically deploy each time you push to GitHub.    
To do so, from the Heroku dashboard follow the steps:
-  **Deploy** section -> **Deployment method** -> select **GitHub**
-  link the Heroku app to your GitHub repository for this project
- click **Enable Automatic Deploys** in the Automatic Deployment section
- Run `git push` command in the terminal, that would now push your code to both Github and Heroku, and perform the deployment.     

Alternatively, in the terminal you can run:    
- `heroku login`    
-  after adding and comitting to Git, run the following command:     
`git push heroku master`
15. After successful deployment, you can view your app bu clicking **Open App** on Heroku platform.
16. You will also need to verify your email address, so you need to login with your superuser credentials and verify your email address in the admin panel. Now you will be able to view the app running!    
##### Hosting media files with AWS
The **static files** and **media files** (that will be uploaded by superuser - product/service images) are hosted in the [AWS S3 Bucket](https://aws.amazon.com/). To host them, you need to create an account in AWS and create your S3 basket with *public access*. More about setting it up you can read in [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) and [this tutorial](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).
##### Senging email via Gmail
In order to send real emails from the application, you need to connect it to your **Gmail account**, setting up your **email address** in EMAIL_HOST_USER variable and your **app password** generated by your email provider in EMAIL_HOST_PASS variable.


<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Credits
### Code
- The project's code was developed by following the [Code Institute](https://codeinstitute.net/) video lessons and based on the understanding of the Boutique Ado Django Mini-Project, but was customized, modified and enhanced to fit the project purposes. Some comments with credits to that were added to some parts of the code, where needed.
- [Stack Overflow](https://stackoverflow.com/) was extremely helpful and useful during the process of building this project, credits for the certain solutions are given in the comments.
- I also constantly referred to the following documentation sources during the development: [Django](https://docs.djangoproject.com/en/3.1/), [Stripe](https://stripe.com/docs).
### Content and Media
- 

### Acknowledgements
I would like to thank everyone who has helped me throughout the development of this project:      
- **My mentor** [Guido] for his guidance, very useful tips and advice!         
- **Code Institute tutors** Tim, Michael, Miklos, Stephen, Anna, Samantha, Haley and others for their help to debug issues, assistance and support!    
- Many thanks to my fellow students, **Slack community** and, of course, **my friends** and **my family** for the time, patience, help and support!         

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---

## Disclaimer
This site is made for **educational purposes** only.        

## Issues
- Colors styling to match mobile and desktop view after test-user feedback. 
- Homogenize colors for primary/secondary btns across different tabs and for nav. 
- Nav and Mobile-Top-header invading the main div in small screen sizes. Corrected via media queries.
- Nav active feature implemented with if statement with the help of mentor.
- About section: Implemented bootsrap slider for about me, reviews and portafolio.
- About landing image fitted as hero-img css.
- About me section implemented as per client's feedback.
- About contact form implemented. Connected with Email.js. Difficulties implementing the code as the tutorial from the course is not updated. Load.gif was achieve using }{% static%}
- Services grid/list implemented from online example when client want to add more products/services.
- Service json files added rating feature from the terminal to text how to do it. 
For future to add rating to the service card information generated by reviewers.
- Service detail card original layout restyled as per UX design received feedback.
- Quantity btn resize for small screen using media queris.
- Implemented datepicker function using boostrap instead of materialize and connect with back end.
- Bag view: add to bag. Implemented if/else logic for adding a service without duplicating date selection during session(bag shop) and preventing same service double purchase error.
For future a calendar database should be implemented to avoid other clients booking on occupied timeslots.
- PENDING datapicker for other apps: checkout Bag.
- Shopping bag restyle as per test user feedback for user friendlyness. Idea to use boostrap dnone to hide/show views depending on sizes, together with redistributions of code snip to different sections.
- Admin: defensive modal installed to prevent edit/delete a service by mistake using boostrap.
- Admin: Date(Timestamp) and select_date(book_date) added to the Admin view. 
- Services images if conditioned improved to search for image in static folder, url_link or non-available image. Fix feature across all apps.
Discovered instrinsice property When images are uploaded from url-link which lowers the resolution of the image. For this reason prefered chooice to upload images from Folder.
Improved image resolution and responsiveness.
- My profile: implemented full name value pre-fill feature to the checkout order.
- Portafolio full page vertical slider implemented with bootstrap instead of horizontal customized to fit between the NAV or footer.
- PENDING: Portafolio images are quite heavy pending to reduce this.
- Portafolio images uploaded to Portafolio database json. 
- PENDING: portafolio json file, view, model, url pending to implement in order to re-use and optimize code.
- Blog app requested from client. Pending to implement for this project due to timelines.
- PENDING: to add entity selection relationship between databases for json files. 
- Allauth templates customized for this project.
- All images relocated to the correct folder of static as per mentor's feedback.
*Images provided by Client and for the service part obtain from google images for the purpose of this exercise. 

<div align="right">
    <b><a href="#table-of-contents">↥ Back To Top</a></b>
</div>

---