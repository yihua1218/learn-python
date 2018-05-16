# Virtual Environment

這禮拜練習使用 virtualenv 在 Mac OS 和 Windows 10 上面建立虛擬環境。

## Mac OS

``` bash
$ pip install virtualenv
$ virtualenv -p python3 day6
$ source day6/bin/activate
```

## Windows 10

``` powershell
> pip install virtualenv
> virtualenv -p python day6
> cmd
> day6/scripts/activate
```

## urlib3

``` bash
$ pip install urllib3
```

## Pillow

[Pillow](https://pillow.readthedocs.io/en/latest/installation.html)

``` bash
$ pip install Pillow
```

## QRCode

``` bash
$ pip install qrcode
$ pip install Image
$ qr "Hello Python" > test.png
```