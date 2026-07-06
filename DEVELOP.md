# Develop this package

```
git checkout -b dev main
python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

## run tests

```
uvx --with tox-uv tox
```


## run lint

```
uvx --with tox-uv tox -e lint
```

## run dependenciy check

```
uvx --with tox-uv tox -e dependencies
```