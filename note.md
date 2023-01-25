docker run -itd --name python-container -v c:/workspace/algorithm_tutorial:/algorithm_tutorial python

docker run -itd --name python-container -v ${pwd}:/home/algorithm_tutorial python

docker exec -it python-container bash