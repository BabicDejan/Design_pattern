#Old --> JSON - str
#New --> XML - int

#inheritance example

class Old: #string class
    def get(self):
        return "123"

class New: #int class
    def get(self):
        return 123

#ovo iziskuje kreiranje nove klase koja je adapter
class Adapter():
    def __init__(self, cls):
        self.cls = cls

    def get(self):
        return str(self.cls.get())

def main(obj):
    print("The result is " + obj.get())


if __name__ == '__main__':
    obj = Adapter(New())
    main(obj)
