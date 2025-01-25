## Activate Virtual Environment

To setup and Activate Virtual Environment. 

Execute these commands in terminal
>   .\venv\Scripts\activate

## Package / Library Installation:

Method 1:

If you want to install the package from the terminal after setting up the Virtual Environment

Execute these commands from terminal

> pip install flask flask-sqlalchemy flask-jwt-extended python-dotenv flask-marshmallow marshmallow-sqlalchemy

Method 2:

Install all the package from requirements.txt

> pip install -r requirements.txt

FYI (use if needed):

    1. if you want to see the list of used Package/library use this command

    > pip freeze


    2. if you wanted to save the used package/library in requirements.txt. Execute these command

    > pip freeze > requirements.txt


## Run the application

To run the flask application.

>   flask route.py

## To create DB

```bash
>>> from models import db
>>> db.create_all()
```

## To create Secret Key

``` python
import secrets
print(secrets.token_hex(16))
```

## Testing Endpoints
- Use **Postman** or **cURL** to test endpoints.

## Example API Calls (via `curl`):

##  Register Routes

1. **Register Company:**
```bash
curl --location 'http://127.0.0.1:5000/register_company' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "1",
    "email": "1@gmail.com",
    "password": "xxx1"
}'
```

2. **Display all Company**

```bash
curl --location 'http://127.0.0.1:5001/show_all_companies'
```

3. **Find Company By ID**


```bash
curl --location 'http://127.0.0.1:5001/find_Company_By_Id/1'
```

4. **Find Company By EmailAddress**
```bash
curl --location 'http://127.0.0.1:5001/find_By_Company_Email/1@gmail.com'
```

## Login Routes

1. **Company Login:**
```bash
curl --location 'http://127.0.0.1:5000/companyLogin' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"1@gmail.com",
    "password": "xxx1"
}'
```

## Tool routes

1. **Create Tool:**
```bash
curl --location 'http://127.0.0.1:5000/create_tool' \
--header 'Content-Type: application/json' \
--data '{
    "company_id" : 1,
    "name" : "tool2",
    "version":  "v2"
}'
``

2. **Display Tools**

```bash
curl --location 'http://127.0.0.1:5001/show_tool' \
--header 'Content-Type: application/json'
```

```bash

Output:
[
    {
        "id": 1,
        "name": "tool3",
        "version": "v3"
    },
    {
        "id": 2,
        "name": "tool1",
        "version": "v1"
    }
]
```

3. **Get Tool By ID**

```bash
curl --location --request GET 'http://127.0.0.1:5000/get_tool_By_Id/2' \
--header 'Content-Type: application/json' \
--data '{
    "company_id" : 1,
    "name" : "tool1",
    "version":  "v1"
}'
```

```bash

output:
{
    "id": 2,
    "name": "tool1",
    "version": "v1"
}
```

4. **Update Tool By ID**

```bash
curl --location --request PUT 'http://127.0.0.1:5001/update_tool/1' \
--header 'Content-Type: application/json' \
--data '{
    "name" : "tool1",
    "version":  "v1"
}'
```

```bash

Output:

{
    "message": "Tool updated successfully"
}
```

5. **Delete Tool By ID**

```bash
curl --location --request DELETE 'http://127.0.0.1:5001/delete_tool/1' \
--header 'Content-Type: application/json' \
--data ''
```

```bash

Output:

{
    "message": "Tool deleted successfully"
}
```



## Section Route

1. **Create Section**

```bash
curl --location 'http://127.0.0.1:5000/create_section' \
--header 'Content-Type: application/json' \
--data '{
    "tool_id": "1",
    "name": "session1"
}'
```

```bash

Output:

{
    "message": "Section created successfully!",
    "section": 1
}

```

2. **Get Section by ID**


```bash
curl --location 'http://127.0.0.1:5000/get_sections_By_Id/1' \
--header 'Content-Type: application/json'
```


```bash
Output:
{
    "id": 1,
    "name": "session1",
    "tool_id": 1
}

```


3. **Update Section By ID**

```bash
curl --location --request PUT 'http://127.0.0.1:5000/update_section_By_Id/1' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Section Part 1"
}'
```

```bash
Output:

{
    "message": "Section updated successfully"
}


```

4. **Delete Section By ID**

```bash
curl --location --request DELETE 'http://127.0.0.1:5000/delete_section_By_Id/1'
```

```bash
Output:

{
    "message": "Section deleted successfully"
}

```


## Component Route

1. **Create Component**

```bash
curl --location 'http://127.0.0.1:5000/create_components' \
--header 'Content-Type: application/json' \
--data '{
    "section_id": "2",
    "type": "basic",
    "variant": "basic_2",
    "pricing": "22"
}'
```

```bash
Output:

{
    "component": 3,
    "message": "Component created successfully!"
}

```



2. **Get Component By ID**
```bash
curl --location 'http://127.0.0.1:5000/get_component_By_Id/1' \
--header 'Content-Type: application/json'
```

```bash
Output:

{
    "id": 1,
    "pricing": 5.0,
    "section_id": 1,
    "type": "basic",
    "variant": "basic_1"
}


```


3. **Update Component By ID**

```bash
curl --location --request PUT 'http://127.0.0.1:5000/update_component_By_Id/1' \
--header 'Content-Type: application/json' \
--data '{
    "type": "pro",
    "variant": "elite",
    "pricing": "55.5"
}'
```

```bash
Output:

{
    "message": "Section updated successfully"
}
```

4. **Delete Component By ID**


```bash
curl --location --request DELETE 'http://127.0.0.1:5000/delete_component_By_Id/1'
```


```bash
Output:
{
    "message": "Component deleted successfully"
}
```


## Pricing Calculator

```bash
curl --location 'http://127.0.0.1:5000/estimate_cost' \
--header 'Content-Type: application/json' \
--data '{
    "id": 2
}'
```


```bash
Output:
{
    "total_cost": 3.0
}
```



## Publishing Routes

1. **Publishing Live**

```bash
curl --location --request POST 'http://127.0.0.1:5001/publish_tools/3/live' \
--header 'Content-Type: application/json'
```


```bash
Output:
{
    "message": "Tool is in live state"
}
```

2. **Publishing to Draft**

```bash
curl --location --request POST 'http://127.0.0.1:5001/publish_tools/3/draft' \
--header 'Content-Type: application/json'
```


```bash
{
    "message": "Tool is in draft state"
}
```

