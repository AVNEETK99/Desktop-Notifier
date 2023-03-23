# Desktop-Notifier

A desktop notifier is a software application that displays notifications on the user's desktop, usually in the form of pop-up windows or messages. These notifications can inform the user about important events, such as new emails, incoming instant messages, upcoming appointments, and system updates. Desktop notifiers are often used by users who want to stay updated on their notifications without having to constantly check their email or messaging apps. They are also useful for applications that need to notify the user of important information, such as task management tools, to-do lists, and news aggregators.

## Instructions to run the game

* Open the Github repository where the game code is hosted.

* Click on the green "Code" button and then select "Download ZIP" to download the code as a ZIP file.

* Extract the ZIP file to a folder on your computer.

* Open a command prompt or terminal window and navigate to the folder where you extracted the code.

* Type ```python basic_notifier.py``` and ```python advanced_notifier.py``` . Press Enter to start the game.

* Follow the prompts to play the game.

## Functionality of the code

### Basic :
* This code imports the notification function from the ```Plyer module```.

* The code creates two variables, ```title``` and ```message```, which contain the content of the notification.

* The code then calls the ```notification.notify``` function, passing the ```title``` and ```message``` variables as arguments.

* The ```app_icon argument``` is set to None, which means that no icon will be displayed with the notification.

* The ```timeout argument``` is set to 10 seconds, which means that the notification will disappear after 10 seconds.

* The ```toast argument``` is set to False, which means that the notification will not be displayed as a ```toast notification```.

### Advanced :

This code imports three modules: ```datetime```, ```time```, and ```requests```. It also imports the notification function from the ```Plyer module```.

The code tries to retrieve COVID-19 data from a ```web API``` hosted on ```"https://corona-rest-api.herokuapp.com/Api/india"```. If the request is successful, the data is converted into a ```JSON format```, and the loop is executed. If the data is not fetched due to lack of internet, the code prints ```"Please! Check your internet connection".```

The loop repeatedly executes the notification function every 4 hours. The notification contains the COVID-19 statistics for India for the current date, including the ```total number of cases```, ```the number of new cases for the day```, ```the number of new deaths for the day```, and the ```total number of active cases```. The notification will stay for ```50 seconds```.
