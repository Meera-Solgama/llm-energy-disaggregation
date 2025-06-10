# llm-energy-disaggregation
llm-energy-disaggregation

## LLM Used
Groq Console (Model: Mistral / CodeLlama)

## Dataset
[UCI Household Power Consumption Dataset](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption)  
File used: `household_power_consumption.txt`

## Tasks Completed
This project demonstrates using natural language queries converted into executable Python code for energy data analysis using pandas. The following tasks were completed:

1. Calculated the average active power consumption in March 2007.
2. Found the hour of highest power usage on Christmas 2006.
3. Compared weekday vs weekend energy usage.
4. Identified days with energy usage above 5 kWh.
5. Plotted energy usage trend for the first week of January 2007.
6. Calculated average voltage for each day in the first week of February 2007.
7. Analyzed correlation between Global Active Power and sub-metering values.

## Requirements
- Python 3.7+
- pandas
- matplotlib
- seaborn

Install dependencies:
```bash
pip install pandas matplotlib seaborn
