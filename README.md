# EventHive

Eventhive is a concert/event management database ,created for the purpose of college project,The eventhive web application can register the uses data for booking tickets for various events and concerts hosting currently

The web app was created using python Flask framework and sqlite for the backend database 

and due to less time for the  project basic html and css was used for the frontend <br>


![](https://img.shields.io/static/v1?label=Flask&message=db&color=<COLOR>)
![](https://img.shields.io/static/v1?label=Python&message=3&color=<red>)
![](https://img.shields.io/static/v1?label=sqlite&message=db&color=<COLOR>)

![landingpage](https://user-images.githubusercontent.com/98420696/213472814-0c833d38-25ed-4b49-99a3-a537ba048e10.png) <br>
![event](https://user-images.githubusercontent.com/98420696/213472876-4ee2d380-e9bb-40d7-aa61-ca556c7eb8d4.png)<br>
![tickets](https://user-images.githubusercontent.com/98420696/213472905-62044494-58e7-44d3-a621-758a5d11c75e.png) <br>
![registration](https://user-images.githubusercontent.com/98420696/213472999-3a4b77d1-09ed-4bdc-80d0-1346eacf2911.png) <br>
![table](https://user-images.githubusercontent.com/98420696/213473091-5424cbd8-bfe9-43a4-82e1-37782beede7e.png) <br>

## Requirments
>Python <br>
>flask <br>
>flask_sqlalchemy <br>
>sqlite <br>
>HTML <br>
>CSS <br>

## Instructions for running the applications
>open vs code terminal and type
~~~
pip install flask
~~~
~~~
pip install flask_sqlalchemy
~~~
~~~
pip install SQLAlchemy
~~~
<p> Then u can download the files from here and open it in vs code</p>

**important point to be noted**
>The database file should be deleted and created again , to do that open terminal and type(Delete the existing .db file first)
~~~ 
    from app import app
    from app import db
    db.create_all()
    exit()
~~~
By doing this a new db file will be created

next run the app.py file and open the localhost shown in the terminal

**THANK YOU !**







