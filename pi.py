#!/usr/bin/env python
# coding: utf-8

# In[23]:


import time
from mpmath import mp

def calculate_pi():
    mp.dps = 9999  # Precision
    pi_str = str(mp.pi)[2:]  # Remove the 3. prefix from pi string
    return pi_str

def display_realtime_pi(pi_digits):
    idx = 0
    while True:
        print(f"\r... {pi_digits[idx]} ...", end="")
        idx = (idx + 1) % len(pi_digits)
        time.sleep(1.5)

pi_digits = calculate_pi()
display_realtime_pi(pi_digits)


# In[2]:


import mpmath
import time

def generate_pi_digits():
    mpmath.mp.dps = 9999  # Precission
    pi_str = str(mpmath.pi)
    pi_digits = [int(digit) for digit in pi_str[2:]]  # Convert to an integer and remove the 3. from pi string
    return pi_digits

def print_realtime_pi(num_digits, update_interval):
    pi_digits = generate_pi_digits()
    pointer_position = 0
    left_padding = " " * (3 * (num_digits // 2))  # Google code

    while True:
        # Prepare the line to print
        line = " |".join(str(digit) for digit in pi_digits[pointer_position:pointer_position + num_digits])
        pointer = left_padding + "^"  # Pointer

        # Clear the previous line and print the new line with the pointer
        print("\r" + line + "\n" + pointer) #Doesn't work LOL!

        # Update pointer position
        pointer_position = (pointer_position + 1) % len(pi_digits)

        # Time in between new digits
        time.sleep(update_interval)

# 7 digits of pi every 0.5 second
print_realtime_pi(7, 0.5)

