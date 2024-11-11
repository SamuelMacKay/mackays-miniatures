# Mackay's Miniatures
MacKay's Miniatures is a platform that sells and distributes Warhammer Miniatures, for warhammer 40,0000 and Age of Sigmar.
The website will have an easy navigate navbar, and search engine so you can find what you are looking for easily.
An account page will let the users save their details, delivery address and view their previous purchases.


![Responsive Mockup](media/responsive-mockup.png)

## User Stories 
|Story No.|Story|
| ------------- | ------------- |
|1| As A first time user, <br> I want to be able to find what i am looking for with ease <br> So I can buy what I am looking for <br><br> I know I am done when I have an easy to use NavBar and an effective search engine that allows you to filter out specific items, and a sorting system |
|2| As the Site Owner, <br> I want to have a site that has secure payment methods <br> So first time and repeat buyers feel comfortable purchasing from me, <br><br> I know I am done when I have a secure payment method that is reliable and looks professional |
|3| As A returning Customer , <br> I want to be able to see my previous purchases, save my delivery and payment details <br> So I can buy from the provider again with ease and without adding in all the info ever time.  <br><br> I know I am done when I have an account system that when logged in will save the delivery address location and payment method to auto fill. |
|4| As the Owner of the site, <br> I want to have an easily identifiable notification on all New Releases and Pre Orderes <br> So potential customers can see what is the newest products and be excited by them <br><br> I know I am done when I have an icon that stands out and identifies the specific product as New or Pre-orderable.|
|5| As A potential buyer , <br> Iwant to be able to see whats in my shopping cart and be able to edit them, remove them or increase how many i want <br> So I dont have to navigate away from the buy page to edit what im buying <br><br> I know I am done when i have a page for displaying shopping bag contents and lets me edit what is in it.|

***

## Wireframes
Below are the designs that I can use to build the site. I have used the user story numbers to link where I can meet the goal in my design. This will help me to think about the users needs as I build the page.

### Home Page Design<br>
User Story Number -  <br>
![Home Page Design]()


***

## Features

### Existing Features

- __Navigation Bar__

  - 

![Nav Bar]()

- __Home page__

  - 

![Home Page]()



### Features Left to Implement

- a way to rate reviews
- have comment board/forum


## Testing

This is a sample of shots of what the site looks like on different devices. 

#### Desktop
|Firefox 128.0.2| Chrome 127.0.6533.72/73 / 23 July 2024|
| ------------- | ------------------ |
|![firefox home page]()|![chrome home page]()|


| Firefox 128.0.2 medium | Chrome 127.0.6533.72/73 / 23 July 2024 medium |
| ------------- | ------------------ |
|![firefox home medium]()|![chrome home page medium]()|


| Firefox 128.0.2 small | Chrome 127.0.6533.72/73 / 23 July 2024 small |
| ------------- | ------------------ |
|![firefox home small]()|![chrome home page small]()|

#### Mobile

##### Safari iOS Phone 17.5
| iPhone home page |
![iPhone home page](media/mobile-home.JPG)

### Validator Testing
- HTML
    - home.html: No errors were returned when passing through the official W3C validator [validation]()|<br> 

- CSS 
    - style.css: No errors were returned when passing through offical Jigsaw validator ![]()|<br> 

- JS 
    - script.js: No errors were returned when passing through offical Jigsaw validator ![]()|<br> 

    - password_validate.js: No errors were returned when passing through offical Jigsaw validator ![]()|<br> 

- Python
    - app.py:  No errors were returned when passing through CI Python Linter ![]()<br>

### Manual Testing
- I have tested that this page works in different web browsers.
- I have tested that the project is responsive and works with different device sizes. It looks good and functions as normal. 
- I have tested all links, internal and external. They go to the correct destination and open in the correct way. 
- I have tested that all text and fonts are readable and easy to understand.
- I have asked my partner to use the website to see what a first time user would experience.

### Bugs
#### Bug 1
- 

Old code:
```

```
New code:

```

```

### Unfixed Bugs
 -

### User stories Testing
|Story No.|Result|Story/ Evidence|
| ------------- | ------------- | ------------- |
|1|<font color="green"></font> | <br><br> Evidence: <br> ![]()|
|2|<font color="green">Test Pass</font> | <br><br> Evidence: <br><br> ![]()|
|3|<font color="green"></font> | <br><br> Evidence: <br><br>![]()||
|4|<font color="green"></font> | <br><br> Evidence: <br><br> ![]()|
|5|<font color="green"></font> | <br><br> Evidence: <br><br> ![]()|

### Accessibility Testing

To check the colors and fonts, I used Lighthouse in the Google devtools. The results are shown below:

| Home  |
| ------- |
| ![lighthouse result home page](media/get_reviews-lighthouse.png) |

## Deployment

### Cloning & Forking
#### Fork
1. On GitHub.com, navigate to the [SamuelMacKay/mackays-miniature](https://github.com/SamuelMacKay/mackays-miniatures) repository.
2. In the top-right corner of the page, click Fork.
3. By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
4. Add a description to your fork.
5. Click Create fork.

#### Clone
1. Above the list of files click the button that says 'Code'.
2. Copy the URL for the repository.
3. Open Terminal. Change the directory to the location where you want the cloned directory.
4. Type git clone, and then paste the URL
5. Press Enter.

### Local Deployment
1. Sign up to [Gitpod](https://gitpod.io/)
2. Download the Gitpod browser extension.
3. On GitHub.com, navigate to the [SamuelMacKay/mackays-miniatures](https://github.com/SamuelMacKay/mackays-miniatures) repository.
4. Above the list of files click the button that says 'Gitpod'.

### Remote Deployment 
 The prgoram was deployed to Heroku. If you have forked/cloned the repository the steps to deploy are:
 1. On Heroku, create a new app.
 2. input a name for your app
 3. Click on the settings tab
 4. Scroll to the Config Vars and click on the "Reveal Config Vars"
 5. Input CREDS into the key field and the content of the Google API creds file into the value area.
 6. Add another config, PORT into key and 8000 into value.
 7. Set the buildbacks to Python and NodeJs in that order .
 8. Link your Heroku app to you repository.
 9. Click on Deploy.
 10. The page will then provide the url to the python terminal.

 The live link can be found here - []()

## Credits
  
### Content
- Processes from the CI task manager mini project was used to help create this website - [Task-Manager-Mini-Project](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main)

- HTML, CSS and Javascript code help was taken from w3schools - [W3Schools](https://www.w3schools.com/)

### Media

#### Icons
- All page Icons - [Font Awesome](https://fontawesome.com/)
- home page image - [Warhammer Artwork](https://www.goodfon.com/games/wallpaper-download-1920x1120-dark-imperium-warhammer-40-000-box-cover.html)
