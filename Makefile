build up:
	docker-compose up -d --build

up:
	docker-compose up -d

test coverage:
	docker-compose exec api bash -c "python -m coverage run -m unittest && python -m coverage html"

down:
	docker-compose down
