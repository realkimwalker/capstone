# FINAL PROJECT
#### Distinctiveness and Complexity - My project is completely different than the assignments given in class, and other than the usage of methods in Django and JavaScript, bears no resemblance to the source code, look, or feel of the lessons and the completed assignments. I created an election polling app which reflects the current environment of the 2024 presidential elections. I also used a couple new features (new to me, but not necessarily new to experienced coders!) not shown in class that I read in the documentation, which were recommended to use only after doing it the way we learned in class. I will outline these in detail the below paragraphs.

### I made sure to include a requirements.txt file. I found a python command called Freeze, which will autogenerate a requirements file for your program, once you have completed it. It also automatically places it at the root level, where manage.py is. I had to remind myself that requirements is a root-level file, not to be namespaced, like other app=specific files are. I found the Freeze python command to be helpful when building apps, or more complex programs. Freeze will also include the actual release date of the libraries in requirements, which I hadn't thought to do on my own.

### It was important to me to be able to configure all of the back end components together. I really enjoyed learning about the admin feature in class. All of the setup and configuration was the same as on other projects, except that I found the timezone in settings. What is distinct is that I developed a few different features in my admin view that include updating or timestamping date and time with a button, tabular view of different menus (Questions and Choice). I added different filtered views of the content.

### I created models, views, urls, which is all necessary for a functioning app. Making sure that I did not hard code any routes was similar to class, but I did remember to keep things loosely routed and passed in variables. I also learned  Django shortcuts from the documentation such as a ListVeiw and DetailView which have been included with Django. I used these after writing the code the way we learned in class just to see if I could get it working. It worked, so I kept it in as it was my goal to make sure I could create distinctions and show continued learning for my final project. I also made use of Django's utilities, again built-in functionality is often faster and has optionality built-in. I think that for the next steps, I would like to explore how to make the apps reusable. Ultimately, reusability saves time and creates more time for building greater programs.

### I did include testing in my apps (in tests.py) . My tests catch make sure that only polls based on recent questions are taken. I also tested that no questions appear if the time at a future date than the current time, and that a 404 error is displayed in the date is in the future. I tested to make sure that the index page could display multiple questions for users to vote upon. I also tested my tests, rewriting code with forced errors, and debugging until all tests passed. My testing code was longer than a lot of my other files.

### I tried to keep my .html files to a minimum, using the an index and detailed view to go with the Django shortcuts ListView and Detailview. Since we are focused on using JavaScript and Django, my efforts were most building front and back end with less html-based structure and more functionality from Django and JavaScript. I was able to add filters to all of the added questions, so that the admin can search the archived questions by day, week, month, year. The shortcuts built into Django make faster to build in complexity.

### I did have templates, static, and an app folder, added as necessary, and I did follow the namespacing methodology recommended in Django docs. At times, namespacing does get confusing just having extra folder layers that are named the same, but it clears things up for the program to run smoothly.

### To run the polls application: First, download the "capstone" folder from my submitted project. Next, change directories into the capstone directory (using the python command: cd capstone). Then, just as we learned in class with the last project, create migrations using the command: python manage.py migrate. Last, you will run the server, with the python command: python manage.py runserver. This last command will return the server link for you to view the app. It will land on the index page, and you can start polling. If you want to explore the admin interface, you will have to first create a superuser, using the python command: python manage.py createsuperuser, and following the instructions. If you want to run my tests, then you will use the python command: python manage.py test polls.

### Thanks for visiting my app, and for your dedication to CS!!
