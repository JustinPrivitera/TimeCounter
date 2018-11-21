# 03/22/18
# Justin Privitera
# TimeCounter
# v1.5
#
# Version History:
# 03/21/18 v1.0 - provided basic functionality
# 03/22/18 v1.1 - added my more powerful split function, 
#                 prepended 0s when a value is a single digit
# 03/22/18 v1.2 - allowed for input of variable length, simplified the addition phase
# 03/22/18 v1.3 - transformed the program into a function so that it can be called in other programs
# 03/22/18 v1.4 - changed the result times into a list to cut down on lines and variables
# 03/22/18 v1.5 - added a test for validity, so the function won't break when incorrect inputs are given
#
# To be used to add values represented by units of time, so a minute calculator, so to speak.
# My idea was usage for counting total duration of different audio files so that a playlist could be completed in a timely manner.
# It takes in a series of inputs that have to be formatted as an integer with a semicolon followed by another integer, 
# ending with the String 'done'.
#
# At the end of the file is a simple user test with input and output

# imports the StringToken function I created
from StringToken import stringToken

def timeCounter(times):

	totalTime = [0, 0, 0] #format is [hours, minutes, seconds]

	# add times
	for i in range(0, len(times)):
		if not valid(times[i]):
			return "Invalid input: " + times[i]

		#parser = times[i].split(":") # default split function
		parser = stringToken(times[i], ":") # my more powerful split function
		while len(parser) != 3:
			parser.insert(0, 0)
		for j in range(0, 3):
			totalTime[j] += int(parser[j])

	extraMinutes = int(totalTime[2] / 60) # cut off excess seconds and add them to minute total
	extraHours = int((totalTime[1] + extraMinutes) / 60) # cut off excess minutes and add them to hour total

	result = [] # same format as totalTime, this stores string versions of the results

	# Ensures time is displayed properly
	result.append(str(totalTime[0] + extraHours))
	result.append(str((totalTime[1] + extraMinutes) % 60))
	result.append(str(totalTime[2] % 60))

	for i in range(0, 3):
		if len(result[i]) < 2:
			result[i] = "0" + result[i]

	# return result
	return "Total Time: {}:{}:{}".format(result[0], result[1], result[2])


def valid(word): # returns true if the word entered is valid, false if invalid
	
	isValid = True
	for i in range(0, len(word)):
		if word[i] not in "1234567890:": # Note: a time of the form "3::03" is still considered valid, and the second colon will be ignored.
			isValid = False
	return isValid

# A simple test to demonstrate functionality

print("Enter a sequence of times to be added, then enter done when finished: ")

times = []
while True:
	entered = input()
	if entered == "done":
		break
	times.append(entered)

print(timeCounter(times))