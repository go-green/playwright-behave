## PRM web UI Tests

### Project setup

```
git clone
python -m venv venv
.\venv\Scripts\ativate
pip install --upgrade setuptools
pip install -r requirements.txt
playwrght install
```

### Running UI tests

```
behave ./features 
```

### Generating test report

```
allure serve .\allure-results\
```