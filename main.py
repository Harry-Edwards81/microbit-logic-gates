from microbit import *

# Current selected logic gate
selector = 0

# List of available gates
logicOperators = ['AND', 'OR', 'NOT A', 'NOT B', 'XOR']

# Function to display all LEDs at maximum brightness
def onDisplay():
    display.show(Image('99999:'
                       '99999:'
                       '99999:'
                       '99999:'
                       '99999'))

# AND gate: displays LEDs only if both buttons are pressed
def AND():
    while button_a.is_pressed() and button_b.is_pressed():
        onDisplay()  # show full LED pattern while both buttons are pressed
    display.clear()  # clear LEDs when either button is released

# OR gate: displays LEDs if either button is pressed
def OR():
    while button_a.is_pressed() or button_b.is_pressed():
        onDisplay()  # show full LED pattern while at least one button is pressed
    display.clear()  # clear LEDs when both buttons are released

# NOT A gate: displays LEDs when button A is NOT pressed
# Can switch gate with logo touch or shake gesture
def NOT_A(selector):
    while not button_a.is_pressed():  # loop while A is not pressed
        onDisplay()  # show full LED pattern

        # Check if user touches logo to move to next logic gate
        if pin_logo.is_touched():
            selector += 1  # increment selector
            display.scroll(logicOperators[selector])  # show new gate name
            sleep(200)  # short delay to debounce touch
            break  # exit loop

        # Check if user shakes micro:bit to reset to first gate
        elif accelerometer.is_gesture('shake'):
            selector = 0
            display.scroll(logicOperators[selector])
            sleep(200)
            break  # exit loop

    display.clear()  # clear LEDs when leaving NOT A function
    return selector  # return updated selector to main loop

# NOT B gate: displays LEDs when button B is NOT pressed
# Can switch gate with logo touch or shake gesture
def NOT_B(selector):
    while not button_b.is_pressed():  # loop while B is not pressed
        onDisplay()  # show full LED pattern

        # Check if user touches logo to move to next gate
        if pin_logo.is_touched():
            selector += 1
            display.scroll(logicOperators[selector])
            sleep(200)
            break

        # Check if user shakes micro:bit to reset to first gate
        elif accelerometer.is_gesture('shake'):
            selector = 0
            display.scroll(logicOperators[selector])
            sleep(200)
            break

    display.clear()  # clear LEDs when leaving NOT B function
    return selector  # return updated selector to main loop

# XOR gate: displays LEDs when exactly one button is pressed
# Includes simple debouncing to account for imperfect human timing
def XOR(selector):
    # Save initial button states
    a1 = button_a.is_pressed()
    b1 = button_b.is_pressed()

    while True:
        # Allow user to exit XOR by touching logo or shaking
        if pin_logo.is_touched() or accelerometer.is_gesture('shake'):
            selector = 0  # reset selector to first gate
            display.scroll(logicOperators[selector])
            sleep(200)
            return selector  # exit XOR function

        sleep(40)  # short delay for debouncing button presses

        # Read button states again after delay
        a2 = button_a.is_pressed()
        b2 = button_b.is_pressed()

        # Only update display if button states are stable (debounced)
        if a1 == a2 and b1 == b2:
            # XOR logic: exactly one button pressed → display LEDs
            if (a2 or b2) and not (a2 and b2):
                onDisplay()
            else:
                display.clear()  # clear LEDs if both or none pressed

        # Update previous button states for next iteration
        a1 = a2
        b1 = b2

# Display the initial gate name
display.scroll(logicOperators[selector])

# Main loop: continuously checks inputs and runs the selected logic gate
while True:
    if pin_logo.is_touched():  # cycle to next gate on logo touch
        selector = 0 if selector == 4 else selector + 1  # wrap around to first gate if needed
        display.scroll(logicOperators[selector])
        sleep(300)  # debounce logo touch

    elif accelerometer.is_gesture('shake'):  # reset selector on shake
        selector = 0
        display.scroll(logicOperators[selector])

    elif selector == 0:
        AND()  # run AND gate

    elif selector == 1:
        OR()  # run OR gate

    elif selector == 2:
        selector = NOT_A(selector)  # run NOT A gate

    elif selector == 3:
        selector = NOT_B(selector)  # run NOT B gate

    elif selector == 4:
        selector = XOR(selector)  # run XOR gate