#build docker compose
build:
	docker compose build
#run docker compose up
run:
	docker compose up
#docker compose interactive shell remove
shell:
	docker compose run --rm blogsvc bash

.PHONY: run build shell

