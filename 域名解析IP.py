import socket


def url2ip(ul=[]):
    res = {i: '' for i in ul}
    for i in ul:
        try:
            inf = socket.getaddrinfo(i, None)
            res[i] = inf[0][4][0]
        except:
            pass
    return res


if __name__ == '__main__':
    ul = ['www.baidu.com', 'www.baidu.com', 'www.baidu.com']
    print(url2ip(ul))
