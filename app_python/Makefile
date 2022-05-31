docker_nickname = willsem
docker_image = moscow-local-time

restart: build clean run
	:

build:
	docker build -t $(docker_nickname)/$(docker_image) .

push:
	docker push $(docker_nickname)/$(docker_image)

run:
	docker run -d -p 5001:5000 --name $(docker_image) $(docker_nickname)/$(docker_image)

clean:
	docker stop $(docker_image)
	docker rm $(docker_image)
