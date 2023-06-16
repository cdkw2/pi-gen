#!/usr/bin/env python
# coding: utf-8

# In[28]:


import time
from mpmath import mp
import pyautogui

def calculate_pi():
    mp.dps = 9999  # Precision
    pi_str = str(mp.pi)[2:]  # Remove the 3. prefix from pi string
    return pi_str

def fun_0():
    pyautogui.moveTo(100, 100)

def fun_1():
    pyautogui.moveTo(200, 200)

def fun_2():
    pyautogui.moveTo(300, 300)

def fun_3():
    pyautogui.moveTo(400, 400)

def fun_4():
    pyautogui.moveTo(500, 500)

def fun_5():
    pyautogui.moveTo(600, 600)

def fun_6():
    pyautogui.moveTo(700, 700)

def fun_7():
    pyautogui.moveTo(800, 800)

def fun_8():
    pyautogui.moveTo(900, 900)

def fun_9():
    pyautogui.moveTo(1000, 1000)

def display_realtime_pi(pi_digits):
    idx = 0
    try:
        while True:
            digit = pi_digits[idx]
            print(f"\r... {digit} ...", end="")
            if digit == "0":
                fun_0()
            elif digit == "1":
                fun_1()
            elif digit == "2":
                fun_2()
            elif digit == "3":
                fun_3()
            elif digit == "4":
                fun_4()
            elif digit == "5":
                fun_5()
            elif digit == "6":
                fun_6()
            elif digit == "7":
                fun_7()
            elif digit == "8":
                fun_8()
            elif digit == "9":
                fun_9()
            idx = (idx + 1) % len(pi_digits)
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

pi_digits = calculate_pi()
display_realtime_pi(pi_digits)


# In[29]:


import mpmath
import time

def generate_pi_digits():
    mpmath.mp.dps = 9999  # Precision
    pi_str = str(mpmath.pi)
    pi_digits = [int(digit) for digit in pi_str[2:]]  # Convert to an integer and remove the 3. from pi string
    return pi_digits

def print_realtime_pi(num_digits, update_interval):
    pi_digits = generate_pi_digits()
    pointer_position = 0
    left_padding = " " * (3 * (num_digits // 2))  # Custom code

    try:
        while True:
            # Prepare the line to print
            line = " |".join(str(digit) for digit in pi_digits[pointer_position:pointer_position + num_digits])
            pointer = left_padding + "^"  # Pointer

            # Clear the previous line and print the new line with the pointer
            print("\033[F" + line + "\n\033[F" + pointer) # Move the cursor up and print the new line

            # Update pointer position
            pointer_position = (pointer_position + 1) % len(pi_digits)

            # Time in between new digits
            time.sleep(update_interval)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

# 7 digits of pi every 0.5 second
print_realtime_pi(7, 0.5)


# In[27]:


import time
from mpmath import mp

def calculate_pi():
    mp.dps = 9999  # Precision
    pi_str = str(mp.pi)[2:]  # Remove the 3. prefix from pi string
    return pi_str

def display_realtime_pi(pi_digits):
    idx = 0
    digit_messages = {
        "0": "It's a 0",
        "1": "It's a 1",
        "2": "It's a 2",
        "3": "It's a 3",
        "4": "It's a 4",
        "5": "It's a 5",
        "6": "It's a 6",
        "7": "It's a 7",
        "8": "It's an 8",
        "9": "It's a 9"
    }
    try:
        while True:
            digit = pi_digits[idx]
            message = f"\r... {digit} ..."
            if digit in digit_messages:
                message += f"\n{digit_messages[digit]}"
            print(message, end="")
            idx = (idx + 1) % len(pi_digits)
            time.sleep(1.5)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

pi_digits = calculate_pi()
display_realtime_pi(pi_digits)

