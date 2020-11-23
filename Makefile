.PHONY: build run run-prod clean

build:
	@sudo docker-compose build

run:
	@sudo docker-compose up

run-prod:
	@sudo docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

clean:
	@sudo docker-compose down