class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state


if __name__ == '__main__':
    c = Borg()
    c.erind = 'test'
    d = Borg()
    print(d.erind)