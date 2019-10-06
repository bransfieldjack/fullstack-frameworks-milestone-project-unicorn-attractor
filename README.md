# Full Stack Frameworks Milestone Project - Unicorn Attractor App

### This app can bee accessed from the following link: [Unicorn Attractor](https://unicorn-attractor-ci.herokuapp.com/)

![UA](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/ua.PNG)

The unicorn attractor is a modern start-up venture.
The business model for this app centres around the idea of an online, open source community contributing capital and ideas to its development. 
The unicorn attractor offers software development services and bug fixes for free, but a small fee from any user requesting an additional feature on the site. 
The applications primary means of collecting user information is in the form of issue/work tickets, not too dissimilar to what you might find in a modern CRM. 
Each ticket displays one of three different status'; assigned, in progress or completed. 
Issues or tickets are logged to two different categories; bugs/defects in the application which will be fixed for free, and feature additions which will only be implemented for a chargeable fee. 

The application facilitates the prioritisation of different tasks for the administrator, by implementing a mechanism for the user to 'up-vote' both bug fixes and feature additions. 
Upvoting bug fixes does not cost any money, but the addition of a new feature to the site, which requires a certain number of upvotes to be implemented, requires a small fee to cover labour costs. 
In return, the site administrator will pledge to spend a minimum amount of time working on the most popular voted highest-paid feature addition request. 

## UX
 
This app is targeted towards the open source developer community. It is meant as a means for people to come together in an online community to discuss and share their ideas. As a start-up company project, the intention is to allow the user to have an input into the design of the web app, by allowing the facility for features requests to be voted upon/developed. 
###	User Stories:
-	As an open source developer, I am looking for a place to collaborate and share my ideas in relation to software development. 
-	My aim is to be able to learn from others and develop my skills to become a better developer. 
-	I need to be able to login to an app where I can use a commenting system to discuss features and bugs with other developers. 

### Wireframes: 

Landing Page:
![Landing Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_landing_page.PNG)

Login Page:
![Login Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_login_page.PNG)

Landing Page After Login:
![Landing Page After Login](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_landing_page_after_login.PNG)

Registration Page:
![Registration Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_registration_page.PNG)

Tickets Page:
![Tickets Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_tickets_page.PNG)

Add Bugs Page:
![Add Bugs](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_add_bug_page.PNG)

Add Features Page:
![Add Features](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_add_feature_page.PNG)

Bugs Page:
![Bugs Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_bugs_page.PNG)

Features Page:
![Features Page](https://s3-ap-southeast-2.amazonaws.com/full-stack-frameworks/unicorn-attractor/github/ua_features_page.PNG)

## Features

## Existing Features

### Registration: 

New users are provided with a means to register on the site. Access to any of the sites functionality requires that the user be registered. Registration is handled by the accounts app, it uses the Django AUTH model. Django forms handle the user input and form. 

- Login: Login functionality is handled by the accounts app. This allows a user who has already registered on the site to login and access the sites functionality. A user can login using a combination of either their username and password or email address and password.  
- Index: Once the user has logged in they will be redirected to the index.html page. Here the user will be greeted with a jumbotron containing their own login username and a welcome message. This page contains information about the sites goals and usage, as well as displaying the navbar functionality for the first time. The navbar functionality is available on all pages if the user has successfully logged in. 
- Tickets Functionality: To add a feature request or register a bug on the site, the user can navigate to the user profile page using three different methods; the About icon contained in the navbar, the unicorn icon also contained in the navbar, or by following the instructions contained on the index page. Once the user has successfully navigated to the /tickets/ page, they can select from “Report a Bug” or “Log Feature Request” options. 

### Navbar:

- Bugs: When the user selects the Bugs option on the navbar, they are redirected to the /bugs/ url. Here they will see a list of bugs retrieved from the database that have already been added in the database by any other user. The bug ticket will show its ticket status, number of views, creation date and number of likes or “up-votes”. The user can click on the title of the bug to be transferred to the /bug_detail/ url. Here the user will be free to comment on the issue, and edit the bug specific information: description, title and status. 
- Features: When the user selects the Features option on the navbar, they are redirected to the /features/ url. Here they will see a list of features retrieved from the database that have already been added in the database by any other user. The feature ticket will show its ticket status, number of views, creation date and number of likes or “up-votes”. The user can click on the title of the feature to be transferred to the /feature_detail/ url. Here the user will be free to comment on the issue, and edit the bug specific information: description, title and status. The user will also have the option to “Upvote” the feature request, to signify their interest in having the feature implemented in the web app. Upon clicking the upvote button, the user will be redirected to the /view_cart/ url, where they will be presented with the number of items added to the user’s cart, and the total cost of all items. The user will have the option to “Go To Checkout”. The user can access the /view_cart/ url from the navbar, so long as their cart contains at least one item. 
- Checkout: The /checkout/ url displays a Django payment form allowing the user to pay for items in their cart. The form is implemented using the stripe API integration. On this page, the user will be presented with the number of items being purchased and the total cost. Once payment has been successfully completed, the user will observe a Django messages success message, notifying them that the payment has completed with success. 
- Profile: Users can access a rudimentary profile page from the navbar. Here they will be presented with a means of logging a ticket via the /tickets/ url, as well as confirmation of their user login ID. 
- Stats: Users can access the sites usage data graph using the /stats/ url. Here they will see content pertaining to the number of bugs, features, users and comments contained within the database. This was implemented using Django REST framework and Chart.js. 

### Features Left to Implement

- User Profile: Additionally, I would like to extend the default Django AUTH model to allow users to input extra information upon registration, Bio, Location, Occupation etc. I would also like to include functionality to upload a user profile picture in the same update. 

## Technologies Used

- [Git](https://git-scm.com/) Version control for this app was managed using Git, with a remote public repository hosted on Github: [github](https://github.com/bransfieldjack/fullstack-frameworks-milestone-project-unicorn-attractor/tree/master)
- [Python 3 ](https://www.python.org/download/releases/3.0/) Python was chosen as it is delivered on the course content. It is easy to use, modern and versatile. 
- [Django==1.11 (LTS) ](https://www.djangoproject.com/download/) Django 1.11 long term support was used for the sites framework. This is the version used throughout the tutorials during the course and support for this iteration extends beyond 2018.
- [Django REST framework ](https://www.django-rest-framework.org/) Django REST framework was used to construct the web API for use with the sites stats page. The endpoints can be accessed via JQuery and provide data input for the Chart.js plugin. The browsable API can be accessed via the following link once logged into the site: https://unicorn-attractor-jackalack117.c9users.io/ChartData/.
- [JQuery 3.3.1 ](https://blog.jquery.com/2018/01/20/jquery-3-3-1-fixed-dependencies-in-release-tag/) JQuery 3.3.1 was used for both the styling and to assist with the AJAX calls used on this site. 3.3.1was used as it resolved an issue discovered in the previous release. 
- [Bootstrap 4.1.3 ](https://getbootstrap.com/docs/4.1/getting-started/download/) Bootstrap 4 was used for this sites style templating. Bootstrap 4 is the newest and fastest version of bootstrap. 
- [AWS SDK for Python (Boto) ](https://aws.amazon.com/sdk-for-python/) Boto is a library used to access AWS S3, EC2, and DynamoDB services. I used it in conjunction with an S3 bucket to host the static files required for this site. 
- [AWS S3 ](https://aws.amazon.com/s3/) AWS S3 Bucket storage was used to host static files. This can be accessed programmatically from our app using boto and secretkey environment variables. 
- [Stripe ](https://stripe.com/au) The sites online payment functionality has been implemented using Stripe. The stripe API allows us to process payments on the site which are dealt with by 3rd party banks/financial companies. 
- [Gunicorn 19.9.0 ](http://docs.gunicorn.org/en/stable/news.html) Gunicorn is a python WSGI used for deployment of the application on Heroku. 
- [Psycopg2==2.7.6.1 ](https://pypi.org/project/psycopg2/) Psycopg2 is a Postgresql adaptor/driver used for deployment of the sites database on Heroku.
- [Heroku](https://www.heroku.com/products) Heroku is a managed, container-based cloud (PaaS) platform as a service. Heroku was a clear choice in terms of deployment platform given its integration with modern technologies. 
- [Balsamiq](https://balsamiq.com/) Wireframing was completed using Balsamiq. This was helpful during the UX design process. 
- [icons8](https://icons8.com/) Iconography for this site was obtained from icons8. 

* All of the code written in this project is my own, with the exception of the stripe.js file for interacting with the stripe API and the Chart.js code in the Django-Charts app for interacting with the Django REST framework end points.

## Testing

This project was created using a TDD approach where possible. This site is built with the understanding that it will accommodate a large online community of users, who wish to interact and collaborate on issues and feature requests. 
As such, integral to the TDD process for this app was to ensure that both form submission and validation were working without issue. Additionally, testing for model functionality was also a requirement.
Automated testing was carried out using Travis CI, and unit testing was carried out on "target areas" such as form validation, model tests and form submission. Undocumented in this manual are trivial tests, such as checking to see that a function is "on" etc. 
Travis integration has since been removed from the repository. The production environment is using a POSTGRESQL database, all CI testing was running on the local SQLITE database. As such, Travis CI was failing. I have not yet discovered a fix, env variables have been configured on Travis but it is still failing on database testing. 

![Accounts User Login Form](https://s3-ap-southeast-2.amazonaws.com/fullstack-frameworks-milestone-project-unicorn-attractor/screenshots/accounts_test_user_login_form.PNG)

```
from django.test import TestCase
from .forms import UserLoginForm, UserProfileForm


class TestUserLoginForm(TestCase):
    
    def test_UserLoginForm(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        
    def test_UserLoginForm_validation(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
```

![Accounts test_views.py](https://s3-ap-southeast-2.amazonaws.com/fullstack-frameworks-milestone-project-unicorn-attractor/screenshots/accounts_tests_views.PNG)

```
from django.test import TestCase


class TestViews(TestCase):
    
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        
    def test_get_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")
        
    def test_get_user_profile_page(self):
        page = self.client.get("/tickets/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tickets.html")
```

![Tickets models_test.py](https://s3-ap-southeast-2.amazonaws.com/fullstack-frameworks-milestone-project-unicorn-attractor/screenshots/model_tests.PNG)

```
from django.test import TestCase    
from .models import Features, Comments


class TestFeatureModel(TestCase):
    
    def test_status_default_assigned(self):
        feature = Features(title="Test Feature 1")
        feature.save()
        self.assertEqual(feature.title, "Test Feature 1")
        self.assertEqual(feature.status, "assigned")
        
    def test_can_create_a_feature(self):
        feature = Features(name="Create a test", done=True)
        feature.save()
        self.assertEqual(feature.name, "Create a test")
        self.assertTrue(feature.done)
```

![Charts Test](https://s3-ap-southeast-2.amazonaws.com/fullstack-frameworks-milestone-project-unicorn-attractor/screenshots/charts_test.PNG)

```
def get_data(request, *args, **kwargs):
    
    """
    A test function to research returning API data from REST using python logic instead of AJAX. 
    """
    
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response
```

![Charts API Test](https://s3-ap-southeast-2.amazonaws.com/fullstack-frameworks-milestone-project-unicorn-attractor/screenshots/chart_api_test.PNG)

```
class ChartData(APIView):
    
    """
    Returns data from the API endpoint. Passes values into variables to be used in template via AJAX. 
    """
    
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format=None):
        
        users = Users.objects.all().count()
        comments = Comments.objects.all().count()
        features = Features.objects.all().count()
        bugs = Bugs.objects.all().count()
        
        labels = ["Users", "Comments", "Features", "Bugs"]
        default_items = [users, comments, features, bugs]
        
        data = {
                "labels": labels,
                "default_items": default_items,
            }
        return Response(data)
```

## Manual Testing

### Linking/pages:

Checked all outgoing (page to page) and internal links.
Confirmed that no orphan pages exist as part of this project. (Un-used pages left over from the development process)

### Form Testing:

Tested form submission links and form validation - no issues.

### Cookies Testing:

Disabled cookies and confirmed that the site behaves as per normal.
No observable effect on application security after disabling cookies during or outside of a session.

### HTML Validation:

Validated all HTML code using: https://validator.w3.org/ (Fixed minor errors/warnings)

### Database Testing:

Verified that test data was writing to the database. 
Verified the ability to retrieve data from the same database.

### Ease of Learning:

Everything the user needs in terms of information is clearly displayed. Clickable links are made obvious when appropriate, and large icons are used for clarity.

### Navigation:

The site is relatively easy to navigate. 
The user cannot progress throughout the site without entering a username. 

### Compatibility:

Cross browser compatibility testing has been conducted using Chrome, Firefox, Edge and Opera.
Mobile compatibility testing has been undertaken to ensure that the site works well on mobile devices. 

## Deployment

- This site was developed with Cloud 9 IDE primarily, and VS Code for editing when required (offline). 
- A delivery and CI pipeline was implemented using the remote Github repository, Travis CI, Heroku staging and Heroku production.
- Automated testing and release to staging has been setup, and the staging environment has been configured using the same environment variables as production (heroku config vars). 
- The development environment contains environment variables which are not shared on the publicly accessible repository, for obvious security reasons. 

### From the Heroku Dashboard:

* Login to your heroku account.
* From the dashboard, select: New > Create New App.
* Select an appropriate App Name as per the on-screen instructions, and the most relevant hosting region. 
* Select Create App.

### From the bash command line/local repo:

* Logon to your heroku account using the 'heroku login' command. 
* Initialise your repo, if you havent already done so.
* Connect the Heroku App repo using the 'heroku git:remote -a (app name)' command.
* In order for Heroku to build your app, you will need to specify the requirements using the following command: 'sudo pip3 freeze --local > requirements.txt'.
* As per the development process, remove all packages/dependencies installed as a result of experimentation which may prohibit successful build on the heroku container. 
* You will also need to generate a "Procfile" before pushing your code. This acts as the entry point for your application. To generate this file, use the 'echo web: python app.py > Procfile' command from bash.
* Use git add . to save your work.
* Add your first commit (git commit -m "Initial Commit. "), then use 'git push heroku master' to push your code to Heroku. 
* To complete the process and ensure that your app will run, set the appropriate config variables from the heroku settings tab. 
* Create Heroku add-ons (PostgreSQL).
* Run heroku config:set DEBUG_COLLECTSTATIC=1, this allows for integration of our static files being hosted on S3 with boto. 
* Create an 'IP' config var, with a corresponding value of: 0.0.0.0.
* Create a 'PORT' config var, with a corresponding value of: 5000.
* Create a config var for storage of the S3 secret access key credentials. 
* Create a config var containing your DATABASE_URL credentials for use with Postgresql.
* Make sure all other relevant environment variables (see env.py) are configured, as required. 
* To access the application, click open on the heroku console (top right) and record the apps URL. 

## Credits

- [Pretty Printed, Django REST](https://www.youtube.com/watch?v=263xt_4mBNc)
- [Coding Entrepreneurs, Django and Chart.js](https://www.youtube.com/watch?v=B4Vmm3yZPgc)

### Content
- All text content on the site is my own.

### Media
- The icons used in this site were obtained from [icons8](https://icons8.com/)

### Acknowledgements

- Django REST framework tutorial: ![Pretty Printed] https://www.youtube.com/watch?v=263xt_4mBNc
- Django REST framework with Chart.js tutorial: ![Coding Entrepreneurs] https://www.youtube.com/watch?v=B4Vmm3yZPgc
- Chart.js: https://www.chartjs.org/
