# Micro:bit Logic Gates Simulator

## Overview
This project simulates basic digital logic gates (AND, OR, NOT A, NOT B, XOR) using a BBC micro:bit.  
It is designed as an **interactive and educational tool** to help children or beginners understand how logic gates work in a hands-on way.

## Features
- **AND Gate**: LEDs light up only when both buttons A and B are pressed.
- **OR Gate**: LEDs light up when either button A or B is pressed.
- **NOT A / NOT B Gates**: LEDs light up when the respective button is NOT pressed.
- **XOR Gate**: LEDs light up when exactly one button is pressed (includes simple debouncing for human timing).

## Educational Purpose
- Helps beginners visualize how different logic gates behave.  
- Makes learning digital logic **interactive** and **fun** with the micro:bit LEDs.  
- Allows children or students to experiment by pressing buttons and seeing immediate results.

## How to Use
1. Connect the BBC micro:bit to your computer.
2. Copy the `main.py` file to your micro:bit.
3. The micro:bit will start by displaying the current logic gate name.
4. **Switch gates**: Tap the logo to cycle through gates.
5. **Reset to first gate**: Shake the micro:bit.
6. Press buttons according to the selected logic gate to see the LEDs respond.

## Technologies
- MicroPython (for BBC micro:bit)
- BBC micro:bit v2

## Notes
- The XOR gate includes a short delay to debounce human button presses.
- LEDs clear automatically when the logic gate condition is not met.
- Designed for educational purposes, suitable for children or beginners learning digital logic.

## Author
Harry Edwards