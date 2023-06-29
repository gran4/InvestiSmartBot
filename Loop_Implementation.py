"""
Name:
    Loop_implementation.py

Purpose:
    This module provides a loop implementation that is applied to the data
    in the models.

Author:
    Grant Yul Hur

See also:
    Other modules related to running the stock bot -> resource_manager, lambda_implementation
"""

import time, json
from threading import Thread
from Models import *
from datetime import datetime, timedelta

import numpy as np

TIME_INTERVAL = 5#86400# number of secs in 24 hours
TICKER = "AAPL"

model = ImpulseMACDModel()
model.load()
#model.get_stock_data_offline()

def run_loop() -> None:
    """This function will attempt to run the loop for the stock bot indefinitely."""
    temp = []
    print(model.end_date)
    start = model.data['Dates'].index(model.end_date)
    while len(temp) < 1000:
        model.update_cached_offline()
        input_data_reshaped = np.reshape(model.cached, (1, 60, model.cached.shape[1]))
        temp.append(model.predict(input_data_reshaped)[0][0])

        date_object = datetime.strptime(model.start_date, "%Y-%m-%d")
        next_day = date_object + timedelta(days=1)
        model.start_date = next_day.strftime("%Y-%m-%d")

        date_object = datetime.strptime(model.end_date, "%Y-%m-%d")
        next_day = date_object + timedelta(days=1)
        model.end_date = next_day.strftime("%Y-%m-%d")
    with open(f'{TICKER}/info.json') as file:
        data = json.load(file)
    temp_data = data['Close'][start:start+1000]

    together = []
    for predicted, real in zip(temp, temp_data):
        if predicted > 0 and real > 0:
            together.append(1)
        elif predicted < 0 and real < 0:
            together.append(1)
        else:
            together.append(0)
    print(sum(together)/len(together))



if __name__ == "__main__":
    # Create a new thread
    thread = Thread(target=run_loop)

    # Start the thread
    thread.start()
