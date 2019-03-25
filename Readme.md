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
    
   
OneToOne
   
   ユニークであるならば使える
   それ以外はManyToManyの可能性がある
   
select_related

    １対１
    多対１
    
    
prefetch_related

    一対多
    多対多

prefetch(prefetch_relatedをコントロールする)
    クエリセットにPrefetchの下の階層のデータで行って欲しいQuery、to_attrで別名つけてall()のようにおこえる

    Prefetch('choice_set', queryset=voted_choices, to_attr='voted_choices')
    
Dockerで行う場合
mysqlclientでなく、
PyMySQLで行えば大丈夫な場合がある。 

    pip install PyMySQL

    import pymysql
    pymysql.install_as_MySQLdb()
    
使用中のポートを確認する
    lsof  -i:80
   
https://mkai.hateblo.jp/entry/2018/11/05/234611  
