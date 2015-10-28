# Settingup the Project

TODO: put together all these setups to setup.sh

## install pyenv
```
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
exec $SHELL
```

## install pyenv-virtualenv plugin
```
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
exec "$SHELL"
```

## install latest Python with pyenv
use 3.5.0 in this Project.
```
pyenv install 3.5.0
```

## create virtualenv for this project named `django`
```
pyenv virtualenv 3.5.0 django
```

## set the local application-specific Python version to `django` created above
```
pyenv local django
```
