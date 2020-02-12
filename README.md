# BEAR NATION GAMING
## Milestone Project Four - (Full Stack Frameworks with Django - CI)
By Martin Crowley

[![Build Status](https://travis-ci.org/Mcrowley93/bear_nation_gaming.svg?branch=master)](https://travis-ci.org/Mcrowley93/bear_nation_gaming)

The deployed project can be found at: https://bear-nation-gaming.herokuapp.com/

### User Experience (UX)
#### Project Purpose
In this project I am focusing on creating a website aimed towards the gaming community that will give them some background on the group and their aims, as well as providing them with a platform on which they can read reviews for games, connect with other gamers and purchase Bear Nation Gaming merchandise which would help the brand to grow and expand on the content it creates.

Users will also be able to register and login to access other features such as being able to add their own reviews to the website, as well as post their own messages to the community noticeboard to allow them to connect with other users. They will also be able to edit and delete the reviews they have added to the website (should such action need to be taken).

This project will use a postgres database, and the application itself will be set up using the Django web framework.

The primary target audience is anyone that has an interest in gaming, whether they are casual gamers that use their console to wind down in an evening, or the type of gamer to sit through a 12-hour gaming session like it’s nothing. Due to the nature of providing an online store that requires payment for merchandise, as well as being able to post/read messages and connect with others, the age range I will be targeting will be 18+.

#### Why would a user want this?
The video games industry is worth around $152.1 billion (which is up by roughly 9.6% from the 2018 figure of $138.7 billion), and with around 2.3 billion gamers in the world. This shows the possible reach, and wide spread appeal for an application designed specifically for gamers that will provide them with the important information that they need to help them figure out if they’d enjoy a certain game or not. It would also allow less sociable gamers a chance to connect with likeminded people to exchange opinions and thoughts on the industry as a whole.

Therefore users would benefit from the website as it would allow them to make well informed decisions on whether to buy into a game or not, based on what they have seen/read prior to the games release. It would also allow them to expand their social network, as they would come to the site and be able to connect with likeminded people that also have a passion for video gaming. The users would also be able to show their passion for gaming by being able to submit their own reviews, as well as support the growth of the website and brand as a whole by either donating, and/or being able to purchase merchandise from the e-store. This would allow for more meaningful content to be produced on a regular basis.

https://www.forbes.com/sites/kevinanderton/2019/06/26/the-business-of-video-games-market-share-for-gaming-platforms-in-2019-infographic/#586fd6e7b254

https://techjury.net/stats-about/video-games-industry/#gref

#### Why is this so special?
The application will give users an easy and accessible way to view reviews on various games (whether existing or new releases), as well as providing a social element to allow other users to post comments to a message board. This would therefore encourage them to share their opinions and thoughts and even exchange PSN IDs/Gamertags, so that they may be able to connect and play online together. It also allows them to show their support through the purchase of merchandise on the website e-store, which would also help the user feel like a part of the community rather than just another registered user.

#### User Experience
The site itself will follow standard web design conventions and so the layout and initial use of the site should feel immediately recognisable to almost all users, with those lacking experience in web browsing finding the website to be self-explanatory and easy to use/navigate.

The Home page will immediately inform the user of the site’s purpose, through the use of a gaming related background image, as well as the site being labelled “Bear Nation Gaming”, and the tagline “Forging a community of likeminded gamers.”

If this doesn’t display the sites purpose clearly enough, then it will be very apparent from the rest of the information displayed on the home page as to what the site has to offer.

#### User Stories
It is key to think about what the user would require from such a site:
- As a user, I'd like to be able to view reviews of games, to give me a better idea of whether I’d like the game or not
- As a user, I'd like to add new reviews to the database/website that aren’t currently featured on the website
- As a user, I’d like to be able to edit/update a review that I have previously added to the website
- As a user, I’d like to be able to delete a review that I have previously added to the website
- As a user, I’d like to be able to easily see any reviews that I previously submitted
- As a user I’d like to be able to request reviews to be carried out on specific games I am interested in.
- As a user I’d like to be able to interact with other users and feel a part of a community
- As a user I’d like to be able to buy specific branded merchandise from the website, which would support the growth of the brand
- As a user, I’d like for the website to be user-friendly and easy to navigate
- As a user, I’d like to be able to search the website/database for the reviews on games that match search criteria
- As a user, I’d like to be able to search the website/database for the products in the store that match the search criteria
- As a user, I'd like to be able to access the data and experience all the site has to offer, regardless of device and browser type being used

Whilst the website aims to provide a service for the user and their needs ultimately need to be fulfilled to provide a good user experience, the site will also benefit the Site creator/admin, as they will be able to grow their website and brand through merchandise sales. The site will create the feeling of a community coming together by allowing users to interact with each other, as well as by allowing users to upload their own reviews. This allows the website to gain more traction as other users may come to the website to find specific reviews that they can’t find elsewhere, or to try and find other users that they can connect/play online with. This will in turn cause more traffic on the website, which also increases the chances of merchandise sales, as users feel more inclined to keep the community and brand growing.

#### Design Ideas
When thinking about the layout and the design of the site, I wanted it to look professional and of a high standard, so I used some dark colours (black, dark grey) and some bold colours (White, Orange) so as to make the website stand out and look both professional and memorable. It also has a clean aesthetic, and feels easy and approachable when using it.

I broke the design down into various style decisions:
##### Font
I will be using “Exo 2” for the website’s used font type, as this is a no-frills, modern, professional looking font that is easy to read.
##### Colour Scheme
I have opted for a darker background picture containing a PS4 controller, and the rest of the site will be of a similar colour scheme. With the grey, white and oranges being used to contrast the dark colour of the navbar, footer and background image.
##### Icons
With this project, I used Font Awesome for the icons used on the website. This was due to Font Awesome providing a large range of icons that were easily recognisable and could be used to provide visual flare. (https://fontawesome.com/icons?d=gallery) 

### Wireframes
For my wireframes, I designed these using “Justinmind Prototyper”.

For the most part, I have tried keeping the wireframes and the website fairly similar, however during the creation of certain parts of the website, other pages were conceived to allow the users of the website to feel like they have more involvement with the content on the website. For example the community page was originally going to be a community message board, but more along the lines of a continuous chat page. Yet during the creation of the community page it made more sense to make it more like a community blog, wherein users could make community posts, and these posts could be viewed and commented on by other users. 

On the reviews/community and merchandise page I opted to use a single search bar, this will search the results using one of the filters to get specific results from the search. For example if in the products/merchandise section, a user types “T-shirt” into the search bar and clicks search, the search will display all of the products in the database that have “T-shirt” in their name.

For Desktop, Mobile and tablet I opted to use a hamburger button in the top right corner. This stops the navbar looking cluttered when not being used and therefore allows for a cleaner visual aesthetic, and more pleasant user experience.

These wireframes have been included and are able to be viewed in a separate directory/folder called "Wireframes", which have subdirectories called "Desktop" and "Mobile". The views on Tablet will look like either the mobile OR the desktop wireframes, depending on whether the tablet itself is a small tablet or a large tablet, however the desktop wireframes will be the ones that will be seen on the majority of tablets due to the viewpoints, columns and styling used being so similar between tablets/desktops.

### Features
#### Current Features
- Feature 1 – Navigation
    - The navigation bar will be a dropdown side-nav, that will be accessed through clicking on the hamburger button. This is to streamline the navigation for the website, as well as leaving a clean amount of space and to save the nav looking cluttered 
    - The options displayed on the nav will also change depending on whether the user is logged in (should they have previously registered). If the user has not logged in, they will see the options on the nav to “Register” and “Log In”, whereas if the user is logged in, they will see “My Account”, “Community” and “Log Out” in their place.
- Feature 2 – Index/Home Page
    - On the index/home page, I am going to display the name of the website and an introduction. There will be access to other pages through this page, and depending on whether the user is logged in, there will be varying options available to the user.
    - When the user is logged in, they will be able to access the user’s account page as well as being able to log out.
    - When the user is not logged in, they will be able to see the pages to allow them to register and/or log in.
    - There are also links/pages that are universal on the site and can be accessed by both registered users and guest users. These features will consist of: the reviews page and the merchandise shop.
- Feature 3 – Search 
    - The search function will be available on multiple pages, with these pages being: the Reviews page, the Community Posts page, and the Merchandise/Products page. 
    - The user will be able to search using multiple filters:
    - The products page search bar can be used to search for products using their product’s name, OR the products price
    - The reviews page search bar can be used to search for reviews using a game’s name OR the platform/console OR the review score
    - The blogs page search bar can be used to search for blog posts using the post’s name, OR the blog’s author
    - Alternatively if the doesn’t enter anything into the search box and the user just clicks the search button, then every result/object in the relevant database will be displayed.
    - This feature will be available to all users, whether registered and logged in, or just browsing the site as a guest user.
- Feature 4 – Register
    - A user can use the site as a guest, however they will need to register as a user should they wish to use the user specific functions of the website such as add reviews, make community posts or access the checkout to make a purchase. 
    - The user information will consist of a username and a password, which get stored in the database, therefore allowing for the users information to be retained for future logins.
    - Should a user try to register with a username that is already in the database, then a message will display asking them to choose another username.
    - If the user has clicked on the register page by accident and actually meant to go to the log in page, there will be a link at the bottom that will take the user to the log in page.
- Feature 5 – Log In
    - Once a user has registered, they can click on the log in option on the navigation bar, this will then take them to the log in page that will allow them to log in with their user.
    - If the user has previously registered, they will be able to input their username and password, and once checks have been carried out to ensure that the values of those fields are values stored in the database, then the user will be logged in and redirected to the home page with the option to now add reviews and edit/delete any reviews they may have added, view their account and write messages on the community message area.
    - If the user has clicked on the log in page by accident and actually meant to go to the register page, there will be a link at the bottom that will take the user to the register page.
    - If the user has forgotten their password, they will be able to click the link that says “Forgot password?” and it will take them through the relevant steps to allow them to change their password. 
- Feature 6 - My Account
    - Once a user is logged in, they are able to view their account, from here they will easily be able to see the reviews they have previously placed.
    - They will also be able to see the reviews and community posts they have added to the website, making it easy for them to edit/delete any of either should they need to.
- Feature 7 – Community message area
    - The community message area will consist of a community message board type blog space, which will accessible only to logged in users, and will allow users to make community posts, and to also allow users to comment on posts, whether it be their own, or others.
    - This is intended as a feature to encourage interaction between users of the website, as users can make posts for other users to see, whether this be general chit-chat about a game, or passing on their online ID so other users can team up with them for a gaming session online.
- Feature 8 – Reviews
    - The reviews page will show the reviews that have been added to the site, whether they have been added by the site content creator, or by the users of the site themselves.
- Feature 9 – Add/Edit/Delete Reviews
    - The ability to add/edit/delete reviews will be locked to registered users, and the user will be able to fill out a form containing input text boxes and text areas. When submitted, this information is then stored in the database and displayed on the website for all users to view on the reviews page.
    - The edit and delete functions can only be carried out by users that are logged in, and on the review/s that the user has added to the website themselves. This is to stop reviews being added by one user and then being edited or deleted by a different user.
- Feature 10 – Merchandise/E-commerce store
    - The user will be able to view the merchandise available to purchase from the website, which will show a picture and price of the item available to purchase, allow them to choose the quantity they would like to purchase and then allow them to add said item/s to their cart.
    - From the merchandise page, the user can click on a specific item, and it will allow the user to see a product details page, with a description of said product for the user to read. The user will also be able to add the item to their cart from this page.
    - Users will be also be able to see product reviews left by users that have previously purchased the product the user is viewing, however the ability to add reviews to a product is only available to users that have registered and logged in.
- Feature 11 – Cart
    - The user will be able to see the items they added to the cart with the intention of purchasing, however the user will also be able to amend the cart to edit the quantity or remove an item/items from the cart altogether.
    - The user will then be able to access the checkout from the cart by clicking on the checkout button, however this will take them to a login screen should they not logged in already.
- Feature 12 – Checkout
    - The user will be able to enter their delivery/shipping information and their card details on the checkout page, which will allow them to proceed with their order and finalise their purchase.
    - The checkout will only be accessible if the user has first logged in, so the user will be redirected to the login page if they are trying to access the checkout as a guest user.
- Feature 13 - Log Out
    - When a user decides they want to log out of the site, the option to do so is located on the navbar once the user is logged in.
    - Once the user chooses to log out, they will be taken back to the home page as a guest, with the default nav options available for a guest user (Home, Reviews, Register, Log In, Merchandise, Cart).
#### Future Features
- Feature 1 – Media/Gameplay
    - I would eventually like to add a section that will contain forms of media, ranging from clips of gameplay uploaded by both myself and also other users, to artwork, etc… This could allow for some fun montages, but also allow for the community to share their favourite new creations online with others.
- Feature 2 – Donate
    - I would eventually like to add a feature that will allow any visitors/users to donate whatever value of money they wish to the website to help support new content being made and to grow the brand as a whole.
- Feature 3 – Further expansion on product/merchandise section
    - I would like to implement a feature in future that would allow the user to purchase different sized clothing items (S/M/L/XL) when necessary, currently the items are listed as one size fits all to allow for the products to be added to the cart and purchased without this.
    
### Technologies Used
- Pycharm
    - Pycharm was the IDE I chose to use for this project, and all code was written in Pycharm.
- Justinmind Prototyper
    - Justinmind was used to create the wireframes for the project
#### Front-end technologies/frameworks/languages
- HTML5
    - The markup language used for the project
- CSS3
    - Used to style the HTML
- Javascript/JQuery
    - Used to create responsive/interactive elements, such as the close button for the flashed messages, as well as being required when using the stripe framework
- Bootstrap
    - Bootstrap was used for the CSS framework
- Font Awesome
    - Font Awesome was used to provide the website with suitable icons.
- Google Fonts
    - Google Fonts provided the “Exo2” font used throughout the project.
#### Back-end technologies/frameworks/languages
- Python
    - Python has been used to run the backend of the application
- Django
    - The project uses Django which is a Python Web Framework used as the backend of the project and fulfilling functions such as; connecting to the SQL database, controlling routing and navigation across pages etc.
#### Databases
- Postgres/SQLite3
    - Postgres was used for the database for my deployed project.
    - SQLite was used for the test database, as was used for when the postgres database couldn’t be accessed
#### Version control
- Git & GitHub
    - Git used for version control
    - GitHub used as a remote repository and the hosting of this site
#### Deployment
- Heroku
    - Heroku is used to host the app
#### Payment processing
- Stripe API
    - The project uses Stripe on the front and back end to take users information and process payments

There were also many libraries used in this project, which are available to see in the “requirements.txt” file

### Testing

When carrying out testing on the project, I set up Continuous Integration using Travis, and set up automated testing on models, and views for all the apps. These tests are available to see by looking at the individual “test_“ files set up in each app.

I set up the CI by first creating a .travis.yml file in my project, and then linking my GitHub repository to Travis by adding the build status mark-up that was provided by Travis. Once this was set up, the checks were carried out every time the code was pushed to the GitHub repository.

I also carried out rigorous physical testing locally in Pycharm and on Heroku using Chrome developer tools. On chrome developer tools I tested its functionality on simulated devices, in both portrait and the landscape views. The simulated devices that the website was tested on were:
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5/SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iphone X
- iPad
- iPad Pro
- Responsive

I have also tested the website both locally and remotely on actual devices (rather than just simulated ones on Google Chrome tools), these devices consisted of:
- iPhone 6s
- iPhone 7
- iPad (generation 2)
- iPad Pro 
- Sony Xperia Play
- Multiple desktops (various sizes)

Some examples of the physical testing carried out by myself on certain parts of the site include:
- Link to my Github
    - Scrolled to the bottom of the page
    - Clicked on the text “Martin Crowley - 2020”
    - This loaded up a new webpage that took me directly to my Github user page/repositories
    - Clicking on the github logo also took me directly to my Github user page/repositories
- Links to social networks (facebook/Instagram)
    - Scrolled to the bottom of the page
    - Clicked on the icons for both facebook and instagram
    - This loaded up a new webpage that took me directly those social networking sites
- Logo in the nav
    - Click on the icon at the top of the page on separate occasions
    - When on a different page it redirected back to the home page, when already on the home page, it just reloaded the home page
- Nav links (user not logged in & user logged in)
    - On both desktop and mobile, the hamburger button rendered perfectly. I clicked on the hamburger button in the top right of the screen, then clicked on each link in the sidenav and each link took me to the relevant page.
    - When log out was clicked, I was logged out and directed back to the home page as a guest user.
- Register
    - When testing the register page, I initially tried registering with a username and email that I knew hadn’t previously been used. I also used the same password in both boxes, and upon submitting the form, I was redirected to the home page and a flashed message informed me that I had successfully registered.
    - When trying to register with a username that I knew had already been, the register page reloaded and displayed an error message that informed that “A user with this username already exists”, therefore this was working as it should as it was informing the user that there was another user in the database with that username, and so the user would know to try a different username.
    - When typing a username in the username box, but leaving the password box empty, upon clicking “create account”, it informed me to “Please fill in this field” underneath the password input.
    - The same also happened when I typed in a password, but didn’t input a username, the form would not submit, and the message was displayed again.
    - Also tested the password field by making it shorter than the requirements for the field (8 characters for password), and when trying to submit the form, it informed me that the password was too short and required 8 characters.
    - Also tested the link at the bottom of the page, which successfully redirects to the log in page.
    - When already logged in and trying to access the register page by typing it into the URL, I was returned to the home page and a message was flashed that I had to log out first to try and register a new user
- Log In
    - When testing the log in page, I initially tried logging in with a username that I knew had previously been registered, and the correct password that coincided with the username. Upon submitting the form I was redirected to the home page, and a flashed message informed me that I had successfully logged in.
    - I then tried to log in with a username that I knew hadn’t been registered yet, and therefore didn’t exist in the database. This reloaded the log in page and displayed a flash message that informed me that “Your username or password is incorrect”. In this situation I knew it was because the username didn’t exist as it hadn’t been registered yet, however the error will also display if the user has spelt their username wrong, or if the password doesn’t match the password that is saved against that username in the database.
    - When typing a username in the username box, but leaving the password box empty, upon clicking “log in”, it informed me to “Please fill in this field” underneath the password input.
    - The same also happened when I typed in a password, but didn’t input a username, the form would not submit, and the message was displayed again.
    - Also tested the link at the bottom of the page that says “Not registered yet? Click here…”, which successfully redirects to the register page.
    - When already logged in and trying to access the log in page by typing it into the URL, I was returned to the home page and a message was flashed that I had to log out first to try and log in as another user
    - I also simulated forgetting my password, and tested the password reset function, and every stage of this worked as was expected and allowed me to reset my password.
- Pagination
    - The pagination used on the reviews, the merchandise and the community pages works perfectly and allows for a maximum of 6 items to be displayed per page, and the user can change between the pages at their own leisure. At the time of testing, there were 10 products on the site, so there were two pages available, on the first page there were 6 products, and on the second page there were the remaining 4.
- Search
    - The search function was used on 3 different pages, these being: the reviews page, the merchandise page and the community posts page.
    - I used filters for each page to return the results based on what is entered into the search bar. This was tested extensively, with me testing each of the pages individually.
    - On the reviews page, I tried 3 different types of searches: using the name of a game, the platform/console, and the score the reviewer has given. So for example, I could type in “the last of us” and it would return all reviews for games called the last of us, alternatively I could also search for all reviews on PS4 games, or all reviews that gave games a score of 9.
    - On the community page, I tried 2 different types of searches: using the name of a post and using the name of a user that had written posts.
    - On the products page, I tried 2 different types of searches: using the name of a product, and using the price that I wished to find products at (minus the £ sign).
    - When clicking the search button without writing anything in the search bar, it would return ALL the results. For example, it would return all of the reviews and display then on a single page.
    - When clicking Cancel, it returns the user to the initial page prior to any searches being carried out.
- Merchandise store
    - The merchandise store uses cards to display the products available to purchase, on each card you are able to see an image of the product, the name of the product and the price of the product. You are able to change the quantity of the product you wish to add to your cart (with a minimum of 1, and a maximum of 999), then consequently add that quantity of the product to your cart. This feature can be used whether you are logged in or not.
    - I removed the number from the quantity field (so it was empty) and tried to add this to the cart, and this resulted in an error-500 page being displayed. The error-500 page gave me a link to click on that returned me to the previous page. This was a nice quality of life addition, as nothing would have broken the immersion more than if the user was displayed a blank white server error page.
    - The pagination at the bottom of the page allows you to change between the pages of products, which at the time of testing was 10 products, so there were 2 pages, with 6 on the first page, and 4 on the second page.
- Product details
    - When clicking on the name of the product, it would take me to the product details page, here I was presented with: a button that would return me to the merchandise store, a larger picture of the item, the name of the item, the description of the item. On this page I was also able to change the quantity of the item I wished to add to my cart, and then add that amount to the cart.
    - On this page I was also able to click the “Review the product” button, and this would redirect me to the product review form. Once this form was filled out, it is checked that it is valid (no fields left empty) and if it passes these checks it can be submitted, and will then appear at the bottom of the product details page. When carrying out testing, reviews were left by myself and multiple other users.
    - It is important to note that reviews can only be left by users that are registered and logged in, the review can also be deleted from the product reviews, but only by the user that left the review.
- Reviews
    - The reviews section uses cards to display the reviews that have been submitted for the users to read, on each card you are able to see the name of the game being reviewed, the platform that the game was on, the score the reviewer gave the game, and a link the user can click to actually read the review.
    - Upon clicking this link it loaded a new page that displayed all the information for that specific review, including: the games name, the author of the review and when they wrote it, the platform the game was on, the review itself, and the score given to the game.
    - There was also a link at the top left of the page that when clicked, took me back to the reviews page, at which point I could then choose to read another review if I wanted.
    - When viewing a review that I had written, at the bottom of each of the submitted reviews there were two buttons that would allow me to edit or delete the review, both of these links worked and would allow me to either edit the review, or delete it from the site/database.
    - When viewing a review that had been submitted by a fellow user, I could see all of the information for the review, but the buttons for edit and delete were not present (because I was not the one that wrote the review).
- Add a review
    - I first tried accessing the add a review page whilst not logged in, and it wasn’t possible, as it wasn’t available on the nav, and if I tried entering the url for the add a review page, then I would be redirected to the login page. This was working as planned, and allows for accountability for when people leave reviews but it also allows for credit to be given to the user that submitted the review.  
    - When filling in the add review form, I tried to submit the form with all of the fields left empty, it wouldn’t allow me to and would show a message under the top most field that said “Please fill this field”. I then filled the top field and tried submitting again and the same thing happened. This occurred with each field until every field was filled, and only once each field was filled and the form was valid, could it then be submitted.
    - If all required fields were filled, but the score that was given wasn’t a number between 1-10, then the form wouldn’t submit and would show a message saying that I had to ensure the value was less than or equal to 10.
- Edit a review
    - As with the add a review page, the ability to edit a review could only be accessed if certain conditions were met. These were that I was logged in, and that I was the user that had added the review in the first place.
    - This was working as planned, as it prevents other users going on the site and being able to unfairly edit someone else’s view. It was important to ensure this as it makes it fair on everyone, but also allows for them to have a voice and review a game, without having someone disagree with their view and be able to edit the review they submitted. 
- Delete a review
    - As with the add and edit review, the ability to delete a review could only be accessed if certain conditions were met. These were that I was logged in, and that I was the user that had added the review in the first place.
    - This then worked as planned, I could both delete reviews I had added using the review’s own page and clicking the delete button, or through my user account page, that allows you to click the links to view/edit/delete, using this method works well and allowed for me to remove the review I had added.
- Community Posts
    - The community section is locked to users that aren’t registered and logged in, so I firstly tried to access this whilst logged out, and not only is “Community” not in the nav links, but it also couldn’t be accessed by typing the url for the community page.
    - Upon logging in, I was suddenly able to click the link for community, and it loaded the community page. Once it had loaded I could see the intro paragraph explaining the page, but also a button that allowed the adding of community posts, the search bar and relevant buttons, as well as various community posts and pagination at the bottom of the page that limited the posts per page to 6, and could be used to access the other posts.
    - Each post shows the post’s name, the author of the post and the date they posted it. It also shows a truncated version of their post, as well as the number of comments that the user has on their posts.
    - When clicking on the name of the post, it took me to the post’s details page, so I could see the name of the post, the authors name and date the post was made, as well as the full post that had been submitted.
    - When viewing posts I had written, there was two buttons: “edit post” and “delete post”. However when viewing posts I had not written, the buttons did not appear, this was to ensure that only the user that had made the post could edit/delete it.
    - When I clicked edit on the post I had previously created, it took me to the edit post page, and got the post using it’s id and pre-filled the fields of the post form with the data that already existed for that post. I then tried clicking the cancel button, which used javascript to go back one page using the webpage history. Upon clicking edit again, I was able to add some additional text to the post and even rename the post, and upon clicking post, it changed the original data saved for that post in the database and on the website.
    - To test the delete function, I made a dummy post and then clicked on the post to view its post detail page. Once I’d loaded this, I clicked delete post, and the post was removed from the database and the website.
- Add comments
    - When viewing a post I had written, or one that another user had written, I was able to press a button midway down the post’s page that said “Add comment”. Upon pressing this I was taken to another screen that had a text box I could write in, and when I had written a comment and clicked send, it would then post the comment below the post in the Comments section.
    - Once I’d written and sent the comment, it was available for all other logged in users to see. I then decided to test the delete comment function, and upon deleting my comment I was returned back to the community screen. This was implemented purely for if a user had replied to another user or made a comment that they no longer wished to remain posted to the post’s comment section, and so it removes the comment from the database and works as desired. 
- Cart
    - After adding any items to the cart (using the merchandise store) the nav button could be clicked at any time and the cart showed exactly how many items were currently in the cart.
    - Upon clicking on the cart in the nav, I was taken to the cart page and I was able to see the items that had been added into my cart. I could amend the number of each item in the cart, which could be lowered or raised to any number ranging from 1 to 999. If I decided I didn’t want the item anymore, I just lowered the item quantity down to 0, and upon clicking “Amend” it would remove the item from my cart altogether.
    - At the bottom of this page it showed the total price for all of the items in my cart, and when I was happy with the items currently in my cart and I wished to purchase said items, I would click the checkout button and this would take me to the checkout.
    - I also tried removing all items from my cart, and when I had no items in my cart there would be a message displayed on the screen that informed me of this and would provide a link to go to the merchandise store.
    - When the cart was empty the checkout button (when clicked) would just take me back to the cart, and would only take me to the checkout once an item was actually in the cart.
- Checkout
    - On the checkout page I was able to see the items I had put in my cart with the intention of purchasing. Below this was the Payment Details form, which consists of 2 parts: the Delivery Info, and the Payment Info.
    - All fields must be filled out, and there are form messages that display when you try to submit the form whilst leaving fields blank (the exception to which is the Street Address 2 field, as many people don’t have a 2nd line to their address).
    - Once all form fields are filled in with valid information, I was able to submit the form. I was then returned to the home page and a flashed message informed me that my payment had been successful.
    - I then clicked onto my account, and at the bottom of my account page I was able to see that my order had gone through.
- Your Account
    - When clicking the “Your Account” nav link, I was taken to my user account page, which contained a message to the user and explains what they will find on the account page.
    - The subsections on the page (reviews, posts and orders) were all collapsible by clicking on the relevant heading for that section.
    - I checked the reviews and posts sections by clicking on the view, edit and delete links for the reviews and posts that I had submitted previously, and these all carried out the relevant functions they were implemented for.
    - In the orders section at the bottom of the page, my previous ordered items were displayed, with the order ID they corresponded to, the order date, the product and the quantity that had been purchased.
- Home
    - The home page displayed a different welcome message depending on whether I was logged in or not. The links on the home page all went to the relevant pages on the website, with the exception being the link for the community page, which would take guest users that hadn’t yet registered/logged in to the login page instead (as the user is required to be registered and logged in to access the community page)
- Log Out
    - When clicking “Log Out” from the nav, I would be logged out of my account and a flashed message would pop up at the top of the screen informing me that I had been logged out. I would also get returned to the home screen whenever I chose to log out.
- Stripe
    - Once I had completed the checkout stage and had been told the payment was successful, I logged into stripe to check that the payments were going through, and each order that was going through was registering on stripe. Therefore confirming that the checkout was working and the users order and payment was being processed correctly.
    
- Family & Friends Testing
    - Once the application was up and running, I asked 3 of the members of my family, my girlfriend and 2 of my friends to register and test the site.
    - They said that it was intuitive and easy to use, and that they had no issues with working out what to do or how to use certain functions on the site. They all created reviews/posts, reviewed an item on the store, added items to their cart and then subsequently went to the checkout and carried out the purchase of what had been added to their cart.

The devices my friends and family tested on were: 
- iPhone 6s
- iPhone 7
- iPhone X
- iPad Pro
- Various desktops

#### Carrying out tests
If you are wishing to test the various functions of the website, you can register and login using said registered user account, or alternatively you can log in and use the account that I have made for test purposes, wherein you are able to see the reviews, posts and purchases made in the “Your Account” page. You may add new reviews, comments and posts as this user (which you can then edit and delete if you want to test that functionality), but please do not edit or remove any content that was added using this user initially as it was added to demonstrate the various functions available to the user (please note that the reset password function can only be accessed if you register your own user, as it will require you to have access to the email account that you enter).
- USERNAME: BearNationUser
- PASSWORD: letsgame123

Also, when entering card details in the checkout, ensure you don’t use your actual card details.
- For the card number use: 4242424242424242
- For the cvc, you can use any 3 numbers
- The expiry month/year can be any valid month/year combination

### Deployment

My application was coded in Pycharm. Once I had created the workspace in Pycharm for my project to be built in, I then went into the terminal used the Command Line Interface command “git init” to create a local Git repository.

Once I had done this, I was then able to use git commands in the CLI at various stages to add changes I had made within the workspace, to the staging area (storing files is a 2 step process). This was done using the command: ‘git add ‘which could be followed with the specific file name/s that needed to be added to the staging area (prior to being committed to the repository). Alternatively, when there was a few changes that could be added all at once, the command was followed by a full stop (‘git add .’)

Once changes had been added to the staging area, they then needed to be committed (the 2nd stage of storing files) to the repository using ‘git commit’. However with each commit, I also included a message that explained the reason for each commit to the repository. This was done by using the command: ‘git commit –m “TEXT GOES HERE“ ‘

Now I had the local repository, yet I needed to form a link between my local Git repository and GitHub. So I went onto GitHub and created a repository for my milestone project, I then had to link the local repository to the GitHub repository, which was done using:
- git remote add origin https://github.com/Mcrowley93/bear_nation_gaming.git
- git push -u origin master

At this stage, the local Git repository could then be synced with the repository on the GitHub server, which was achieved by using the command: ‘git push’

Once the project/website was in the dedicated GitHub repository, I had a few other steps that I carried out, including: setting up my S3 bucket and custom storages, so that my static files(css, js and images) would be stored and fetched from the S3 bucket. I set up the email backend using one of my email addresses to send emails, this allows for users to receive the email when trying to reset their password. I also used the STRIPE API, which once it was set up was used to handle payments at the checkout.

Prior to deploying the project to heroku, I also had to update my requirements.txt file to ensure the project’s dependencies list was up to date, as well as having to create a Procfile, which is a simple text file stored in the root directory of the project that describe the components required to run the application. At this point I then went to the Heroku dashboard and created a new app called “bear-nation-gaming” with Europe as its region. Once the app was created I clicked on Resources and in Add-Ons I chose Postgres which created a postgres database (the url for which was added to the config variables by Heroku), following this I went to settings and had to set the many project Config variables including: AWS Keys, Stripe Keys, Email information, Secret key, and DISABLE_COLLECTSTATIC (which had to be set due to using S3 buckets to store the static files, etc…). I also had to tell the project to use the new postgres database that heroku had set up, as well as running “makemigrations” (which should be up to date anyway), “migrate” and then “create superuser” (so that the admin panel may be accessed).

Once these steps were complete I could click on the Deploy tab in the Heroku app dashboard and use the Github deployment method which connects the app to my Github repository, I then turned on automatic deploys, so any changes made to the project that are then pushed to my Github repository are automatically updated on the application once live. All that was left to do was to manually Deploy Branch, this allows you to see a build log for the app being made, but once this step was done the app was deployed on Heroku and was able to be opened and used.

### Credits
#### Content
Code for the database website/app was written by myself with knowledge I’ve picked up from the code institute course.
#### Code used from others
Code to allow accounts to login with both a username OR an email was adapted from: https://www.youtube.com/watch?v=c7PqMsQiWKU

Help creating the post models/views from: https://tutorial.djangogirls.org/en/django_views/

Help creating the comment model was from: https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/

#### Media

Black-ps4-controller: (taken by Garrett Morrow)
https://www.pexels.com/photo/4k-wallpaper-black-black-background-console-1647369/

ps1-classic: (taken by Marco Verch)
https://www.flickr.com/photos/160866001@N07/45478228054

metallic black ps4 contoller:
https://www.piqsels.com/en/public-domain-photo-oijkz

red-ps4-controller:
https://www.piqsels.com/en/public-domain-photo-ijxqq

black-beanie:
https://pxhere.com/en/photo/10622
 
Logo images -
- Bear-icon:
https://svgsilh.com/image/2660867.html
- Ps4-controller-icon:
Author: needforbleed
https://opengameart.org/content/ps4-controller-icon  

Background Image:
https://www.wallpaperflare.com/black-sony-ps-dualshock-4-wallpaper-186197/1366x768

The above URL was used for the background image on the site.

It is taken from a website called “Wallpaper Flare”, which is a royalty free site, and it was free to use. 
All other images used were royalty free, but I included links for the images so others may be able to locate and use them.  

### Acknowledgements
- Spencer Barriball - My Code Institude assigned mentor, for his invaluable knowledge, guidance and advice.
- Daniel Kew (LemonGhost) – who wrote the review for breath of the wild for me to use with my projects during the CI course.
- My family – For their patience and understanding and for supporting me when I came to bumps in the road.
- All the people that helped to test my website and gave valuable feedback.
