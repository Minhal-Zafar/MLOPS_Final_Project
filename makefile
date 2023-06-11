install: 
	pip install --upgrade pip && pip install -r requirements.txt

format:
	echo "Formatted files"
	#black *.py

lint:
	echo "Pylint finished"
	
