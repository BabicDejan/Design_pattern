from unicodedata import name


class Target:
    """
    This class is the interface used by the client code
    """

    def request(self):
        return "Target: The default target's behaviour"

def client_code(target: "Target"):

    #This function supports all classes following Target interface

    print(target.request())


class Adaptee:
    """
    This is the new class which has some useful behaviour but is incompatible
    with client_code function
    """

    def specific_request(self):
        return "ruoivaheb laiceps si sihT"

#inheriting adapter class

class Adapter(Target, Adaptee):
    """
    This class makes the Adaptee's interface compatible with the Target's
    interface through inheritance
    """
    def request(self):
        return "(TRANSLATED): " + super(Adapter, self).specific_request()[::-1]


if __name__ == "__main__":
    print("Client: I am working fine with Target objects: ")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    try:
        client_code(adaptee)
    except:
        print("Client: There was an error, i don't seem to understand Adaptee interface!\n")
        print("Client: Adaptee returned this: " + adaptee.specific_request() + "\n")

    print("Client: Lets try with Adapter..\n")
    adapter = Adapter()
    client_code(adapter)



