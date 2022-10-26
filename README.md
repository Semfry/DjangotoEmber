# DjangotoEmber

 Combining DjangoRestAPI Pandas and Emberjs

python3 -m venv env

source env/bin/activate

## WSL settings

sudo chown -R $USER ~/GitHub
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa

## Jupyter notebooks fix

In pyreadline files
modified py3k_compat.py by 8 string:
return isinstance(x, collections.Callable) -> return isinstance(x, collections.abc.Callable)

## pipwin on Windows

pip install pipwin

pipwin install gdal

pipwin install fiona

pip install -r requirements.txt

pip install djangorestframework-jsonapi['django-filter']
pip install djangorestframework-jsonapi['django-polymorphic']
pip install djangorestframework-jsonapi['openapi']
pip install black[jupyter]

## Two Terminals

cd mysitedjango
cd mysiteemberjs

## Run both as proxies

python manage.py runserver
ember s

git commit -m "push message"

git push

black -l 80 mysitedjango

## Run custom Django Code

python manage.py shell

run "file"
