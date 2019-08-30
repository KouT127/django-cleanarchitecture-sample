## Python
pyenvでpythonのVersionを固定する　　

    pyenv install 3.7.2
    pyenv shell 3.7.2  # shell or local
    pyenv local 3.7.2
virtualenvでライブラリ等を管理する　　

    virtualenv env
    . env/bin/activate
    pip install -r requirements.txt

envから抜ける

    deactivate  