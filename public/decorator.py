""" 装饰器 """


def sliptimes(func):
    def wrapper(n):
        while 1:
            if n >= 1:
                for i in range(n):
                    func(n)
                break
            else:
                return
    return wrapper
