'''
Createa background process that runs a function every second.
'''
import time
import threading

def my_function():
    print("Hello world")

def main():
    threading.Timer(1.0, my_function).start()
    
if __name__ == "__main__":
    main()