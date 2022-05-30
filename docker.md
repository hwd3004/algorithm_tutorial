```bash
docker run -d -it --name python-container -v C:\workspace\algorithm_tutorial:/algorithm_tutorial python:3.10

docker exec -it python-container bash

pip install pipenv
```