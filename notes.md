SQL access: sqlite3 db.sqlite3

-------------------------------

Python Shell Access:

Python 3.4.3 (default, Nov 17 2016, 01:08:31) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from tickets.models import Features
>>> a = Features.objects.all()
>>> a
<QuerySet [<Features: Mo's Feature>, <Features: Feature 1>, <Features: Test Feature 3>]>
>>> a[0]
<Features: Mo's Feature>
>>> a[0].title
"Mo's Feature"
>>> for item in a:
...     print(item.pk, item.title)                                                                                                                                                                                                
... 
1 Mo's Feature
2 Feature 1
3 Test Feature 3
>>> for item in a:
        return(item.pk, item.title)
        
        