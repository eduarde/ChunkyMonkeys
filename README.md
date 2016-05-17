# ChunkyMonkeys
Hackathon project

1. Install Python 3.5

2. Clone the project

3. Create a virtual environment under ChunkyMonkeys project:

    Windows: 
      python -m venv myvenv

    Linux & OS X:
      python3 -m venv myvenv
      
4. Activate the virtual environment:

    Windows:
      myvenv\Scripts\activate
      
    Linux & OS X:
      source myvenv/bin/activate
      
5. Install required modules:
  
    Django: pip install django~=1.9.0
    
    Widget Tweaks: pip install django-widget-tweaks
    
    DatetimeWidget: pip install django-datetime-widget
    
6. Run: python manage.py migrate 

7. Create super administrator: python manage.py  createsuperuser
8. Start server: python manage.py runserver
9. Test the application:  http://127.0.0.1:8000/
