# python-socket-server

in this project I created a python client server application. there is a list of customer information in database and the server program loads it at the beginning. The client program has access to this database by its interface. The user has options to add, find, delete, update and print report(of all customers information). As a challenge I improved the original design of the program to support concurrency. This way the server can handle multiple clients. 


### prerequisites:
you need to have[python3](https://wiki.python.org/moin/BeginnersGuide/Download) installed on your machine

### to run the program:

1. clone the project to a directory on your machine:

```
git clone git@github.com:shahryar-h/python-socket-server.git

```
then navigate to the project folder in terminal. and run:

```
python3 server2.py
```
now thevserver is up. next, run another terminal and again navigate to the project's folder.
now we run the client program by running:

```
python3 client2.py
```
you may now see the client menu as follows:

![GitHub Logo](/images/logo.png)