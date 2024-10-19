# Makefile

.PHONY: all build run stop logs clean

IMAGE_NAME = mlops-app
CONTAINER_NAME = mlops_container
PORT = 8000

all: build run

build:
	podman build -t $(IMAGE_NAME) .

run:
	podman run -d --name $(CONTAINER_NAME) -p $(PORT):8000 $(IMAGE_NAME)

stop:
	podman stop $(CONTAINER_NAME)
	podman rm $(CONTAINER_NAME)

logs:
	podman logs -f $(CONTAINER_NAME)

clean: stop
	podman rmi $(IMAGE_NAME)
