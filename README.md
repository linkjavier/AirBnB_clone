![HBNB](https://user-images.githubusercontent.com/54350108/85913016-b08ba100-b7f6-11ea-8f18-0c27ce10e218.jpg)

0x00. AirBnB clone - The console0x00. AirBnB clone - The console

# Description of the project
This is the first multi-part project to build a full [AirBnb](https://es.airbnb.com/?_set_bev_on_new_domain=1592945111_bWw%2By%2F%2FvZh5U%2BDGg) web app clone. In this first part, the command interpreter will be implemented in the Python programming language, in which through the console we can store objects and retrieve objects from a JSON.

# Description of the command interpreter
This command interpreter is similar to a BASH shell but is designed for a specific use case.
Our command interpreter allows us to manage all the functionality of the application from the command line, such as:
- `create`
- `show`
- `destroy`
- `all`
- `update`
- `quit`/EOF quit the console
- `help`

# How to start the interpreter
In the command line run `./console.py` or `echo help | ./console.py`
# How to use the interpreter

------- | ------ | ------
help | `help [option]` | Lists all available commands, or displays what option does
quit | `quit` | Exit command interpreter
EOF | `EOF` | Exit command interpreter
create | `create [class_name]` | Creates an instance of class_name
update | `update [class_name] [object_id] [update_key] [update_value]` | Updates the key:value of class_name.object_id instance
show | `show [class_name] [object_id]` | Displays all attributes of class_name.object_id
all | `all [class_name]` | Displays every instance of class_name, if used without option displays every instance saved to the file
destroy | `destroy [class_name] [object_id]` | Deletes all attributes of class_name.object_id
count | `[class_name].count()` | Counts all the instances with class name specified

#  Testing our console
```
/Holberton/AirBnB_clone$ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)create User
6a64d1a9-42b9-4589-9efc-9e1368809f44
(hbnb)show User 6a64d1a9-42b9-4589-9efc-9e1368809f44
[User] (6a64d1a9-42b9-4589-9efc-9e1368809f44) {'id': '6a64d1a9-42b9-4589-9efc-9e1368809f44', 'updated_at': datetime.datetime(2020, 7, 1, 17, 36, 53, 271047), 'created_at': datetime.datetime(2020, 7, 1, 17, 36, 53, 271006)}
(hbnb)create BaseModel
27ee8601-8446-42bd-b516-9a19e44f9c76
(hbnb)update User 6a64d1a9-42b9-4589-9efc-9e1368809f44 name "Laura"
(hbnb)all
["[User] (6a64d1a9-42b9-4589-9efc-9e1368809f44) {'id': '6a64d1a9-42b9-4589-9efc-9e1368809f44', 'created_at': datetime.datetime(2020, 7, 1, 17, 36, 53, 271006), 'name': 'Laura', 'updated_at': datetime.datetime(2020, 7, 1, 17, 38, 6, 746942)}", "[BaseModel] (27ee8601-8446-42bd-b516-9a19e44f9c76) {'id': '27ee8601-8446-42bd-b516-9a19e44f9c76', 'updated_at': datetime.datetime(2020, 7, 1, 17, 37, 29, 966146), 'created_at': datetime.datetime(2020, 7, 1, 17, 37, 29, 966104)}", "[User] (49812247-e41e-495a-b710-aa1aadf16bc4) {'id': '49812247-e41e-495a-b710-aa1aadf16bc4', 'updated_at': datetime.datetime(2020, 7, 1, 17, 35, 53, 670200), 'created_at': datetime.datetime(2020, 7, 1, 17, 35, 53, 670164)}"]
(hbnb)create User
4eae30f6-f3c4-44ec-98b3-2b8c4e0952ca
(hbnb)User.count()
3
(hbnb)destroy BaseModel 27ee8601-8446-42bd-b516-9a19e44f9c76
(hbnb)show BaseModel 27ee8601-8446-42bd-b516-9a19e44f9c76
** no instance found **
(hbnb)quit
```
