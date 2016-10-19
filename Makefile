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

.PHONY: test
test: $(setup)
	$(pytest) --cov=better --flake8 tests/
