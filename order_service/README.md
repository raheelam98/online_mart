# online_mart_class

poetry —-version

**Poetry Commands**

**Create Poetry Project**

```bash
poetry new project_name 
```

add drivers mac
```shell
poetry add fastapi uvicorn\[standard\] 
```

add drivers for db
```shell
poetry add sqlmodel psycopg
```

add drivers (one line command) mac
```shell
poetry add fastapi sqlmodel uvicorn\[standard\] psycopg 
```

add drivers (one line command) window
```shell
poetry add fastapi uvicorn[standard] sqlmodel psycopg 
```

run poetry app
```shell
poetry run uvicorn folder_name.file_name:app --port 8000 --reload
```

```shell
poetry run uvicorn app.main:app --reload
```
**======================== ** ** ========================**

**Methods HTTP (Hypertext Transfer Protocol)**

GET: Retrieves data from a server.

POST: Sends data to the server to create a new resource. 

PUT: Updates or replaces an existing resource on the server.

DELETE: Removes a resource from the server.

PATCH: Applies partial modifications to a resource.

**======================== ** ** ========================**

**Difference between return and yield Python**

**return** sends a value and terminates a function
**yield** in Python used to create a generator function
-statement only pauses the execution of the function
-yield statements are executed when the function resumes its execution.
**Note:** The generator is NOT a normal function. It remembers the previous state like local variables (stack).

**======================== ** ** ========================** 

## Tutorials


[Simple Hero API with FastAPI](https://sqlmodel.tiangolo.com/tutorial/fastapi/simple-hero-api/)

[Using Dataclasses](https://fastapi.tiangolo.com/advanced/dataclasses/)

[Why Aren't We Getting More Data](https://sqlmodel.tiangolo.com/tutorial/fastapi/relationships/#why-arent-we-getting-more-data)

[Dependencies with yield](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)

[Lifespan Events](https://fastapi.tiangolo.com/advanced/events/)

[SQL (Relational) Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)