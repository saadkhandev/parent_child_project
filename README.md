# parent_child_project

#### Download or clone the project from : 
https://github.com/saadkhandev/parent_child_project

#### Go to project directory
for example /home/user/Desktop/parent_child_project

#### Python 3 should be installed in your Windows/Linux/Mac first
- These instractions are based on Linux
- Run the command in terminal:
```
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
```

#### For TDD
```
    $ python manage.py test app
```

#### Go to the URL: http://127.0.0.1:8000/api/v1/ + endpoints
- By using the following URL + endpoints the Rest API communication is performed.
- Main API endpoints are:

| SL. |  URL + endpoint | Method | Purpose |  
|---|---|---|---| 
| 1 | URL/parents/ | GET | To get all parent list | 
| 2 | URL/parents/id/ | GET | To get single parent list | 
| 3 | URL/parents/ | POST | To create a parent | 
| 4 | URL/parents/id/ | PUT | To update single parent list | 
| 5 | URL/parents/id/ | DELETE | To delete single parent list |
| 6 | URL/children/ | GET | To get all children list |
| 7 | URL/children/id/ | GET | To get single child list |  
| 8 | URL/children/ | POST | To create a child | 
| 9 | URL/children/id/ | PUT | To update single child list | 
| 10 | URL/children/id/ | DELETE | To delete single child list |  

- After hitting the url the sample responses are :
```
    1. HTTP_201_CREATED
    2. HTTP_400_BAD_REQUEST
    3. HTTP_401_UNAUTHORIZED
    4. HTTP_403_FORBIDDEN
    5. HTTP_415_UNSUPPORTED_MEDIA_TYPE
    6. HTTP_409_CONFLICT
    7. HTTP_404_NOT_FOUND
    8. HTTP_204_NO_CONTENT
    9. HTTP_500_INTERNAL_SERVER_ERROR
    10. HTTP_200_OK
```

#### Go to Postman and copy the url in there and hit the send button

URL + endpoints examples are given based on Postman
#### SL. 1
- Method: GET

- Url: URL/parents/

- Body -> raw
```
{	

}
```

- Required fields:

| key value|is_required|
|---|---|
| | |

- Response:
```
[
    {
        "id": 1,
        "first_name": "Saad",
        "last_name": "khan",
        "street": "a",
        "city": "b",
        "state": "c",
        "zip": "d",
        "children": [],
        "address": "a, b, c, d"
    },
    {
        "id": 2,
        "first_name": "Zubair",
        "last_name": "khan",
        "street": "a",
        "city": "b",
        "state": "c",
        "zip": "d",
        "children": [],
        "address": "a, b, c, d"
    }
]
```

#### SL. 2
- Method: GET
- Url: URL/parents/id/
- Body -> raw
```
{	

}
```
- Required fields:

| key value|is_required|
|---|---|
| | |

- Response:
```
{
    "id": 3,
    "first_name": "Saad",
    "last_name": "khan",
    "street": "a",
    "city": "b",
    "state": "c",
    "zip": "d",
    "children": [],
    "address": "a, b, c, d"
}
```

#### SL. 3
- Method: POST
- Url: URL/parents/
- Body -> raw
```
{
    "first_name": "Saad",
    "last_name": "khan",
    "street": "a",
    "city": "b",
    "state": "c",
    "zip": "d"

}
```
- Required fields:

| key value|is_required|
|---|---|
|first_name | True |
|last_name | True |
|street | True |
|city | True |
|state | True |
|zip | True |

- Response:
```
{
    "id": 3,
    "first_name": "Saad",
    "last_name": "khan",
    "street": "a",
    "city": "b",
    "state": "c",
    "zip": "d",
    "children": [],
    "address": "a, b, c, d"
}
```

#### SL. 4
- Method: PUT
- Url: URL/parents/id/
- Body -> raw
```
{
    "first_name": "S",
    "last_name": "khan",
    "street": "a",
    "city": "b",
    "state": "c",
    "zip": "d"

}
```
- Required fields:

| key value|is_required|
|---|---|
|first_name | True |
|last_name | True |
|street | True |
|city | True |
|state | True |
|zip | True |

- Response:
```
{
    "id": 3,
    "first_name": "Saad",
    "last_name": "khan",
    "street": "a",
    "city": "b",
    "state": "c",
    "zip": "d",
    "children": [],
    "address": "a, b, c, d"
}
```

#### SL. 5
- Method: DELETE
- Url: URL/parents/id/
- Body -> raw
```
{


}
```
- Required fields:

| key value|is_required|
|---|---|
| | |

- Response:
```
{

}
```

#### SL. 6
- Method: GET
- Url: URL/children/
- Body > raw
```
{


}
```
- Required fields:

| key value|is_required|
|---|---|
| | |

- Response:
```
[
    {
        "id": 1,
        "first_name": "child1",
        "last_name": "child1",
        "get_parent": "Saad khan",
        "address": "a, b, c, d",
        "parent": 1
    },
    {
        "id": 2,
        "first_name": "child2",
        "last_name": "child2",
        "get_parent": "Saad khan",
        "address": "a, b, c, d",
        "parent": 1
    }
]
```

#### SL. 7
- Method: GET
- Url: URL/children/id/
- Body > raw
```
{


}
```
- Required fields:

| key value|is_required|
|---|---|
| | |

- Response:
```
{
    "id": 1,
    "first_name": "child1",
    "last_name": "child1",
    "get_parent": "Saad khan",
    "address": "a, b, c, d",
    "parent": 1
}
```

#### SL. 8
- Method: POST
- Url: URL/children/
- Body > raw
```
{
    "first_name": "child1",
    "last_name": "child1",
    "parent": 1

}
```
- Required fields:

| key value|is_required|
|---|---|
|first_name |True |
|last_name |True |
|parent |True |

- Response:
```
{
    "id": 1,
    "first_name": "child1",
    "last_name": "child1",
    "get_parent": "Saad khan",
    "address": "a, b, c, d",
    "parent": 1
}
```

#### SL. 9
- Method: PUT
- Url: URL/children/id/
- Body > raw
```
{
    "first_name": "child12",
    "last_name": "child12",
    "parent": 1

}
```
- Required fields:

| key value|is_required|
|---|---|
|first_name |True |
|last_name |True |
|parent |True |

- Response:
```
{
    "id": 1,
    "first_name": "child12",
    "last_name": "child12",
    "get_parent": "Saad khan",
    "address": "a, b, c, d",
    "parent": 1
}
```

#### SL. 10
- Method: DELETE
- Url: URL/children/id/
- Body > raw
```
{

}
```
- Required fields:

| key value|is_required|
|---|---|
| | |
| | |
| | |

- Response:
```
{

}
```