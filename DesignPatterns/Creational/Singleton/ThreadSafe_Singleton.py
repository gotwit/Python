from threading import Lock, Thread

class SingletonMeta(type):
    """ This is a thread-safe implementation of Singleton. """

    # class variable / members
    _instances = {}

    _lock: Lock = Lock()

    """ 
    We now have a lock object that will be used to synchronize threads during first 
    access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of `__inti__` argument do not affect the returned value.
        """

        """
        Assume the program has just been launched. SInce there's no
        Singleton instance yet, multiple threads can simultaneously pass the 
        previous condition and reach the point almost at the same time.
        First of them will acquire lock and will proceed further, while the rest will wait here.
        """
        # instance variable cls / self is `this` or instance parameter
        with cls._lock:
            """
            The first thread to acquire the lock, reaches this conditional,
            goes inside and creates the Singleton instance. Once it leaves the lock block,
            a thread that might have been waiting for the lock release may then enter this section.
            But since the Singleton field is already initialized, the thread won't create new object.
            """
            if cls not in cls._instances:
                instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def business_logic(self):
        print("business logic is here")


def test_singleton(value: str)->None:
    singleton = Singleton(value)
    print(singleton.value + "\n")

if __name__ == "__main__":
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("Shazam",))
    process2 = Thread(target=test_singleton, args=("Jam",))
    process1.start()
    process2.start()