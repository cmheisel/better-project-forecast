pytest = venv/bin/pytest
setup = better_project_forecast.egg-info


$(pytest):
	virtualenv ./venv
	./venv/bin/pip install -r requirements.txt

$(setup): $(pytest)
	./venv/bin/python setup.py develop


.PHONY: clean
clean:
	rm -rf venv
	rm -rf *.egg-info
	rm -rf .cache
	rm -rf .coverage
	rm -rf sdist-venv
	rm -rf dist

.PHONY: test
test: $(setup)
	$(pytest) --cov=better --flake8 tests/

.PHONY: test_sdist
test_sdist: clean
	python setup.py sdist
	virtualenv ./sdist-venv
	./sdist-venv/bin/pip install ./dist/*.tar.gz
	./sdist-venv/bin/python setup.py test
	./sdist-venv/bin/python -c "import better; assert better"
