# Makefile

.PHONY: run clean docs

run: main.py
	python3 main.py

clean:
	rm -rf __pycache__

docs:
	doxygen Doxyfile
