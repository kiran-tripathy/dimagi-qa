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
pytest --reruns 2 --reruns-delay 2 --capture=tee-sys  --email_pytest_report Y
```
