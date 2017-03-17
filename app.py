#!/usr/bin/env python
def greetings():
 	"""new comment"""
	print "Hello RESIF people!"
        print "oui on est vendredi"
        print "new modif 10:53"

def repeat(x, callback):
	for _ in range(x):
 		callback()
if __name__ == "__main__":
 	repeat(5, greetings)

