<h1 align="center">
    <a href="https://romqrq.github.io/pawer/" target="_blank"><img src="static/images/pawer-logo.jpg" alt="Pawer logo"/></a>
</h1>
<h2 align="center">
    <a href="https://romqrq.github.io/pawer/" target="_blank">Pawer - Dog adoption, services and stores.</a>
</h2>

<div align="center"> 

[Pawer](https://romqrq.github.io/pawer/) is an application that has the proposal to be a platform where users can adopt dogs and business/services can engage new customers.
Users can register and interact with other users information or leaving them feedback on their interaction. 
The website has a clean visual while bringing an inviting and friendly feel with an intuitive experience for the user.

As possibilities for monetization for this platform we have implemented discount codes and affiliate links. 
Other options such as premium accounts and business/service accounts are also realistic possibilities that can be implemented in the future.

<br>

[View our Pawer page](https://romqrq.github.io/pawer/)

</div>

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**Customer goals**](#customer-goals)
    - [**Service Provider goals**](#service-provider-goals)
    - [**Store goals**](#store-goals)
    - [**Developer and Business Goals**](#developer-and-Business-Goals)
    - [**User Stories**](#user-stories)
    - [**Design choices**](#design-choices)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)
    - [**How to run this project locally**](#how-to-run-this-project-locally)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

7. [**Disclaimer**](#disclaimer)

## UX

### Project Goals

The primary goal of Pawer is to create, around the dog adoption process, a meeting point for customers and business/services to meet and improve the adoption experience. 
This structure has the objective of making easier for the adoptant to get it right from the first time and reducing the chances of dogs being abandoned again. 

Pawer has four target audiences: potential dog adoptants, people that already have pets, dog-related service providers and stores.  

Potential source of income are:
- Premium accounts for customers: 
    - Discount codes for partner services or stores.
    - Personalized content from partner services or stores
- Affiliate links
- Services and stores accounts:
    - Specific paid accounts for businesses to be showcased on the platform.


#### Customer goals

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

#### Service Provider goals

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

#### Store goals

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

#### Developer and Business Goals

- Well thought out programming that offers a responsive, easy-to-use and stable platform to all users.
- A professional looking, first projeck with Python + Flask, Mongo DB, Materialize and modulated structure of files.
- Project that the developer is excited to make part of his portfolio. 
- Allow users to allow users to store and manipulate data records about a particular domain.
- Showcase an application with real possibility for monetization and with user feedback system.

#### User Stories

As a customer I want:
1. The ability to easily navigate through the application with controls that are intuitive and easy to find.
2. Visual feedback for my interactions with the content, so that I know if I have clicked or not clicked something.
3. Be able to register to the website and avail from the discounts on products and services.
4. Be able to update my register information.
5. Find a dog to adopt.
6. Find a service.
7. Find a store.
8. Leave feedback for a service provider.
9. Leave feedback for a store.

As a staff member I want:
1. The ability to easily navigate through the application with controls that are intuitive and easy to find.
2. Visual feedback for my interactions with the content, so that I know if I have clicked or not clicked something.
3. Be able to register to the website.
4. Be able to easily update register information from customers, services and stores.

As a service provider I want:
1. The ability to easily navigate through the application with controls that are intuitive and easy to find.
2. Visual feedback for my interactions with the content, so that I know if I have clicked or not clicked something.
3. Be able to register to the website and expose my service to potential customers.
4. Showcase my service on a platform that aggregates value to the service.
5. Be able to update my register information.

As a store I want:
1. The ability to easily navigate through the application with controls that are intuitive and easy to find.
2. Visual feedback for my interactions with the content, so that I know if I have clicked or not clicked something.
3. Be able to register to the website and expose my store and products to potential customers.
4. Showcase my service on a platform that aggregates value to the service.
5. Be able to update my register information.


### Design Choices

The application is aimed to provide users with a clean, consistent and easy-to-use interface with an engaging and intuitive design.


**Fonts**

- The header font **Alfa Slab One** was chosen because it has a professional look and strong character while still highly readable. It is aimed to catch the eye when the user is "sweeping" the screen looking for information. 

- The secondary font **Lexend Tera** was chosen to counter balance the header, adding a slim look with more spaced letters. It introduces a more informal visual while still favoring the readability.

- The tertiary font **Roboto** was chosen for the general text, offering a mid-term to the two previous fonts and keeping the page ballanced. It is a font with high readability and keeps a clean and professional look.

**Icons**

- All icons used were chosen from materialize library. They are all icons that have strongly established meaning and are widely used accross the internet making them easy to understand by the users.

**Colours**

- The colours chosen to the logo were a mustard-yellow, black and red. The red and yellow colours have an attention-grabbing propriety as human brain is hardwired to pay attention to these colours for primitive survival reasons. The black colour brings contrast, balance and readability to the logo.

- The buttons are on a green colour and this colour is used only for buttons, the contrast with the main colour scheme makes it grab attention. This way the user has a more consistent and predictable experience.

- The colours were saved as variables on scss file and are recalled from these variables accross the styling files to make sure the colours are consistent across the entire project.

**Styling**

- The materialize parallax class was used to give users a distinct scrolling experience while framing content, helping user to localize the information.
- Cards and buttons have slightly rounded corners for a more smooth visual.
- Cards and buttons have a slight shading for improved perspective perception by the user, helping them to recognize interactive elements on the page.
- Each database entry is displayed on a separate card, making clear to the user the individuality of each entry.
- Repetition of patterns accross the whole application provides consistency and helps the user getting familiarized to the application.

**Backgrounds**

- The elements with the parallax class display pictures that help setting the theme and the feel for each specific section or page.
- Content areas have plain white background to keep it neutral and not to compete for attention with content and pictures.

- The background image of toy trains was chosen to give the feeling of playing the game in a child's playroom. 
- Specifically chosen because it is a "flat-lay" - a photograph taken from directly above - this means the background complements the game without distracting from it.
- The background images for the modals were chosen for their comic-book like qualities, adding a little positive emotional feedback at a level that appeals to a child. 

**Card images**

- Disney and Pixar characters were chosen for this game because they are recognised and loved by children. 
Cars characters were specifically chosen because it is extremely popular with boys, 
the Frozen characters because they are very popular with girls, 
and the Toy Story Characters because they appeal to both girls and boys. 

**Audio files**

- To continue the feeling of a game made for children, clicking button sounds were added that are similar to the sounds a child might hear when operating a physical toy with buttons. 
- The card flipping sounds and "bing" on a correct match were added to give positive feedback on use of the game. 
- The sound of applauding children played on completing the game was chosen because it appeals most to children, and again fits within the theme of PicFlip!

### Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project. 

- [User info modal](https://i.ibb.co/FWBy68Q/Create-profile.png)
- [Game page](https://i.ibb.co/H2XtCW9/Game-page.png)
- [Win pop-up](https://i.ibb.co/5809P3Q/Win-popup.png)

## Features
 
### Existing Features

1. **Player info modal**
    - On arriving at the page for the first time, this modal pops up to collect the players name and their choice of avatar image from the three available. 
    - This modal is also activated if stored player data is reset. 
    - The modal has been programmed to not close unless both the name has been filled out at an avatar has been chosen. Tooltips appear to guide the user to enter both.
    - The default setting for modals that they can be closed if clicking on the modal background has also been disabled for this modal specifically.  

<div align="center">
<img src="https://i.ibb.co/NpXs3QC/user-info-modal.jpg" alt="Screenshot: User info modal" >
</div>


2. **Dashboard**
    - The game dashboard contains the player info display, difficulty selection, character selection, info, mute and reset buttons. 
    - On mobile devices a chevron arrow is displayed to tell the player to scroll downwards to the game board. 

<div align="center">
<img src="https://i.ibb.co/pwn3GFV/game-board.jpg" alt="Screenshot: Game board"><br>
<img src="https://i.ibb.co/JFr93rH/mobile-view-dashboard.jpg" alt="Screenshot: dashboard mobile view" >
</div>

3. **Player info display**
    - At the top of the dashboard the players name is displayed with their chosen avatar. 
    - Underneath this is the display to show their highest score (out of 5 stars) for the currently selected difficulty level. 
    - The star display changes if a different level is selected. 

4. **Difficulty selection buttons**
    - Players can select from three difficulty levels: Easy (8 cards), Medium (12 cards) and Hard (16 cards).
    - The difficulty buttons are coloured green, yellow and red for users who can't read to tell them apart.
    - Selecting any of these buttons turns any face-up cards back over and reshuffles the cards.

5. **Character selection buttons**
    - Players can choose from three different Disney movie characters to display on the memory cards.
    - Selecting any of these buttons turns any face-up cards back over and reshuffles the cards.

6. **Mute button**
    - The mute button switches off all audio in the game. It is represented by a large speaker icon, which switches to one with a cross next to it when active.
 
7. **Reset button**
    - The reset button, represented by a curved arrow, resets the game, when it is pressed the game turns any face-up cards back over, reshuffles them and resets the turns counter back to 0. 
    - It does not reset the difficulty level or characters chosen for the cards. 

8. **Info button**
    - Represented by a large question mark, the info button opens the info modal. 
    - The info modal offers easy to understand instructions on how to play the game. 
    - Underneath how to play instructions there is information on how to open the modal to delete the player’s profile. 
    - The place to click is easy for an adult to see, but not an obvious button to click for a child. 

<div align="center">
<img src="https://i.ibb.co/xJ7PbS2/info-modal.jpg" alt="Screenshot: Info Modal" >
</div><br>

9. **Parental check modal**
    - This modal appears if the correct icon is clicked in the info modal. 
    - It explains that deleting the player profile will remove all game data including high scores. 
    - Then it asks a simple maths question with 9 possible answers to choose from, only if the correct answer is clicked will the player profile be deleted. 
    - All other choices will close the modal when clicked with no further effects to the game.
    - At this point the maths question and correct answer are static. This is a feature I would like to update in the future (see [Features Left to Implement](#Features-left-to-implement) for more information)

<div align="center">
<img src="https://i.ibb.co/nrRkQsq/delete-data-modal.jpg" alt="Screenshot: Parental check modal" >
</div>


10. **Turns counter**
    - Located above the game cards, the turns counter counts the number of turns the player has taken in the current game. 
    - This total is then used to give the player a score out of 5 stars when the game is complete.

11. **Game board and cards**
    - The game board is where the memory cards are displayed. 
    - The cards are laid out in a grid 4 cards wide on medium to large screens, and 3 cards wide on phones to allow the size to remain easy for young fingers to tap on.
    - The number of rows of cards visible changes depending on the difficulty level selected. 

<div align="center">
<img src="https://i.ibb.co/q5sDjB4/mobile-view.jpg" alt="Screenshot: game board mobile view" >
</div>


12. **Win modals** 
    - PicFlip! has two possible win modals that pop up when a game is completed. 
    - Both win modals display the number of stars the player won for the game they just played.
    - The standard win modal is launched if the player completed the game, but did not beat their previous high score.
    - The high score win modal is launched for a new high score, along with the number of stars earned the high score win modal also displays a trophy picture.

<div align="center">
<img src="https://i.ibb.co/YRjzhw5/high-score-modal.jpg" alt="Screenshot: high score modal" >
</div>


13. **Footer tab**
    - A small tab is displayed at the bottom of the website that when clicked pulls up a short footer with developer information on. 

### Features Left to Implement

1. **Improvements to the parental check modal**

In the future more functionality can be added to the parental check modal to: 
    - Randomize the math question and active number to click to prove you are an adult. 
    - if the incorrect answer is given the math question/answer is randomised again. 
    - If the incorrect choice is made 5 times in a row then the modal closes. 

2. **Additional difficulty level**
    - Add level "insane" for older kids to try. 
    - This would only be possible on mobiles if converted into a mobile app, as the full screen would be needed to make enough room for all the cards.

3. **Conversion to a mobile App**
    - If this project were to become commercial the current card pictures would have to be changed to ones commissioned specifically for it, rather than using Disney images.

## Technologies Used

- This project uses HTML, CSS and JavaScript programming languages.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Cloud9](https://c9.io) 
    - Developer used **Cloud9** for their IDE while building the website.
- [Bootstrap](https://www.bootstrapcdn.com/)
    - The project uses **Bootstrap** to simplify the structure of the website and make the website responsive easily.
    - The project also uses Bootstrap to provide icons from [FontAwesome](https://www.bootstrapcdn.com/fontawesome/)
- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google fonts** to style the website fonts.
- [Imgbb](https://imgbb.com)
    - All external images for this project are stored on **Imgbb.com**.
- [Jasmine](https://jasmine.github.io/)
    - This project used **Jasmine** to automatically test all JavaScript and jQuery code.
- [Jasmine-jQuery](https://github.com/velesin/jasmine-jquery)
    - This project used **Jasmine-jQuery** CDN to make it possible to test jQuery code using Jasmine.
- [GitHub](https://github.com/)
    - This project uses **GitHub** to store and share all project code remotely. 
    - The new GitHub Projects planner was utilised to plan and keep track of this project. This project plan can be viewed [here](https://github.com/AJGreaves/picflip/projects/1).
- [Photoshop](www.adobe.com/Photoshop)
    - This project used tools in **Photohshop** to edit, crop and save images as well as ulitising the colour picker to ensure color consistency over the entire project.
- [Browserstack](https://www.browserstack.com/)
    - The project used **Browserstack** to test functionality on all browsers and devices.
- [AutoPrefixer](https://autoprefixer.github.io/)
    - The project used **AutoPrefixer** to make sure all css prefixes were the most up to date versions. 

## Testing 

Testing information can be found in separate [testing.md](testing.md) file

## Deployment

This project was developed using the [Cloud9 IDE](https://c9.io), committed to git and pushed to GitHub using the built in function within cloud9. 

To deploy PicFlip! to GitHub Pages from its [GitHub repository](https://github.com/AJGreaves/picflip), the following steps were taken: 
1. Log into GitHub. 
2. From the list of repositories on the screen, select **AJGreaves/picflip**.
3. From the menu items near the top of the page, select **Settings**.
4. Scroll down to the **GitHub Pages** section.
5. Under **Source** click the drop-down menu labelled **None** and select **Master Branch**
6. On selecting Master Branch the page is automatically refreshed, PicFlip! is now deployed. 
7. Scroll back down to the **GitHub Pages** section to retrieve the link to the deployed website.

The PicFlip project made use of several branches for development, testing and bug fixing. 
The Master Branch has always been the one deployed to GitHUb Pages. When displaying the website life, the developer tries to keep the master branch to optimal code only.
At the moment of submitting this Milestone project the Development Branch and Master Branch are identical. 

### How to run this project locally

To clone this project from GitHub:
1. Follow this link to the [PicFlip GitHub repository](https://github.com/AJGreaves/picflip).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.
```console
git clone https://github.com/USERNAME/REPOSITORY
```
7. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://help.github.com/en/articles/cloning-a-repository).

## Credits

### Content

- All text in this project was written by the developer.

### Media

#### Images
- The PicFlip logo was created using [Hatchful](https://hatchful.shopify.com).
- The Trophy image used was sourced from [Kissping](https://www.kisspng.com).
- The images for the user avatar were sourced from [Pngtree](https://pngtree.com).
- The images used for the memory cards were obtained from [Google Images](https://www.google.com/imghp?hl=en) and are used for educational purposes only. 
Copyright for the memory card images belong to [Disney](https://www.thewaltdisneycompany.com/) and [Pixar](https://www.pixar.com/).
- The comic-book style modal backgrounds were sourced from [freepik](https://www.freepik.com)
- The game board background photograph was obtained from [Jason Leung on Unsplash](https://unsplash.com/photos/M55JcA9wOG0).

#### Audio
- The audio file for button click sound was sourced from [SoundJay](https://www.soundjay.com).
- The audio files for card flip sound, matched cards sound and children applauding were sourced from [FreeSound](https://freesound.org/).

### Code
- Code for the card flip animation taken from this [W3Schools](https://www.w3schools.com/howto/howto_css_flip_card.asp) post.
- Box shadow codes were generated at [CSS matic | box-shadow](https://cssmatic.com/box-shadow).
- Code for filtering through an array for specific values sourced from this [StackOverflow](https://stackoverflow.com/questions/6120931/how-to-count-the-number-of-certain-element-in-an-array) post.
- Code for making images into radio buttons sourced from this [StackOverflow](https://stackoverflow.com/questions/17541614/use-images-instead-of-radio-buttons) post.
- Code for adding the correct prefixes to css was created using [AutoPrefixer](https://autoprefixer.github.io/).
- Function to toggle text in the pull up tab from push to pull taken from this [StackOverflow](https://stackoverflow.com/questions/2155453/jquery-toggle-text) post.

### Acknowledgements

Special thanks to: 
- Code Institute Mentor Simen Daehlin for his time and support in explaining and demonstrating areas of code this developer was struggling to understand.
- Alumni John Longgately and Robin Zigmond for their help in guiding this developer in understanding JavaScript, jQuery and Jasmine testing. 
- Owen (4) and Declan (9) who tested the game play extensively, and offered advice on what would make it more fun for them to play.

#### Disclaimer
The content of this website, including the images used, are for educational purposes only.

### A note to my fellow Code Institute students

I am happy that you have come to look at my readme as an example of how to write a good one for your second Milestone project. You are welcome to learn how to structure and format your own readme from mine.

However, it is not ok to copy and paste large portions of it into your own project. Please remember to write your own readme yourself, rather than copying mine or someone elses.

Many thanks! Anna