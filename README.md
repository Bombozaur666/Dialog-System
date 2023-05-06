
# Dialog-System

Project made to learn how to dialog system works.

Dialog language is `polish`, so not everyone will be able to use this propely ;). 


It is dockerised because nlu library `pyjsfg` will work only on Linux system. I wanted to work on it on every system, not specyfied.

To build this container you need to use this command:

```bash
docker-compose build
```

To run this container you need to use this command.

```bash
docker-compose run system
```


If you want run evaluation script(check on how many sample data NLU will detect slots) you need to build this container and then run this command:

```bash
docker-compose run system python evaluate.py
```
