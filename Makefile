install:
	pip install -r requirements.txt

train:
	python3 src/main.py

predict:
	python3 src/predict.py