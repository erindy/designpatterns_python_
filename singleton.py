class Singleton:
    __instance = None
    def __new__(cls, val=None, name=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        Singleton.__instance.name = name
        return Singleton.__instance

if __name__=='__main__':
    x = Singleton('burger', 'erind')
    print(x.val + x.name )