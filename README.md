# DjangotoEmber

 Combining DjangoRestAPI Pandas and Emberjs

python3 -m venv env

source env/bin/activate

## WSL settings

sudo chown -R $USER ~/GitHub
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa

pip install -r requirements.txt

pip install djangorestframework-jsonapi['django-filter']
pip install djangorestframework-jsonapi['django-polymorphic']
pip install djangorestframework-jsonapi['openapi']
pip install black[jupyter]

## Two Terminals (deactivate venv on Ember one)

cd mysitedjango

cd mysiteemberjs
deactivate

## Run both

python manage.py runserver
ember s

## Git Commands + Use Black Before Upload

black -l 80 mysitedjango

git add .

git commit -m "push message"

git push

## Run custom Django Code

python manage.py shell

run "file"

## Windows Stuff Pipwin + Jupyter notebooks fix

pip install pipwin

pipwin install gdal

pipwin install fiona

In pyreadline files
modified py3k_compat.py by 8 string:
return isinstance(x, collections.Callable) -> return isinstance(x, collections.abc.Callable)
