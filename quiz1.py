####################################################################################
#This quiz is based on sample  Bare conductive code - see licence information below#
####################################################################################
#                                                                                  #
# Bare Conductive Pi Cap                                                           #
# ----------------------                                                           #
#                                                                                  #
# simple-touch.py - simple MPR121 touch detection demo with stdout output          #
#                                                                                  #
# Written for Raspberry Pi.                                                        #
#
# Bare Conductive code written by Szymon Kaliski.
#
# This work is licensed under a MIT license https://opensource.org/licenses/MIT
#
# Copyright (c) 2016, Bare Conductive
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#################################################################################

import time
import signal, sys, MPR121

try:
  sensor = MPR121.begin()
except Exception as e:
  sys.exit(1)

# handle ctrl+c gracefully
def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def check_answer(expected):
	while True:
		if sensor.touch_status_changed():
      			sensor.update_touch_data()
		if sensor.is_new_touch(expected):
        		if expected !=99:
				print ("Correct")
				state = True
				return state
				break
			
		else:
			if expected !=99:
				print ("Incorrect")
				state = False
				return state
				break	
score = 0

print ("To check if everything is working press the start button")
state = check_answer(4)
if state == False:
	print ("You pressed the wrong button")
state = check_answer(99)

print ("1. This component is found in the mains plug and will blow if too much current flows")
state = check_answer(11)
if state == True:
  score +=1
time.sleep(1)
state = check_answer(99)

print ("2. This measures the voltage (pd) in a circuit")
state = check_answer(0)
if state == True:
  score +=1
time.sleep(1)
state = check_answer(99)

print ("3. [True or False] An ammeter is connected in series in the circuit")
state = check_answer(10)
if state == True:
  score +=1
time.sleep(1)
state = check_answer(99)

print ("4. This component changes the resistance in a circuit and can be used as a dimmer switch for a light")
state = check_answer(1)
if state == True:
  score +=1
time.sleep(1)
state = check_answer(99)

print ("5. [True or False] The units of resistance are Watts (W)")
state = check_answer(9)
time.sleep(1)
if state == True:
  score +=1
state = check_answer(99)

print ("6. [True or False] An ammeter is connected in parallel in the circuit")
state = check_answer(10)
time.sleep(1)
if state == True:
  score +=1
state = check_answer(99)

print ("7. This component's resistance varies with light level")
state = check_answer(3)
time.sleep(1)
if state == True:
  score +=1
state = check_answer(99)

print ("8. This component converts electrical energy into light energy")
state = check_answer(6)
time.sleep(1)
if state == True:
  score +=1
state = check_answer(99)

print ("9. This component's resistance varies with temperature")
state = check_answer(2)
time.sleep(1)
if state == True:
  score +=1
state = check_answer(99)

print ("10. This is the symbol for a fixed resistor")
state = check_answer(5)
time.sleep(1)
if state == True:
  score +=1
state = check_answer(99)

print ("11. You would use this component to measure the current flowing in a circuit")
state = check_answer(7)
time.sleep(1)
if state == True:
  score +=1
state = check_answer(99)

print ("Quiz over")
print ("---- ----")
print ("")
print ("Your score is " + str(score))
