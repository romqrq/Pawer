# Pawer - Testing details

[Main README.md file](README.md)

[View website on Heroku](https://pawer-db.herokuapp.com/)

## Table of Contents

1. [User Stories Testing](#user-stories-testing)
   - [Customer User Stories](#customer-user-stories)
   - [Services User Stories](#services-user-stories)
   - [Stores User Stories](#stores-user-stories)
   - [Staff User Stories](#staff-user-stories)
2. [Manual Testing](#manual-testing)
   - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
   - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
3. [Google Chrome Developer Tools Audits](#google-chrome-developer-tools-audits)
4. [Bugs discovered](#bugs-discovered)
   - [Solved bugs](#solved-bugs)
   - [Unsolved bugs](#unsolved-bugs)
5. [Further Testing](#further-testing)

### A note about TDD and automated tests

This project did not utilize Test Driven Development for Jasmine or Python while it is a student project. The reason for this was that I am still very new to both JavaScript and Python and found it impossible to write tests for languages I did not understand well.
During this project, I reached a better understanding of Python and JavaScript and I intend to apply the concept of Test Driven Development in my next project.

Considering the size and complexity of this project I am confident that the manual testing was thorough enough to compensate for the lack of automated tests.

### Validation Services

The following validation services and linter were used to check the validity of the website code.

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML.

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

- [Power Mapper](https://https://www.powermapper.com/products/sortsite/checks/browser-compatibility/) was used to test browser compatibility.

### Python Testing

- Despite following the pertinent documentation and information from diverse sources, I was unable to make automated tests to work for the Python code in this project due to incompatibilities in the workspace on Gitpod that I couldn't figure out at this time.

- The feedback from the Python console was used as main channel to receive error codes, check the status of requests and troubleshooting in general.

## User Stories Testing

The following section goes through each of the user stories from the UX section of [README.md](README.md)

### Customer User Stories

**As a customer visiting the Pawer website I expect/want/need**

1. _To login or register._

   - Login and register buttons are always easily accessible:

     - Navbar is always visible at the top of the screen and for medium resolution and up, the register and login buttons are visible on the right of the navbar.

     - On small resolution the register and login buttons are part of the collapsed menu.

     - The Register and login buttons are also present on the adoptions page and bring the user to the correct pages.

   - Login page is laid out with one single function:

     - The reduced amount of information on the page allows the user to figure out what to do at a glance.

     - Fields for email and password are labeled with placeholders with the respective name for the information required.

     - The login button is placed immediately below the input fields, creating a connection and helps the user understanding that it is the next step to login.

     - Upon form submission, session receives the correct variables for different account types.

   - Register page with cards for different account types:

     - The page displays cards for each type of account the user can create.

     - The cards are displayed dynamically depending on account privileges.

     - Cards automatically adjust to screen width depending on number of cards displayed( 3 for non staff and 4 for staff) through jinja.

     - Pulsating red button on each card triggers respective registration form.

     - Registration forms are shown and hidden dynamically as the user chooses different options. This keeps the page cleaner and only displays to the user the information that is pertinent to their choices.

     - Short sentences are displayed at the bottom half of each card explaining their respective function.

     - Forms are triggered correctly, data is stored correctly on the database and is correctly displayed back on the application.

2. _Finding a dog to adopt._

   - Adoption link/button on the navbar/sidenav and home page:

     - The button brings the user to the adoption page and it is easily accessible.

     - The button within the adoption session on the home page brings the user to the adoptions page.

   - Creating adoption request:

     - Users must be logged in to create an adoption request and the adoption page offers content explaining the need for registration/login.

     - Buttons were also added as part of the content on the adoptions page as during tests, users didn't read the text and nothing grabbed their attention enough to suggest further action.

     - Adopt button triggers pertinent form and information is sent to the database correctly creating a new adoption request.

     - The request is displayed correctly on staff dashboard.

3. _Finding products or services to buy._

   - Services and stores pages are easily accessible through navigation bar(medium screen resolutions and up), sidenav (small screen resolution) and on the body of the home page within its respective section.

   - The buttons and links direct the user correctly to the intended pages.

   - Records are displayed correctly on services and stores pages.

   - A variety of information from each service or store is displayed in an organized and consistent manner.

4. _Finding stores or services nearby._

   - Stores have their address and contact on top of the cards together with the store name.

   - Services don't have address but the contact information is displayed at a proeminent area of the card near the name of the service provider.

5. _Minimum effort to reach my goals._

   - The navigation bar contains links to all the pages and functions the user can access.

   - All buttons and links direct the user to the correct page and logout button gives user feedback after logout.

6. _Use the application intuitively with minimum of learning._

   - The layout used on the page is based on standard rules and best practices that are widespread accross the internet, making the website feel more "familiar" to the user.

   - Icons are displayed on buttons adding a visual, non-verbal layer of communication with the user.

   - Visual feedback is used to give the user confirmation after actions taken. Both for successful or falied actions.

7. _Ability to edit and delete my account details_

   - Dashboard button always visible on the navbar and sidenav brings the user to the correct page.

   - User information and buttons are correctly displayed in the card.

   - Forms to edit or delete information are correctly triggered by the respective buttons.

   - Edit form adds/changes the information from the database correctly.

   - Delete form removes user account from the database correctly.

### Services and Stores Stories

**As a service provider/ Store in Pawer I expect/want/need**

1. _Expose my service/products to a mass of potential new customers._

   - The informations for the service provider/store are displayed correctly to users and within a structured and clear structure.

   - Affiliate links redirect users correctly to external website.

2. _To have reasonable possibility of return over investment (when services account system is implemented)._

   - Service providers can offer discounts through discount codes. The discount code and amount to be discounted display correctly in the service card.

   - The discount codes can be added during registration or through the dashboard. Both methods work to add and change the value for the respective keys on the database

3. _Balanced competition for space between companies and individuals providing the same service._

   - Cards are uniform and offer the same space for all service providers.

   - When returning to the site and logging in again all their activities are saved and accessible in their account page.

4. _Protection against accidental deletion of my information._

   - Delete button triggers a form asking for user confirmation before deleting the information from the database.

5. _Increase physical customer presence at stores (for business with physical stores)._

   - Store address is displayed correctly on the card for each of the stores.

## Manual Testing

Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected.

### Testing undertaken on desktop

All steps on desktop were repeated using Google Chrome Developer Tools to simulate different screen resolutions and orientations.

#### Elements on every page

1. Navbar

   - Hover over each link and button, confirm the hover effect works as expected.
   - Click the **Pawer logo**, confirm it takes the user to the home page.
   - Click the **Home** link, confirm it takes the user to the home page.
   - Click the **Adoption** link, confirm it takes the user to the adoptions page.
   - Click the **Services** link, confirm it takes the user to the services page.
   - Click the **Stores** link, confirm it takes the user to the stores page.
   - Click the **Register** button, confirm it takes the user to the register page.
   - Click the **Login** button, confirm it takes the user to the log in page.
   - Log into the application, confirm that the navbar no longer displays the **Register** or **Login** buttons but does now display the **Dashboard** and **Logout** buttons.
   - Click the **Dashboard** button, confirm it takes the user to their account page.
   - Click the **Logout** button, confirm it takes the user to the home page, the navbar displays again the **Register** or **Login** buttons and logout feedback is displayed.

2. Footer
   - Hover over each link, confirm the pointer changes as expected over links.
   - Click the **Youtube**, **Twitter**, **Facebook** and **Instagram** links, they open the relevant social media pages in separate browser tabs.

#### Home Page

1. Images

   - Confirm that images load at a reasonable speed, and that they are sharp, clear and not distorted.
   - Parallax effect working on all images.
   - Image size adjusts to the screen size as expected.

2. Text formatting

   - Text is easy to read.
   - Fonts are loaded correctly.
   - Backup fonts are loaded correctly.

3. Adopt, Services and Stores buttons

   - Buttons bring the user to the correct pages.
   - Hover effect works as expected.
   - Click feedback works as expected.

#### Adoption Page

1. Images

   - Confirm that images load at a reasonable speed, and that they are sharp, clear and not distorted.
   - Parallax effect working on all images.
   - Image size adjusts to the screen size as expected.

2. Text formatting

   - Text is easy to read.
   - Fonts are loaded correctly.
   - Backup fonts are loaded correctly.

3. Login and Register section buttons

   - Buttons bring the user to the correct pages.
   - Hover effect works as expected.
   - Click feedback works as expected.

4. Dog cards

   - Cards are displayed correctly and are responsive to different screen resolutions.
   - Adopt button is displayed correctly once the user is logged in and hidden when the user is not logged in.
   - Adoption button triggers the form correctly
   - Adoption form posts the information correctly to Python.
   - Edit and delete buttons are displayed correctly for staff users only.
   - Edit and delete buttons trigger the correct forms.
   - Edit and delete forms post the informations correctly to Python.

#### Services Page

1. Images

   - Confirm that images load at a reasonable speed, and that they are sharp, clear and not distorted.
   - Parallax effect working on all images.
   - Image size adjusts to the screen size as expected.

2. Text formatting

   - Text is easy to read.
   - Fonts are loaded correctly.
   - Backup fonts are loaded correctly.

3. Login and Register section buttons

   - Buttons bring the user to the correct pages.
   - Hover effect works as expected.
   - Click feedback works as expected.

4. Services cards

   - Cards are displayed correctly and are responsive to different screen resolutions.
   - Services informations are displayed correctly on the cards.
   - Feedback left by users is displayed correctly.
   - Feedback button is displayed correctly once the user is logged in and hidden when the user is not logged in.
   - Feedback button triggers the form correctly
   - Feedback form posts the information correctly to Python.
   - Edit and delete buttons are displayed correctly for staff users only.
   - Edit and delete buttons trigger the correct forms.
   - Edit and delete forms post the informations correctly to Python.

#### Stores Page

1. Images

   - Confirm that images load at a reasonable speed, and that they are sharp, clear and not distorted.
   - Parallax effect working on all images.
   - Image size adjusts to the screen size as expected.

2. Text formatting

   - Text is easy to read.
   - Fonts are loaded correctly.
   - Backup fonts are loaded correctly.

3. Login and Register section buttons

   - Buttons bring the user to the correct pages.
   - Hover effect works as expected.
   - Click feedback works as expected.

4. Stores cards

   - Cards are displayed correctly and are responsive to different screen resolutions.
   - Stores informations are displayed correctly on the cards.
   - Feedback left by users is displayed correctly.
   - Feedback button is displayed correctly once the user is logged in and hidden when the user is not logged in.
   - Feedback button triggers the form correctly
   - Feedback form posts the information correctly to Python.
   - Edit and delete buttons are displayed correctly for staff users only.
   - Edit and delete buttons trigger the correct forms.
   - Edit and delete forms post the informations correctly to Python.

#### Login Page

1. Images

   - Confirm that images load at a reasonable speed, and that they are sharp, clear and not distorted.
   - Parallax effect working on all images.
   - Image size adjusts to the screen size as expected.

2. Login form

   - Form loads correctly through different screen resolutions.
   - Placeholders displayed correctly and are responsive to users interactions.
   - Validation of the email field requests for a valid e-mail format.
   - Password field hides the user input with dots.
   - Login button is displayed correctly and posts the information correctly to Python.

3. Successful login - User redirect

   - User is correctly redirected to home page.
   - Visual feedback confirms the successful login.

4. Unsuccessful login

   - Visual feedback tells the user "Invalid email or password."

#### Register Page

1. Images

   - Confirm that images load at a reasonable speed, and that they are sharp, clear and not distorted.
   - Parallax effect working on all images.
   - Image size adjusts to the screen size as expected.

2. Text formatting

   - Text is easy to read.
   - Fonts are loaded correctly.
   - Backup fonts are loaded correctly.

3. Account type cards

   - Confirm that "Dogs" account card is visible to staff user only.
   - Confirm that cards are formatted correctly taking 3 or 4 collumns depending on user being staff or not staff, respectively.
   - Cards content is responsive and displayed correctly on different screen resolutions.
   - Red pulse button triggers the correct forms.

4. Register account forms

   - Form is correctly scrolled into view when activated.
   - Text is correctly displayed.
   - Confirm that trying to send the form without filling out any fields causes the form to prompt the user to fill out the fields.
   - Field characters limitter works.
   - Field validation requests user action to correct the information provided.
   - Character counter is displayed correctly.
   - Create account button loads correctly and posts the information correctly to python.

5. Successful registration - Redirect user

   - User is correctly redirected to the home page.
   - "You have been successfully registered! Welcome!" message is displayed as visual feedback to the user.

#### Dashboard Page - Non-Staff user

1. Images

   - Confirm that images load at a reasonable speed, and that they are sharp, clear and not distorted.
   - Parallax effect working on all images.
   - Image size adjusts to the screen size as expected.

2. Text formatting

   - Text is easy to read.
   - Fonts are loaded correctly.
   - Backup fonts are loaded correctly.

3. User card

   - Card is displayed correctly and responsive to different screen resolutions.
   - Edit and delete buttons are displayed correctly.
   - Edit and delete buttons trigger the correct forms.

4. Edit form

   - Form is formatted correctly.
   - Text is displayed correctly
   - Placeholders are displayed correctly.
   - Update Account button is displayed correctly.
   - Form posts information correctly to Python.

5. Delete form

   - Form is formatted correctly.
   - Text is displayed correctly.
   - Delete button is displayed correctly.
   - Information is posted correctly to Python.

#### Dashboard Page - Staff user

1. Images

   - Confirm that images load at a reasonable speed, and that they are sharp, clear and not distorted.
   - Parallax effect working on all images.
   - Image size adjusts to the screen size as expected.

2. Text formatting

   - Text is easy to read.
   - Fonts are loaded correctly.
   - Backup fonts are loaded correctly.

3. Users, Adoption Requests and Create New Account cards

   - Cards are displayed correctly and responsive to different screen resolutions.
   - Buttons are displayed correctly.
   - Buttons bring user to correct pages.

#### Users Page - Staff user

1. Images

   - Confirm that images load at a reasonable speed, and that they are sharp, clear and not distorted.
   - Parallax effect working on all images.
   - Image size adjusts to the screen size as expected.

2. Text formatting

   - Text is easy to read.
   - Fonts are loaded correctly.
   - Backup fonts are loaded correctly.

3. Users cards

   - Cards are displayed correctly and responsive to different screen resolutions.
   - Edit and delete buttons are displayed correctly.
   - Edit and delete buttons trigger the correct forms.

4. Edit form

   - Form is formatted correctly.
   - Text is displayed correctly
   - Placeholders are displayed correctly.
   - Update Account button is displayed correctly.
   - Form posts information correctly to Python.

5. Delete form

   - Form is formatted correctly.
   - Text is displayed correctly.
   - Delete button is displayed correctly.
   - Information is posted correctly to Python.

#### Adoption Requests Page - Staff user

1. Images

   - Confirm that images load at a reasonable speed, and that they are sharp, clear and not distorted.
   - Parallax effect working on all images.
   - Image size adjusts to the screen size as expected.

2. Text formatting

   - Text is easy to read.
   - Fonts are loaded correctly.
   - Backup fonts are loaded correctly.

3. Adoption requests cards

   - Cards are displayed correctly and responsive to different screen resolutions.
   - Yes and No buttons are displayed correctly asking the user if the dog has been adopted or not.
   - Yes and No buttons trigger the correct forms.

4. Dog not adopted form

   - Form is formatted correctly.
   - Text is displayed correctly
   - "Yes, Delete" button is displayed correctly.
   - Form posts information correctly to Python.

5. Adoption forms

   - Forms are formatted correctly.
   - Text is displayed correctly.
   - "Yes, Delete" button is displayed correctly.
   - Information is posted correctly to Python.

#### Log Out Feature

- When logged in, click the logout link, confirm that the user is no longer logged in by checking that no session data can be seen in developer tools.
- Text feedback is displayed confirming to the user that logout was successful.

#### Permission Denied Page

- When not logged in with a staff account, administrative pages display text to warn users that page isn't visible to non-staff users.
- Button "Bring me back home" loads correctly and redirects the user to the home page.

### Testing undertaken on tablet and phone devices

All steps below were repeated to test mobile and tablet specific elements on my Motorola phone and Samsung tablet, in both the firefox browser and samsung internet browser.

Friends and family also used the application through diverse devices and browsers.

Responsive design waw also tested in the Chrome Developer Tools device simulators on all options and orientations.

The screen size of the iPhone 5/SE was used as reference as it is the smallest screen size on Chrome Developer Tools. This way elements would be designed from the smallest size and, consequently, fit on the larger screens keeping the desired form.

#### Elements on every page

1. Navbar

- Open the website on mobile, confirm that the navbar is collapsed into a burger icon
- click the burger icon, confirm that the sidenav list appears as expected.
- Click the **Pawer logo**, confirm it takes the user to the home page.
- When logged in, confirm that the sidenav list appears as expected for someone logged in.
- When on tablet, confirm that the navbar is not collapsed on a larger tablet screen (iPad Pro), but is on smaller tablets (iPad).
- Sidenav
  - Click the **Home** link, confirm it takes the user to the home page.
  - Click the **Adoption** link, confirm it takes the user to the adoptions page.
  - Click the **Services** link, confirm it takes the user to the services page.
  - Click the **Stores** link, confirm it takes the user to the stores page.
  - Click the **Register** button, confirm it takes the user to the register page.
  - Click the **Login** button, confirm it takes the user to the log in page.
  - Log into the application, confirm that the sidenav no longer displays the **Register** or **Login** buttons but does now display the **Dashboard** and **Logout** buttons.
  - Click the **Dashboard** button, confirm it takes the user to their account page.
  - Click the **Logout** button, confirm it takes the user to the home page, the sidenav displays again the **Register** or **Login** buttons and logout feedback is displayed.

2. Footer

   - Click the **Youtube**, **Twitter**, **Facebook** and **Instagram** links, they open the relevant social media pages in separate browser tabs.

#### Home Page

- When viewing on **mobile**, Confirm that the home page appears as expected.

- Parallax image is displayed full width and correct height.

- Confirm that all buttons and links are clickable on the smaller screen.

#### Adoption, Services, Stores, Dashboards, Users, Adoption Requests and Register Pages

- When viewing on **mobile**, confirm that the cards are displayed full width, as expected, with information organized vertically.

- When viewing on **tablet**, confirm that cards are displayed full width, as expected, with information organized horizontally.

#### All Other Pages

- Confirm the layout of all other pages is as designed on mobiles and tablets.

### Google Chrome Developer Tools Audits

- The application was also tested through Google Chrome Developer Tools Audits covering **Performance**, **Accessibility**, **Best Practices** and **SEO**.

- Audits were made for Desktop and Mobile.

- All areas tested reached satisfying results except for **Performance**
  - A big delay is apparently being created by materialize triggering JavaScript calls during page loading.
  - During the tests, it created delays between 2.3s and 3.3s.
  - At this time we weren't able to come around this issue that even though wasn't the only one it is, by far, the most significative one that we couldn't fix.

### Bugs discovered

#### Solved bugs

1. **Register and Login buttons disappearing after logout**

   - When the user logged out, the login and register buttons weren't visible on the navbar and sidenav unless the user clicked to go to another page.

   - To solve this I changed the jinja if statement to display the buttons when there was no session['is_staff'] value created.

```Python
{% if not session['is_staff'] %}
<a href="{{url_for('register')}}" class="btn waves-effect nav-action-button">Register</a>
<a href="{{url_for('user_login')}}" class="btn waves-effect nav-action-button">Login</a>
{% endif %}

```

2. **KeyError when creating new user**

- When trying to create new user and include the "is_staff" key, I would get an error if the form were submitted with the staff status switch turned off.
- Fix: Created a try-except operation to specifically deal with the KeyError raised by the operation.

```Python
try:
request.form['is_staff']
except KeyError:
user.update_one({'email': request.form.get('email')},
{'\$set': {'is_staff': 'not_staff',
'usr_type': usr_type}})

```

3. **Cards on Services and Stores pages not loading correctly**

- Cards were being loaded one inside the other creating a horizontal overflow

- The problem found was the end of the for loop. It was closing before the </div> tag of the element that contained the card.

- The problem was fixed moving the "endfor" tag to after the </div> tag.

4. **TypeError message during non-staff logout**

- When non-staff users logged out, the session.pop('is_staff') would trigger a TypeError message.

```Python
@APP.route('/logout', methods=['GET', 'POST'])
def user_logout():
    """ Simplified logout function that removes items added to the session
    list during login """

    session.pop('is_staff')
    session.pop('user_id')
    session.pop('user_type')

    flash('You have been logged out successfully.', 'info')
    return render_template('pages/index.html')
```

- The 'is_staff', 'user_id' and 'user_type' were values added to the session during login, taking the values from the user's record on the database.

- As non-staff users were getting a '0' result for the is_staff key, it wasn't being created on the database and when the logout operation tried to pop this value from the session, it threw the error.

- The fix:

  - During registration, the 'is_staff' key is created on every user record and it receives the value of 'not_staff'.

```Python
try:
   request.form['is_staff']
except KeyError:
   user.update_one({'email': request.form.get('email')},
                     {'$set': {'is_staff': 'not_staff',
                              'usr_type': usr_type}})
```

- A more elegant logout approach was also adopted simplifying the code using session.clear() replacing the targeting of individual values contained in the session:

```Python
@APP.route('/logout', methods=['GET', 'POST'])
def user_logout():
    """ Simplified logout function that removes items added to the session
    list during login """

    session.clear()

    flash('You have been logged out successfully.', 'info')
    return render_template('pages/index.html')
```

5. **Update function not working as expected**

- When users were trying to edit their information, the empty fields were replacing the information on the database.

- To get around this problem I created an if statement within a for loop checking for fields that were filled in and only updating those specific values on the database.

```Python
@APP.route('/update/<usr_type>/<usr_id>', methods=['GET', 'POST'])
def update_entry(usr_type, usr_id):
    """
    Function to update entries on the database. It takes the user to determine
    the collection to be targeted and the user id to find the specific record
    in the collection.
    """

    if usr_type == 'dogs':
        user = MONGO.db.dogs
        get_user = 'get_dogs'

    else:
        get_user = 'get_'+str(usr_type)
        user = MONGO.db.users

    document = user.find_one()
    for key in document:
        if key != '_id':
            field_name = request.form.get(key)
            if field_name:
                user.update_one({'_id': ObjectId(usr_id)},
                                {'$set': {key: request.form.get(key)}})

    return redirect(url_for(get_user))
```

#### Unsolved bugs

No unsolved bugs at the moment!

## Further testing:

1. Asked fellow students, friends and family to look at the application on their devices and report any issues they found.
2. Pawer was tested on all screen sizes and orientations available on Google Chrome Developer Tools.
