# QA Automation scripts

Setup test environment

```sh
# create and activate a virtualenv using your preferred method. Example:
python -m venv venv
source venv/bin/activate

# install requirements
pip install -r requires.txt

```

Copy `settings-sample.cfg` to `settings.cfg` and populate `settings.cfg` for
the environment you want to test.


Run tests

```sh
command to execute the scripts with 2 reruns
pytest -v --reruns 2 --capture=tee-sys --html=report.html --self-contained-html

command to execute the scripts with 2 reruns and in parallel
pytest -v -n auto --reruns 2 --capture=tee-sys --html=report.html --self-contained-html
```
