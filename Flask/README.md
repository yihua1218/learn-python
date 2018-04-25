# Flask

http://flask.pocoo.org/docs/0.12/

因為辣媽 Mei Lin 的推薦，來試用看看 Python 上面的 Webdevelopment Framework。也許可以成為我正在學習 Python 的朋友們的練習之一。

## Hello Flask

第一個練習，總是 Hello。

``` bash
bash-4.4$ . venv/bin/activate
(venv) bash-4.4$ export FLASK_APP=hello.py
(venv) bash-4.4$ flask run
 * Serving Flask app "hello"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [18/Apr/2018 08:25:02] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [18/Apr/2018 08:25:02] "GET /favicon.ico HTTP/1.1" 404 -
```
