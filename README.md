# Booking Website

## Introduction

This project was created using Django. It is meant to emulate a restaurant website for customers to book a table.

It has been deployed on Heroku, the repository uses Code Institute's template.

The general premise/concept for the imaginary business, that this website is made for, is that a different movie/meal combination will be
available each day of the week and you will be able to book a reservation for one of the available tables.

[Link to Site](https://pp4-bookingwebsite-2-626d2704898f.herokuapp.com)

Below I will outline key aspects of the project and its creation.

## Table of Contents

1. [UX](#ux)
    - Website Visuals
        - Color
        - Font
        - Website Name
        - Imagery
    - Epics
    - User Stories
    - Wireframes
2. [Features](#features)
    - Home
    - Account Registration
    - User Profile
    - Admin Screen
3. [Technologies Used](#technologies-used)
    - Python
    - Django
    - Heroku
    - HTML
    - Packages
4. [Testing](#testing-1)
    - Manual Testing
5. [Deployment](#deployment)
   - Setting Up Repository
   - Deploying on Heroku
   - Clone Repository
   - Fork Repository
6. [Credits](#credits)
    - Code Institute
    - Other

## UX

### Website Visuals

Below will outline various design choices related to how the website visually looks.

#### Color

#### Font

#### Website Name

During development I have been quite uncertain on the specific final name for the website.
It will either go by 'Classics and Cuisine' or 'Candid Cinema'.

During the development the temporary name of just 'Booking Website'.

The final website name would focus on either the restaurant or cinema aspect of the business.

#### Imagery

### Epics

8 Epics were created for this project, these were expanded into user stories.

Epics:

1. As a developer, I want to set up development and deploy the
 project correctly, so that the development of the project runs
 smoothly without issues.
2. As a website owner, I want the website to function properly
 and appear inviting to users.
3. As a website owner, I want the website to display the
 available showings in a uniform manner.
4. As a website owner, I want to be able to edit details of
 movies or meals, if any changes take place.
5. As a website user, I want to register an account.
6. As a website user, I want to login and view details.
7. As a website user, I want to be able to make a booking and
 receive confirmation.
8. As a website owner, I want to create and display upcoming
 news related to the restaurants upcoming new movies or dishes.

### User Stories

User Stories were created based on the above Epics:

1. 
    - A. As a developer, I would like to set up a github
    repository, so that I will have somewhere to maintain and update
    the project files.

    - B. As a developer, I would like to set up my IDE along with
    a virtual environment, so that I will be able to begin coding
    the project.

    - C. As a developer, I would like to set up the django
    project along with required packages, so that I will have all
    the required tools to start developing.

    - D. As a developer, I would like to create the initial home
    screen view and layout, so that the project will be ready for
    early deployment.

    - E. As a developer, I would like to deploy the project to
    Heroku early, so that I can see if there are any issues early
    on.
2. 
    -  A. As a website user, I would like a clear website layout that
    adjusts based on screen size, so that the website is easy
    to navigate regardless of which device I am using.

    - B. As a website user, I would like inviting website colours
    and a readable font, so that the website is enjoyable to
    use and easy on the eyes.

    - C. As a developer, I would like automated code testing, so
    that many user input cases can be tested on a larger scale
    to reduce potential bugs.

    - D. As a developer, I would like manual code testing, so that
    user navigation can be tested to reduce potential bugs.
3. 
    - A. As a website owner, I would like navigation for different
    showings based on the day of the week selected by users.

    - B. As a website owner, I would like the ability to click into a specific
    showing, so users can see additional details.

    - C. As a website owner, I would like the ability to mark specific
    showings as 'unavailable' if they become fully booked.
4. 
    -  A. As a developer, I would like to create a custom admin
    screen/UI, so that the website owner will have easier
    access to certain functionality on the website.

    - B. As a website owner, I would like to create new
    listings in the admin screen, so that I can easily add showings
    to the website listings.

    - C. As a website owner, I would like to view current showings
    in the admin screen, so that I can easily check
    the status of current showings.

    - D. As a website owner, I would like to edit a current showing’s
    details in the admin screen, so that I can easily
    amend/update specific details when needed.

    - E. As a website owner, I would like to remove/delete 
    specific showings if needed.
5. 
    - A. As a website user, I would like a navigation button to
    register on the home screen, so that I can quickly navigate
    to the desired screen.

    - B. As a developer, I would like a prompt to sign in/register
    when users try accessing some sections that require an
    account, so that they can’t get to specific screens that
    require an account.

    - C. As a website owner, I would like a form to register an
    account, so that all the necessary information is gained
    from the user.

    - D. As a developer, I would like form validation for user
    registration, so that I can make sure invalid information
    isn’t submitted for user details.

    - E. As a website user, I would like confirmation for account
    registration form completion, so that I am confident my
    details have been accepted successfully.
6. 
    -  A. As a website user, I would like the option to login from
    the home screen, so that I can quickly navigate to the
    desired screen.

    - B. As a website user, I would like a prompt to sign in when
    required, so that I only sign in when needed.

    - C. As a website user, I would like an account details screen,
    so that I can check what details are currently associated
    with my account.
    
    - D. As a website user, I would like to be able to update my
    details from the account screen, so that I can amend any
    details that may be incorrect.

    - E.As a website user, I would like to be able to delete
    specific details from the account screen, so that I can remove
    details I don’t want attached to the account.
7. 
    -  A. As a website developer, I would like showings to have the function/ability to be clicked,
    so that website users will be able to access further details and proceed to booking.

    - B. As a website user, I would like a customs screen to show the further details about a 
    specific showing, so that I can see if I want to book a reservation.

    - C. As a website user, I would like be able to proceed with a booking from the custom screen,
    so that I can lock in a spot from the specific showing.

8. 
    - A. As a website owner, I would like a section to display
    upcoming restaurant news, so that I have a spot on the home
    screen to inform users of important information such as
    new movies or meals.

    - B. As a website owner, I would like the ability to create new
    posts from an admin/staff screen, so that it will be easy
    for myself or a staff member to add news when needed.

    - C. As a website owner, I would like the ability to edit
    previous posts, so that I can amend incorrect news quickly
    without hassle.

    - D. As a website owner, I would like the ability to remove/hide
    previous posts, so that I can stop users from seeing news
    that no longer applies.

### Wireframes

A wireframe was created to layout the home screen for the website on computer and mobile screens.

Wireframe 1 shows a general mockup of the home screen. Different movies options are shown, with mobile view on the side.

[Wireframe 1](/docs-media/pp4-wireframe1.png)

Wireframe 2 shows a mockup for what the further details of a showing would look like, with additional screens for forms.

[Wireframe 2](/docs-media/pp4-wireframe2.png)

## Features

Based on the User Stories certain features of the website are created and implemented.

### Home

The home page is where the user will first arrive. Here they will have navigation to all aspects of the website.

[Home Screenshot](/docs-media/PP4-home.png)

Each movie available will be listed. Users will see important details about the movie. They can click on the title to be brought to further details and the ability to make a booking.

### Movie Details

The movie details screen provides the added description of the movie and the ability to make a booking.

[Movie Details Screenshot](/docs-media/PP4-movie.png)
[Booking Screenshot](/docs-media/PP4-booking.png)

There is the option to pick which day for the booking. Users bookings will appear on the profile section.

### Navbar

The navigation bar appears at the top left of the screen for users, beside the website title.

[Navbar logged in Screenshot](/docs-media/PP4-navbar-in.png)

Above is how the navigation bar looks if the user is signed in. They will have the option for 'Profile' and to 'Logout'.

[Navbar logged out Screenshot](/docs-media/PP4-navbar-out.png)

Above is how the navigation bar looks if the user is sign out. As you can see the previous options are gone.
They will now have the options to 'Signup' or 'Login'.

### Account Registration

There are various screens based on which option the user is picking.

[User Signup Screenshot](/docs-media/PP4-signup.png)

Here the user is creating an account and must fill in the required details.

[User Signin Screenshot](/docs-media/PP4-signin.png)

After signing up they will have the ability to sign in.

[User Signout Screenshot](/docs-media/PP4-signout.png)

If the user is signed in they will have the ability to sign out.

### User Profile

The User Profile screen allows users to see their details and bookings.

[Profile Screenshot](/docs-media/PP4-profile.png)

The user's bookings will be listed in order of creation. It will show which day they are booked for and the associated movie.
You can see and edit button, this unfortunately is unfunctional but the intended purpose was to allow users to update/delete their bookings.

### Admin Screen

The admin screen is unfortunately non-existent. The intention would be an additional screen for authorised users such as owner or staff.
Here they would see all bookings and add/change/remove movie listings when needed.

## Technologies Used

### Python

The following python packages were previously used:

- asgiref==3.8.1
- dj-database-url==0.5.0
- Django==5.1.4
- django-allauth==65.2.0
- gunicorn==23.0.0
- packaging==24.2
- psycopg2==2.9.10
- pytz==2024.2
- setuptools==75.6.0
- sqlparse==0.5.2
- tzdata==2024.2

The following python packages were changed to:

- asgiref==3.8.1
- bleach==6.2.0
- certifi==2025.1.31
- cffi==1.17.1
- charset-normalizer==3.4.1
- crispy-bootstrap5==0.7
- cryptography==44.0.2
- defusedxml==0.7.1
- dj-database-url==0.5.0
- Django==4.2.19
- django-allauth==0.57.2
- django-crispy-forms==2.3
- django-summernote==0.8.20.0
- gunicorn==23.0.0
- idna==3.10
- oauthlib==3.2.2
- packaging==24.2
- psycopg2==2.9.10
- pycparser==2.22
- PyJWT==2.10.1
- python3-openid==3.2.0
- pytz==2024.2
- requests==2.32.3
- requests-oauthlib==2.0.0
- sqlparse==0.5.2
- typing_extensions==4.12.2
- tzdata==2024.2
- urllib3==2.3.0
- webencodings==0.5.1
- whitenoise==6.5.0

### Django

- Django was used as the main framework for this project.

### Heroku

- Heroku was used to deploy this website online. [Heroku](https://www.heroku.com)

### HTML

- Html was used as the base language for the site templates.

### CSS

- CSS was used to style the pages for this website.

### JavaScript

- JS was used for any functionality for the website.

### Packages

- VS Code was used to develop the code for this site.
- GitHub was used for version control. [Github](https://github.com)
- Balsamiq was used to create wireframes.

## Testing

Below will have an outline of the types of testing done to identify any bugs within the website.

### Manual Testing

## Deployment

Code Insitute template was used for creation of repository of this site. [Template](https://github.com/Code-Institute-Org/ci-full-template)

### Setting Up Repository

I took these steps to setup my Github repository:
- Open the link to the Code Institute template mentioned above.
- At the top right corner click the button 'Use this template'.
- Click first option 'Create a new repository.
- Give the repository a relevant name and description.
- Make sure the repository remains public.
- At the bottom right click 'Create repository'.

### Clone Repository

Here I will outline the steps to clone a repository on GitHub.
This allows you to save a local copy.

Steps:
- Navigate to the GitHub page for the desired repository.
- Click on 'Code'
- Copy the link provided under HTTPS.
- Open Git Bash.
- Change the current working directory to the location where you want the cloned directory.
- Type 'git clone ' along with the copied link.
- Press Enter to create cloned repository.

Steps are based on GitHub documentation related to cloning repositories.

[GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=webui)

### Fork Repository

Here I will outline the steps to fork a repository on GitHub.
This allows you to have your own repository to make changes to based on an original repositories code/settings.
Additionally you may submit a pull request to the original repository owner.

Steps:
- Navigate to the GitHub page for the desired repository. 
- At the top right, below the search box, click 'Fork'.
- Leaving all the settings will be fine, but here you may apply a new name or description.
- Click 'Create fork'.

Steps are based on GitHub documentation related to forking repositories.

[GitHub Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

### Deploying to Heroku

Here I will outline the steps I took to deploy the project on Heroku. 
It is necessary to have the project hosted somewhere so the website can be accessed by users/testers without needing to download the project and hosting locally.
I deployed to Heroku early on in development so that testing how the website would look outside of local development environment.

Steps:
- Log into Heroku website, go to dashboard
- Click on 'Create new app'
- Give the app a unique name (this is required), select whatever is the closest region
- Click on 'create app'
- Click on the 'settings' tab
- Add 'DISABLE_COLLECTSTATIC' key with the value of '1' (This is required for deploying to Heroku early in development but gets removed at a later point)
- In a terminal on your IDE use the command 'pip(3) install gunicorn' (Version 23.0.0 is being used for this project which can be found in the requirments.txt file)
- In the terminal use the command 'pip(3) freeze > requirements.txt', this will add all the requirements needed based on packages installed on your current virtual environment
- Create a file in the main directory named 'Procfile' (notice no file extention). This file is required for Heroku deployment
- Inside of the Procfile put this one line 'web: gunicorn booking_website_2.wsgi:application'
- Make sure to add '.herokuapp.com' to the 'ALLLOW_HOSTS' list
- Make sure 'DEBUG' is set to 'False' outside local development to avoid exposing any important information
- At this stage commit and push to your Github repository
- Click on the 'deploy' tab (it should be along the same row as settings from a previous step)
- Scroll down till you find a mention of Github
- Sign into your Github if you aren't already
- Type/Paste in the name of your Github repository, which the option pops up, click the correct repository
- Manual deploy the main branch to Heroku
- There will be an option to enable automatic deployments, this will have Heroku redeploy your app each time you push a new commit to your main branch
- At this stage you can click 'Open app' to see if it deployed correctly

These are the general steps I took when deploying my project to Heroku.
Some steps may vary based on user and time of recreating the steps.
As mentioned in one of the steps, as I deployed to Heroku early in development the Heroku app was set not to collect static files. This would need to be changed once static files are setup correctly in the project files.

## Credits

### Code Institute

- Code Institute template used for repository [Template](https://github.com/Code-Institute-Org/ci-full-template)

- Code Institute learning modules used to learn different aspects used to work on this project [Code Institute](https://codeinstitute.net/ie/)

### Other

- An article on GitHub was used to help with creating this README doc [Article](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)