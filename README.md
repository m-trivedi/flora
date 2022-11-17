# Flora
A Python PyQT5 application that makes counselling services more accessible in over 10 schools

### The Homepage
The screenshot below shows the home page of the application. The application contains several pages that act like components. These components can either be brought up or pushed down in the z axis (through the screen). This enables the feature of switching between pages. Buttons trigger functions that perform these actions.

<img src = "https://raw.githubusercontent.com/m-trivedi/flora/main/screenshots/flora-1.png" style = "height: 400px;">

### The Login Page
The screenshot below shows the login page of the application. The application communicates with a MySQL backend and checks if the entered user credentials are correct. If they are, the authentication of the user is set to true and other user information such as assigned counsellors, assigned school, classmates are brought up.

<img src = "https://raw.githubusercontent.com/m-trivedi/flora/main/screenshots/flora-2.png" style = "height: 400px;">

### The Home Page
After logging in, the user is shown the home page. The home page helps navigate other aspects of the application and also displays the upcoming meetups for the user.

<img src = "https://raw.githubusercontent.com/m-trivedi/flora/main/screenshots/flora-3.png" style = "height: 400px;">

### The Meetups Page
The meetups page displays the current, or past meetups that were scheduled by/for the user. It also displays the open meetups which have not been scheduled but have been requested.

<img src = "https://raw.githubusercontent.com/m-trivedi/flora/main/screenshots/flora-4.png" style = "height: 400px;">

### The Request Meetup Page
The request meetup page allows the user to either request a meetup for himself or request a meetup for another user. After requesting a meetup, a counselor will accept the meetup and will schedule a time for the meetup.

<img src = "https://raw.githubusercontent.com/m-trivedi/flora/main/screenshots/flora-5.png" style = "height: 400px;">

### The People Page
The people page displays the students, counselors at the institution. The page also includes the username of users that is used to request meetups.

<img src = "https://raw.githubusercontent.com/m-trivedi/flora/main/screenshots/flora-6.png" style = "height: 400px;">

### The Stats Page
The stats page displays the statistics regarding meetup frequency of different counselors. The statistics are displayed using different charts, such as a pie chart, line chart, or bar chart.

<img src = "https://raw.githubusercontent.com/m-trivedi/flora/main/screenshots/flora-7.png" style = "height: 400px;">

### The Settings Page
The settings page helps users change their password and view their account information.

<img src = "https://raw.githubusercontent.com/m-trivedi/flora/main/screenshots/flora-8.png" style = "height: 400px;">

## Software and Libraries
This project uses the following software and Python libraries:
* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [PyQt5](https://pypi.org/project/PyQt5/)
* [pandas](http://pandas.pydata.org/)
* [mysql.connector](https://pypi.org/project/mysql-connector-python/)
* [matplotlib](https://pypi.org/project/matplotlib/)


