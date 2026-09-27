#variables
IMAGE=blogsvc:latest
CONTAINER=blogsvc

run:
	uvicorn app.main:app --reload

# run container
build:
	docker build -t $(IMAGE) .
docker_up:
	docker run --rm --name $(CONTAINER) -p 8000:8000 $(IMAGE)
# stop and delete container
docker_down:
	docker stop $(CONTAINER)
	docker rm $(CONTAINER)
# interactive shell
shell:
	docker exec -it $(CONTAINER) /bin/sh
.PHONY: run build up down shell

