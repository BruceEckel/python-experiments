from thespian.actors import Actor, ActorSystem, ActorExitRequest


class Hello(Actor):
    def receiveMessage(self, message, sender):
        self.send(sender, "Hello, World!")


if __name__ == "__main__":
    hello = ActorSystem().createActor(Hello)
    print(ActorSystem().ask(hello, "hi", 1))
    ActorSystem().tell(hello, ActorExitRequest())
