<div align="center">
    <img src="GET LOGO IMG" href="GET HEROKU LINK" target="_blank" rel="noopener" alt="Pawer Logo" aria-label="Pawer Logo" />
    <a href="GET HEROKU LINK" target="_blank">Pawer - Dog adoption, services and stores.</a>
</div>

## Introduction

<div align="center">
    <img src="GET IMAGE WITH DIFFERENT DEVICES? OR SCREENSHOT" href="GET HEROKU LINK" target="_blank" rel="noopener" alt="Image of how home page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>
<br>

[Pawer](https://romqrq.github.io/pawer/) is an application that has the proposal to be a platform where users can adopt dogs and business/services can engage new customers.
Users can register and interact with other users information or leaving them feedback on their interaction.
The website has a clean visual while bringing an inviting and friendly feel with an intuitive experience for the user.

As possibilities for monetization for this platform we have implemented discount codes and affiliate links.
Other options such as premium accounts and business/service accounts are also realistic possibilities that can be implemented in the future.

## Table of Contents

1. [UX](#ux)

   - [Goals](#goals)
     - [Customer Goals](#customer-goals)
     - [Service Provider Goals](#service-provider-goals)
     - [Store Goals](#store-goals)
     - [Pawer Goals](#pawer-goals)
   - [User Stories](#user-stories)
     - [Customer Stories](#customer-stories)
     - [Services Stories](#services-stories)
     - [Stores Stories](#stores-stories)
     - [Staff Stories](#staff-stories)
   - [Design Choices](#design-choices)
   - [Wireframes](#wireframes)
   - [Flowchart](#flowchart)
   - [PDF](#pdf)

2. [Features](#features)

   - [Existing Features](#existing-features)
     - [Elements on every Page](#elements-on-every-page)
     - [Home Page](#home-page)
     - [Activities Page](#activities-page)
     - [Listing Page](#listing-page)
     - [Create Account Page](#create-account-page)
     - [Log In Page](#log-in-page)
     - [Account Settings Page](#account-settings-page)
     - [Account Page](#account-page)
     - [Add new Listing Page](#add-new-listing-page)
     - [Preview Listing Page](#preview-listing-page)
     - [Edit Listing Page](#edit-listing-page)
     - [Contact Page](#contact-page)
     - [404 Page](#404-page)
     - [Permission Denied Page](#permission-denied-page)
   - [Features Left to Implement](#features-left-to-implement)

3. [Information Architecture](#information-architecture)

   - [Database choice](#database-choice)
   - [Data Storage Types](#data-storage-types)
   - [Collections Data Structure](#collections-data-structure)
     - [Users Collection](#users-collection)
     - [Activities Collection](#activities-collection)

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6. [Deployment](#deployment)

   - [Heroku Deployment](#heroku-deployment)
   - [How to run this project locally](#how-to-run-this-project-locally)

7. [Credits](#credits)

   - [Content](#content)
   - [Media](#media)
   - [Code](#code)
   - [Acknowledgements](#acknowledgements)

8. [Contact](#contact)

9. [Disclaimer](#disclaimer)

---

# UX

## Goals

### Customer Goals

The central target audience for us are the potential adoptants and people that already have pets and are looking for products or services.

Customer goals are:

- Finding a dog to adopt.
- Finding products or services to buy.
- Finding stores or services nearby.
- Minimum effort to reach goal.
- Intuitive navigation.

Pawer helps the customer meeting these goals because:

- The application was developed around those customers' goals from the planning stages of the construction.
- All the navigation is done from the navigation bar menu so the user won't be looking for it.
- Buttons exibit text and icons that together make the navigation more intuitive.
- Forms where users can interact have explicit field placeholders to guide the user
- Forms that aren't activated by the user are hidden dynamically to avoid cluttering the page.
- Options and features that aren't relevant for customers are omitted according to their account type.

### Service Goals

The pet service sector is getting more diverse by the day.
Our target for services providers are both companies and self employed individuals.

- Exposing their service to a mass of potential new customers.
- Reasonable possibility of return over investment (when services account system is implemented)
- A reliable and reputable platform to advertise and aggregate value to the service.
- Balanced competition for space between companies and individuals providing the same service.

Pawer helps the service providers meeting these goals because:

- Users have access to free accounts that gives them access to a pool of services to choose from.
- Exists the possibility to offer discount codes for services to influence the user decision into hiring the service.
- With affiliate links, it's possible to increase online traffic to the service website.
- Information is prioritized and organized in a way that users can find what is bein offered in a glance.
- With the feedback system, great service providers will stand out and set themselves apart, attracting more customers.
- The standardised layout allows similar exposure for all service providers, creating a plain field for competition.

### Store Goals

With more businness being done virtually, we are aiming for stores are looking to conquer this new territory and virtual stores that depend completely on their virtual presence.

- Showcasing their products to a mass of potential new customers.
- Increase physical customer presence at stores (for business with physical stores)
- Reasonable possibility of return over investment (when stores account system is implemented)
- A reliable and reputable platform to advertise and aggregate value to their products.
- Balanced competition for space between different sizes of business.

Pawer helps the stores meeting these goals because:

- Users have access to free accounts that gives them access to a pool of stores to choose from.
- Exists the possibility to offer discount codes for products to influence the user decision into buying the product.
- With affiliate links, it's possible to increase online traffic to the store website.
- Information is prioritized and organized in a way that users can find what is bein offered in a glance.
- With the feedback system, great stores will stand out and set themselves apart, attracting more customers.
- The standardised layout allows similar exposure for all stores, creating a plain field for competition.

### Pawer Goals

The primary goal of Pawer is to create, around the dog adoption process, a meeting point for customers and business/services to meet and improve the adoption experience.
This structure has the objective of making easier for the adoptant to get it right from the first time and reducing the chances of dogs being abandoned again.

Pawer has four main target audiences: potential dog adoptants, people that already have pets, dog-related service providers and stores.

We are considering the following as potential sources of income are:

- Premium accounts for customers:
  - Discount codes for partner services or stores.
  - Personalized content from partner services or stores
- Affiliate links
- Services and stores accounts:
  - Specific paid accounts for businesses to be showcased on the platform.
- Responsible user data sharing with partners.

## User Stories

### Customer Stories

As a customer I want:

1. The ability to easily navigate through the application with controls that are intuitive and easy to find.
2. Visual feedback for my interactions with the content, so that I know if I have clicked or not clicked something.
3. To be presented concise and objective information displayed in a way that it makes it easier to find what I'm looking for.
4. Be able to register to the website and avail from the discounts on products and services.
5. Be able to update my register information.
6. Find a dog to adopt.
7. Find a service.
8. Find a store.
9. Leave feedback for a service provider.
10. Leave feedback for a store.

### Service Stories

As a service provider I want:

1. To know that my customer can find my information easily
2. The ability to easily navigate through the application with controls that are intuitive and easy to find.
3. Visual feedback for my interactions with the content, so that I know if I have clicked or not clicked something.
4. Be able to register to the website and expose my service to potential customers.
5. Showcase my service on a platform that aggregates value to the service.
6. Be able to update my register information.

### Stores Stories

As a store advertising on Pawer I want:

1. To know that my customer can find my information easily
2. The ability to easily navigate through the application with controls that are intuitive and easy to find.
3. Visual feedback for my interactions with the content, so that I know if I have clicked or not clicked something.
4. Be able to register to the website and expose my store and products to potential customers.
5. Showcase my service on a platform that aggregates value to the service.
6. Be able to update my register information.

## Design Choices

The application is aimed to provide users with a clean, consistent and easy-to-use interface with an engaging and intuitive design. The website was built around the idea that the user will be able to use the website with a minimal learning span and trying to make it achievable upon the first contact.

### Fonts

- The header font `Alfa Slab One` was chosen because it has a professional look and strong character while still highly readable. It is aimed to catch the eye when the user is "sweeping" the screen looking for information.

- The secondary font `Lexend Tera` was chosen to counter balance the header, adding a slim look with more spaced letters. It introduces a more informal visual while still favoring the readability.

- The tertiary font `Roboto` was chosen for the general text, offering a mid-term to the two previous fonts and keeping the page ballanced. It is a font with high readability and keeps a clean and professional look.

### Icons

- All icons used were chosen from materialize library. They are all icons that have strongly established meaning and are widely used accross the internet making them easy to be understood by the users.

- Social media icons for facebook, instagram, twitter and youtube are used on the footer of the website. These links are targeting the main page of their respective social media network

### Colours

- The colours chosen to the logo were a mustard-yellow (#FCD23C), black (#343334) and red(#D8414B). The red and yellow colours have an attention-grabbing propriety as human brain is hardwired to pay attention to these colours for primitive survival reasons. The black colour brings contrast, balance and readability to the logo.

- The buttons are on a green colour (#26a69a) which is used only for buttons, the contrast with the main colour scheme makes it grab attention. This way the user has a more consistent and predictable experience.

- The colours were saved as variables on scss file and are recalled from these variables accross the styling files to make sure the colours are consistent across the entire project.

### Styling

- The materialize **parallax** class was used to give users a distinct scrolling experience while framing content, helping user to localize the information.

- **Cards** and **buttons** have slightly rounded corners for a more smooth visual and a slight shading for improved perspective perception by the user, helping them to recognize interactive elements on the page.

- Each database entry is displayed on a separate card, making clear to the user the individuality of each entry.

- Repetition of patterns accross the whole application provides consistency and helps the user getting familiarized to the application on first time use.

- Hover effect along with color change for active elements have been added to give users visual feedback.

**Backgrounds**

- The elements with the parallax class display pictures that help setting the theme and the feel for each specific section or page.

- Content areas have plain white background to keep it neutral and not to compete for attention with content and pictures.

**Card images**

- Due to technical limitations at this poit, the databae entries can't contain images. Pertinent Materialize icons were used as a placeholder until future update.

**Forms**

- Materialize forms were used for this project. Placeholders were used to auxiliate the user while identifying each field.

- Forms can take up valuable space on the screen so, for this project, we used jQuery to hide or show forms based on user actions and only one form will be visible at a time.

- When a form is activated, jQuery code will automatically scroll it into view.

**Navigation bar**

- Navigation bar is fixed at the top of the screen. This way the user has the controls always visible and within immediate reach.

- Action buttons/links were kept to the sides for ease of reach on mobile devices.

- Buttons are shown or hidden dynamically on the following situations:

  - user is not logged in or not registered
  - user is logged in but doesn't have staff privileges
  - user is logged in and has staff privileges

- Menu is collapsed to a button when on small resolution screen and expanded when from medium resolution and up.

## Wireframes

These wireframes were created using [Mockflow](https://mockflow.com/) during the Scope Plane part of the design and planning process for this project.

<!-- - [Home](https://ibb.co/52Z3P4r)
- [Search](https://ibb.co/Wcgbtqs)
- [Activity search](https://ibb.co/Nm8FYbd)
- [Activity listing](https://ibb.co/PMb9jCm)
- [Event search](https://ibb.co/MR8BFC3)
- [Event listing](https://ibb.co/njnP5C5)
- [Create or Edit account](https://ibb.co/1TyV9sN)
- [Log in](https://ibb.co/yhbBSV0)
- [My account](https://ibb.co/nr2s9cw)
- [Create or Edit Activity page](https://ibb.co/Wv349RB)
- [Create or Edit Event page](https://ibb.co/sqj60xb) -->

### Flowchart

During the planning stages, we created some flowcharts:

- [Pawer - Website hierarchy and structure](GET LINK)

This flowchart illustrates the structure of the website, areas users with different privileges can access and actions they can take.

- [Pawer - Database structure](GET LINK)

This flowchart represents the structure of the database and how files are used to generate new documents combining information from existing files and new input from user.

On the flowcharts the feedback functionality isn't displayed as it wasn't considered to be feasible under the timeframe set for this project. The feature was added after a reassessment of the progress and the positive impact that the feature could bring to the website.

We used [visme.co](https://www.my.visme.co) to make the digital version of the flow charts.

### Conceptual plan (PDF)

- [Pawer - Inception](GET LINK)

This document was created during the planning phase of this project as a way to put the ideas in perspective for further consideration. The final website has some slight differences from what was planned. We have included this document in the project to provide insight into the original planning and direction of the site during the planning stages.

# Features

## Existing Features

### Elements common to all pages

- Navigation bar
  - The navigation bar is fixed at the top of the screen, always visible and is responsive to screen size.
  - On the left side the menu offers all the navigation options for the user to go from one page to another.
  - On small resolution screens, the menu also contains the Register, Dashboard, Login and Logout buttons, depending on user status (not logged in, logged in non-staff and staff).
  - At the center, the Pawer logo is linked to the index page and it holds an attention grabbing place while leving the more accessible to touch edges for the menu and buttons.
  - For medium screens and up, the Register, Login and Logout buttons are on the right side and they are shown/hidden dynamically according to user's account status.

**_User not logged in_**

<div align="center">
    <img class="col-6" src="static/images/wf-images/navbar-mobile-expanded-menu-logged-out.png" alt="Screenshot: Collapsible menu logged out"><br>
    <img class="col-6" src="static/images/wf-images/navbar-logged-out.png" alt="Screenshot: Navbar logged out" >
</div>

**_Non staff user logged in_**

<div align="center">
    <img class="col-6" src="static/images/wf-images/navbar-mobile-expanded-menu-ns-user.png" alt="Screenshot: Collapsible menu non staff user"><br>
    <img class="col-6" src="static/images/wf-images/navbar-ns-user.png" alt="Screenshot: Navbarnon staff user" >
</div>

**_Staff user logged in_**

<div align="center">
    <img class="col-6" src="static/images/wf-images/navbar-mobile-expanded-menu-staff-user.png" alt="Screenshot: Collapsible menu staff user"><br>
    <img class="col-6" src="static/images/wf-images/navbar-staff-user.png" alt="Screenshot: Navbar staff user" >
</div>

- Footer

  - On the left, is displayed a short text about the purpose and mission of the website
  - On the right, a list of the social media links. Currently the links are pointing to the respective home page for that social media platforms.
  - Copyright information.

### Home Page

- Despite the website being fully responsive, there was no need for a different structure on the home page for different devices. The structure is as per image below.

<div align="center">
    <img src="static/images/wf-images/landing-page.png" alt="Screenshot: Landing page" >
</div>

### Adoption Page

- On this page the user can find a list of the dogs on the database.
- Each dog is displayed on a card that contains:
  - Name
  - Breed
  - A short description of the dog
  - Action button(s).
- For non-staff users, the only button available will be "Adopt". This button activates a form that contains a text area for a brief reasoning for the adoption and a submit button.
- The adopt button will be visible but won't activate the form if the user isn't logged in.

<div align="center">
    <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
</div>

- For staff users, the edit and delete buttons will be available and the entry can be edited from there through the dynamic forms activated by the clicked button.

<div align="center">
    <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
</div>

### Services Page

- This page displays the services registered on the database.
- Each service is displayed on a card that contains:
  - First and last name of the service provider
  - Email
  - Type of service
  - Affiliate links
  - Discount code
  - Amount of discount when using the discount code
  - Address
  - A short text describing the service
  - Positive and negative feedback
  - Action button(s).
- For non-staff users, the only button available will be "Feedback". This button activates a form that contains a radio button element where users can leave a positive or negative feedback and the submit button.
- The Feedback button will be visible but won't activate the form if the user isn't logged in.

<div align="center">
    <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
</div>

- For staff users, the edit and delete buttons will be available and the entry can be edited from there through the dynamic forms activated by the clicked button.

<div align="center">
    <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
</div>

### Stores Page

- This page displays the stores registered on the database.
- Each store is displayed on a card that contains:
  - Store name
  - Email
  - Affiliate links
  - Discount code
  - Amount of discount when using the discount code
  - Address
  - A short text describing the store
  - Positive and negative feedback
  - Action button(s).
- For non-staff users, the only button available will be "Feedback". This button activates a form that contains a radio button element where users can leave a positive or negative feedback and the submit button.
- The Feedback button will be visible but won't activate the form if the user isn't logged in.

<div align="center">
    <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
</div>

- For staff users, the edit and delete buttons will be available and the entry can be edited from there through the dynamic forms activated by the clicked button.

<div align="center">
    <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
</div>

### Register Page

- This page allows users to create records in the database.
- Staff members are allowed to create 4 types of user acounts:
  - Dogs
  - Users
  - Services
  - Stores
- Other users won't visualize the "Dogs" option.
- On click, each button will activate a different form containing specific information necessary for each entry type:

  - Dogs:
    - Name
    - Breed
    - Short description
  - Users:
    - First name
    - Last name
    - Email
    - Password
    - Client/Staff switch (Visible only for staff users)
    - Bio
  - Services:
    - Service provider first name
    - Service provider last name
    - Email
    - Password
    - Type of service
    - Website
    - Discount code
    - Discount amount
    - Service description
  - Stores:
    - Address
    - Email
    - Website
    - Password
    - Discount code
    - Discount amount
    - Store description

- The submit button is placed just below the fields and the button style follows the standard set for this application.
- The input `type` attributes are set to `text`, `email`, `url` and `number` where appropriate.
- Fields are marked as `requested` except "discount code", "discount amount", and "website".
- The information submitted by the user is submitted through the form and translated to a dictionary before being added as a new document in the database.

### Login Page

- Page where users can input their email address and password to log in.
- A form is centered on the page with two fields: email and password.
- The fields have placeholders that help the user knowing what information we are asking.
- The login button is placed just below the fields and follows the style for buttons throughout the application.

<!-- - The submit button is placed just below the fields and follows the style for buttons throughout the application.

- This form also uses JavaScript `fetch()` to pass the input data from the user to Python. The reason for this use is that I wanted to provide the user with a modal once they were logged in, rather than reloading the page.

- If the user inputs incorrect data a **modal** responds with various messages depending on what was incorrect.

- When the user logs in with a correct email and password a **success modal** appears with links to their personal account page and editor page to add a new activity to the database.

- This [Account and Log In Pages Flowchart](https://i.ibb.co/x1wxDsZ/flowchart.jpg) fully explains the behavior of the forms, data checks and modal messages on this page and the [Account Page](#account-page). -->

<div align="center">
    <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
</div>

### Dashboard

- The dashboard is a control center and it contains different functionalities depending on the user privileges.
- This page is only accessible through the "Dashboard" button accessible from the collapsible menu or on the navbar, depending on screen resolution.
- The dashboard button replaces the register button once the user is logged in.

**Non-Staff user**

- This page displays a card with the information under the register of the account logged in.
- User can edit the information or delete the account through the dynamic forms.

<div align="center">
    <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
</div>

**Staff user**

- For staff users, the dashboard gives access to all the information in the database.
- The staff member can access the "Users", "Adoption Requests" and "Register" pages.

  - **Users page**: Displays all the users on the database individually on cards that contain the "Edit" and "Delete" buttons activating the respective dynamic form. This page is visible only to staff users.

    <div align="center">
    <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
    </div>

  - **Adoption Requests page**: Displays a list of cards, each one containing one of the adoption requests in the database. This page is visible only to staff users.
    The staff user can mark the dog as: - Adopted: Deletes the dog and the adoption request records from the database. - Not Adopted: Keeps the dog record and deletes only the adoption record.

    <div align="center">
    <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
    </div>

  - **Register page**: Directs the user to the register page where staff can create new dog or user(customer, service or store) entries in the database.
    The staff user can mark the dog as: - Adopted: Deletes the dog and the adoption request records from the database. - Not Adopted: Keeps the dog record and deletes only the adoption record.

    <div align="center">
        <img src="static/images/wf-images/" alt="Screenshot: Navbar staff user" >
    </div>

<!-- ### Contact Page

- The Contact Page features an **email contact form**, which is wired up to my email address with [EmailJS](http://www.emailjs.com/).

- The contact page also features the contact information for Family Hub as displayed in the footer, with a link to google maps for the location. -->

<!-- ### Privacy and Cookies Policy Page

- Features a dummy privacy and cookies policy (to be updated and checked for legality before the site is launched for real).

### 404 Page

- The custom 404 Page contains a fun animation of a robot playing hide and seek, and two buttons to return the user back to the Family Hub **home page** or **activities page**.

### Permission Denied page

- The custom permission denied page features a humorous surprise for the user who attempts to access pages you must be logged in to access, while being logged out.

- Two buttons on this page give the user a choice to either go to the **log in** page or **go back** one item in their browser history to whatever page they were on before this one. -->

## Features Left to Implement

1. Pagination

   - For the presentation of this project, pagination wasn't considered a necessity as the number of registers is very limited.
   - To deal with real world database sizes, the pagination would prevent the users from scrolling for too long and spoiling the overall experience.

2. Filter

   - A filter to help the user to focus on specific categories when searching for dogs, services or stores.

3. More secure login and logout protocol

   - Implementation of a more secure protocol for better protection of users' information.

4. Email authentication

   - Implementation of email authentication of user account before registration is complete.

5. Google maps API

   - Implementation of maps to display stores and services locations on map.
   - Offer a "find near me" function where users can find stores and services based on present location.

6. Promotion Carousel

   - As an extra source of revenue, the carousel could be used to promote products or services.
   - The carousel will replace the image that is displayed on top of every page.

7. Events Section

   - As an oportunity to promote more business and engagement among customers, service providers and stores.
   - This section also opens more oportunities of revenue and brand exposition.

8. Profile images on cards

   - Implementation of functionality where users can upload their profile image or choose from a preset collection.

9. Expiration date for promotional codes

   - Implementation of a field on services and stores cards near the promotional codes displaying an expiration date as a way to create the sense of urgency on users.

This section will continue to grow as the site is deployed to it's own domain. New issues and needs will be found as we continually revaulate the application and other can become apparent as the site is used.

# Information Architecture

### Database Choice

As a course requirement, this project is based on a NoSQL database structure. This project was molded to suit better the database characteristics but it could also have been based on a SQL database structure. This project uses the NoSQL MongoDB Database.

### Data Storage Types

The types of data stored in MongoDB for this project are:

- ObjectId
- String
- Object

### Collections Data Structure

Pawer structure is based on three collections:

#### Users Collection

This collection keeps all user types (customer, services and stores) together for this project but on a real world application it could be hard to manage. We consider the use of separate files to be a better choice both for organization and management reasons.

Different user types contain different keys:

-**User**
| Title | Key in db | Form Validation Type | Data Type|
--- | --- | --- | ---
Account ID | \_id | None | ObjectId
First Name | first_name | text | string
Last Name | last_name | text | string
Email Address | \_email | email | string
Password | password | password | string
Bio | user_description | text | string
Staff Status | is_staff | text | string
Type of user | usr_type | text | string

<!--
Account ID | _id | None | ObjectId
Name | username | text, `maxlength="40"` | string
Email Address | email | email, `maxlength="40"` | string
Password | password | text, `maxlength="15"` | string -->

-**Service**
| Title | Key in db | Form Validation Type | Data Type|
--- | --- | --- | ---
Account ID | \_id | None | ObjectId
Service Provider First Name | service_first_name | text | string
Service Provider Last Name | service_last_name | text | string
Email Address | \_email | email | string
Password | password | password | string
Type of Service | type_of_service | text | string
Affiliate Link | aff_link | text | string
Discount Code | discount_code | text | string
Discount Amount | discount_amount | text | string
Service Description | service_description | text | string
Staff Status | is_staff | text | string
Type of user | usr_type | text | string
Feedback Received | fb_received | None | object
Positive Feedback | positive | text | string
Negative Feedback | negative | text | string

-**Store**
| Title | Key in db | Form Validation Type | Data Type|
--- | --- | --- | ---
Account ID | \_id | None | ObjectId
Store Name | store_name | text | string
Store Address | store_address | text | string
Email Address | \_email | email | string
Password | password | password | string
Type of Service | type_of_service | text | string
Affiliate Link | aff_link | text | string
Discount Code | discount_code | text | string
Discount Amount | discount_amount | text | string
Store Description | service_description | text | string
Staff Status | is_staff | text | string
Type of user | usr_type | text | string
Feedback Received | fb_received | None | object
Positive Feedback | positive | text | string
Negative Feedback | negative | text | string

#### Dogs Collection

| Title           | Key in db       | Form Validation Type | Data Type |
| --------------- | --------------- | -------------------- | --------- |
| Dog ID          | \_id            | None                 | ObjectId  |
| Dog Name        | dog_name        | text                 | string    |
| Dog Breed       | dog_breed       | text                 | string    |
| Dog Description | dog_description | text                 | string    |

#### Adoption Requests Collection

The documents within the adoptRequest collection are a result of the junction of information from the the user (that applied for the adoption) and dog records.

| Title           | Key in db        | Form Validation Type | Data Type |
| --------------- | ---------------- | -------------------- | --------- |
| Request ID      | \_id             | None                 | ObjectId  |
| User First Name | first_name       | text                 | string    |
| User Last Name  | last_name        | text                 | string    |
| Email Address   | \_email          | email                | string    |
| Password        | password         | password             | string    |
| Bio             | user_description | text                 | string    |
| Staff Status    | is_staff         | text                 | string    |
| Type of user    | usr_type         | text                 | string    |
| User ID         | usr_id           | None                 | ObjectID  |
| Dog ID          | \_id             | None                 | ObjectId  |
| Dog Name        | dog_name         | text                 | string    |
| Dog Breed       | dog_breed        | text                 | string    |
| Dog Description | dog_description  | text                 | string    |

<!--
| Title | Key in db | form validation type | Data type |
--- | --- | --- | ---
Activity ID | _id | None | ObjectId
Username | username |text, `maxlength="40"` | string
Title | title | text, `maxlength="50"` | string
Activity image | imgUrl | url, `maxlength="200"` | string
Indoor | indoor | checkbox | boolean
Outdoor | outdoor | checkbox | boolean
Description | description | textarea | string
Short Description | shortDescription | automatically generated | string
Published | published | User click "publish" button | boolean
Recommended | recommended | checkbox (admin only) | boolean
  |   |   |    -->

- The usr_type field is retrieved from the type of form that the user chose during the registration.

- The is_staff value is only changeable by staff accounts and Python uses an if statement to determine if it was activated on the registration/edit forms and attributes a value to the key accordingly.

# Technologies Used

### Tools

- [Gitpod](https://www.gitpod.io/) is the main IDE used for developing this project.
- [Visual Studio Code](https://code.visualstudio.com/) was also used as IDE for development when Gitpod wasn't available.
  <!-- - [Imgbb](https://imgbb.com) to store all external images for this project. -->
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) is the database for this project
- [GitHub](https://github.com/) to store and share all project code remotely.
- [GIMP](https://www.gimp.org/) to edit, crop and save images.
  <!-- - [Browserstack](https://www.browserstack.com/) to test functionality on all browsers and devices. -->
- [Am I Responsive](http://ami.responsivedesign.is/) to create the responsive image when displayed on different devices.
  <!-- - [EZgif](https://ezgif.com/video-to-gif) provided gif editing software for the gif in this readme file. -->

### Libraries

- [JQuery](https://jquery.com) to simplify DOM manipulation.
  <!-- - [Jasmine](https://jasmine.github.io/) to run automated tests on JavaScript and jQuery code.
- [Jasmine-jQuery](https://github.com/velesin/jasmine-jquery) to make it possible to test jQuery code using Jasmine. -->
  <!-- - [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily. -->
- [Materialize](https://materializecss.com/) to provide icons and a consistent and responsive structure to the website.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [PyMongo](https://api.mongodb.com/python/current/) to make communication between Python and MongoDB possible.
- [Flask](https://flask.palletsprojects.com/en/1.0.x/) to construct and render pages.
- [Jinja](http://jinja.pocoo.org/docs/2.10/) to simplify displaying data from the backend of this project smoothly and effectively in html.

### Languages

- This project uses HTML, CSS, JavaScript and Python programming languages.

# Testing

<!-- Testing information can be found in separate [testing.md](testing.md) file -->

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools:

- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:

- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine.
  - How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).

### Instructions

1. Save a copy of the github repository located at https://github.com/romqrq/pawer by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.

```
git clone https://github.com/romqrq/Pawer
```

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:

```
python -m .venv venv
```

_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:

```
.venv\Scripts\activate
```

_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

4. If needed, Upgrade pip locally with

```
pip install --upgrade pip.
```

5. Install all required modules with the command

```
pip -r requirements.txt.
```

6. In your local IDE create a file called `.flaskenv`.

7. Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database `pawer`, with 3 collections called `dogs`, `users` and `adoptRequest`.

   <!-- You will find example json structures for these collections in the [schemas](familyhubapp/data/schemas) folder. -->

8. You can now run the application with the command

```
python app.py
```

9. You can visit the website at `http://127.0.0.1:5000`

## Heroku Deployment

To deploy Pawer to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

5. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

6. Confirm the linking of the heroku app to the correct GitHub repository.

7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

8. Set the following config vars:

| Key        | Value                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| DEBUG      | FALSE                                                                                                              |
| IP         | 0.0.0.0                                                                                                            |
| MONGO_URI  | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority` |
| PORT       | 5000                                                                                                               |
| SECRET_KEY | `<your_secret_key>`                                                                                                |

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

# Credits

## Content

- All the content text was written by me.

## Media

### Images

<!-- - The FamilyHub logo was created using [Hatchful](https://hatchful.shopify.com).

- The photographs for the hero images were sourced from [Pexels](https://www.pexels.com/)

- Where possible the links to the images for the events were taken directly from the source images url in the activity listings I sourced the data from.

- On occasion when this did not work the image was copied to my local machine and then uploaded to my [imgBB](https://anna-gilhespy.imgbb.com/) account, where I took the link from instead. -->

## Code

<!-- - Template code for multi-card carousel using bootstrap classes taken from [MDBootstrap](https://mdbootstrap.com/docs/jquery/javascript/carousel/) and heavily modified to suit the sites needs.

- Code for floating buttons taken from this [W3Schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp) post.

- Box shadow codes were taken from [Material Design Box Shadows](https://codepen.io/sdthornton/pen/wBZdXq).

- Code for adding the correct prefixes to css was created using [AutoPrefixer](https://autoprefixer.github.io/).

- [Hex2rgba](http://hex2rgba.devoth.com/) was used to convert hex colours to rgba when I needed transparent background colours without using opacity css.

- Code for function to capitalize first letter of username was taken from this [paulund.co.uk](https://paulund.co.uk/how-to-capitalize-the-first-letter-of-a-string-in-javascript) post.

- Code to make sticky footer was taken from this [css-tricks.com](https://css-tricks.com/couple-takes-sticky-footer/) post.

- Code for animated side-nav taken from this [w3schools.com](https://www.w3schools.com/howto/howto_js_sidenav.asp) post.

- Code to generate slug-friendly-urls in Python taken from this [Flask](http://flask.pocoo.org/snippets/5/) post

- Code to generate slug-friendly-urls in JavaScript was taken from this [medium.com](https://medium.com/@mhagemann/the-ultimate-way-to-slugify-a-url-string-in-javascript-b8e4a0d849e1) post. -->

## Acknowledgements

<!-- Special thanks to my mentor [Simen Daehlin](https://github.com/Eventyret) for his never-ending patience and willingness to teach me not only what code works, but what is expected of my websites and code in industry. -->

# Contact

To contact me feel free to email

`gilhespy (dot) anna (at) gmail (dot) com`

## Disclaimer

The content of this website is educational purposes only.
