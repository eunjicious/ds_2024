all: use_priority dont_use_priority

use_priority:
	python3 main.py -p

dont_use_priority:
	python3 main.py

test:
	python3 -m pytest ./tests

clean:
	rm -rf __pycache__	rm -rf .pytest_cache
	rm -rf ./tests/__pycache__
	rm -rf ./utils/__pycache__