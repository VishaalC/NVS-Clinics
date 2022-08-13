# NVS-Clinics
Dynamic website built using HTML, CSS, Bootstrap, SQL and a bit of JS.

This project is a website used to book appointments and other tasks present in a commercial a. The implementation is fairly is simple, to keep the project scope in check.

Technologies used:

- Python
- Flask web-framework
- SQLite
- Bootstrap
- Twilio API(for sending messages)
- ICD API(to lookup diseases)
- HTML, CSS and JS

## How does the webpage works?

The visitor can either register as a new patient or as a returning patient. After logging in or registering, you can request an appointment and recieve an SMS (to twilio verfied numbers only) confirming your booked appointment.

You can also lookup various diseases and get their ICD code and a short description explaining what the disease is. The website uses sessions to keep track of logged in users so you don't have to keep loggin in repeatedly.

### Routing
The site has multiple routes each performing a specific action, such as logging in, registering, booking appointments and looking up diseases.

### Sessions
The site keeps track of the logged in user's name and their email address thus improving the user experience.

### SQLite database
The site has a backend as well, storing the patient details in order to use them when it is required such as when booking an appointment.

### Possible improvements
- Adding a chatbot that diagnoses based on the symptoms you provide.
- Improving website UI.
- Improving website UX.
- Adding a login for doctors and other staff.

### How to launch the website
The website is hosted on heroku so all you have to do is click this link [NVS-Clinics](https://nvs-clinics.herokuapp.com/)

Video link -> [link](https://youtu.be/spHN9mPrWac)

### Brief description of flask
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.

Applications that use the Flask framework include Pinterest and LinkedIn

### Brief description of bootstrap
Bootstrap is an HTML, CSS & JS Library that focuses on simplifying the development of informative web pages (as opposed to web apps). The primary purpose of adding it to a web project is to apply Bootstrap's choices of color, size, font and layout to that project. As such, the primary factor is whether the developers in charge find those choices to their liking. Once added to a project, Bootstrap provides basic style definitions for all HTML elements. The result is a uniform appearance for prose, tables and form elements across web browsers. In addition, developers can take advantage of CSS classes defined in Bootstrap to further customize the appearance of their contents. For example, Bootstrap has provisioned for light- and dark-colored tables, page headings, more prominent pull quotes, and text with a highlight.
