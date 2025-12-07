# PANW-Hackathon

Setup:

To run the file, first export an OpenAI API key by running 
```export OPENAI_API_KEY="your_api_key_here"```
and set up the OpenAI SDK with
```pip install openai```

With parser.py and data.csv in the same folder, run
```python3 parser.py```
to run the file

Methodology:

I broke this problem down into two major steps: First, the code breaks down the CSV and cleans up the data using three GPT prompts, and second, it does data analysis on the highest spending volume by merchant and by date. OpenAI's API is used for the GPT prompts, and pandas is used to manage the CSV data so that it can be easily split up by column and cleaned. Generative AI was used for pandas documentation and to create the sample data, which I manually refined so that it would match the problem's requirements. Since there is no way to tell whether a date with unclear formatting, such as 2023-01-04, was on April 1st or January 4th, I made sure dates were not ambiguous to begin with, and were only formatted in ways that were possible to clean up. When doing data analysis, Python's built-in zip method is used to sync up the columns and find the largest amount by a certain key name.
