ASCII Chart and Text Renderer

This repository contains two console utilities:

Text Renderer: A Python script to print styled and colored text to the console.

ASCII Chart: A Python script to generate simple ASCII bar charts from data points.

Installation

Prerequisites

Ensure you have Python installed on your system (Python 3.x recommended).

Installing Required Dependencies

Both scripts require colorama for colored text output. Install it using pip:

pip install colorama

Usage

Text Renderer

The text renderer prints styled text to the console. Example usage:

python text_renderer.py --text "Hello, World!" --color blue --style bold underline

Available colors:

black, red, green, yellow, blue, magenta, cyan, white

Available styles:

bold, dim, underline, normal

ASCII Chart Generator

This script generates ASCII bar charts from data points. Example usage:

python ascii_chart.py --data "A:10,B:20,C:15,D:35"

Each data point must be in the format label:value and separated by commas.

![image](https://github.com/user-attachments/assets/623adc6f-e324-4151-a887-9e1df8056ade)
