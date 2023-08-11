# AI-InvestiBot

## :small_orange_diamond: Table of Contents

- [Introduction](#small_orange_diamond-introduction)
- [Contact Us](#small_orange_diamond-before-you-begin)
- [Features](#small_orange_diamond-getting-started)
- [Planned Additions](#small_orange_diamond-installation-options)
- [How it works](#small_orange_diamond-how-it-works)
  - [Information Retrieval and Caching](#small_orange_diamond-information-handling)
  - [Unique Indicators in Models](#small_orange_diamond-unique-indicators)
  - [Stock Bot Functionality](#small_orange_diamond-functionality)
  - [Bot Selection Process](#small_orange_diamond-bot-selection)
  - [Earnings Processing](#small_orange_diamond-earnings-processing)
- [Comparing Models](#small_orange_diamond-compare-models)
- [Additional Information](#small_orange_diamond-additional-information)

# :small_orange_diamond-introduction: Introduction

This repository is currently under active development.The project aims to provide unique features that are not commonly found in other stock bots.

# :small_orange_diamond-before-you-begin: Contact Us
Discord: https://discord.gg/uHqBrqrr


# :small_orange_diamond-getting-started: Features

- **Unique Indicators**: The project includes unique indicators, which can be found in the `get_info.py` file.
- **Non-Daily Indicators**: Unlike most bots that rely on daily indicators, this project incorporates indicators that are not limited to daily data, such as earnings.
- **Flexible Model Creation**: Users have the freedom to create their own models using the `information_keys` feature.
- **Ingenious Method for Custom Models**: A callback function can be passed to the `train` function(traning the model) that creates the custom model. This allows you do use LSTMs, CNNs, Tranformers, or any type of model you want 
- **ResourceManager Class**: The `ResourceManager` class is implemented to manage and direct financial resources effectively.
- **Predictions for Multiple Companies**: This project offers predictions for multiple companies per day, rather than just one.
- **Holding Stocks**: The stock bot has the capability to hold stocks.
- **Lambda Version**: Allows the bot to be run without keeping a laptop open(It is also very, very cheap to use).
- **AI Techniques such as**:
  + Data Augmentation
  + Transfer learning
  + Early Stopping
  + More planned in the planned additions section
- **Active Development**: The project is actively being developed, with regular updates and improvements.


# :small_orange_diamond-installation-options: Planned Additions

The following features are planned to be added in the future:

- [ ] Achieving a 60% accuracy rate on previously untrained data.
- [x] Easy way to add many models using call backs
- [ ] Reach Library standards such as:
  - [ ] Bug Fixes
  - [ ] More Documentation
  - [ ] More Flexibility
  - [x] A better name




# :small_orange_diamond-how-it-works: How It Works

## :small_orange_diamond-information-handling: Information Retrieval and Caching

The project retrieves and caches information in the following manner:

- The `get_info.py` file processes all data obtained from yfinance.
- The information is stored as a dictionary in a JSON file.
- The `information_keys` feature retrieves values from each key in the JSON.

## :small_orange_diamond-unique-indicators: Unique Indicators in Models

The models in this project incorporate unique indicators as follows:

- Models utilize the `information_keys` attribute.
- These keys correspond to the names of indicators created from `get_info.py`.
- The model retrieves a dictionary from the JSON file and extracts the list associated with the key.
- Features in the form of NumPy arrays are then fed into the Sequential model.

## :small_orange_diamond-functionality: Stock Bot Functionality

The stock bot operates based on the following principles:

- Training, testing, saving, and loading are handled by separate functions.
- Training can be a test, using only the first 80% of data
- Information for each day is obtained through two methods:
  - Method 1: Offline (past data only)
    - Relies on data from `get_info.py`.
    - In this case, `model.cached_info` is always a dictionary or None.
  - Method 2: Online
    - Utilizes data from yfinance.
    - Once 280 days of past data are obtained, the oldest day is removed, and a new day is added at the end.
    - In this case, `model.cached_info` is always a pandas DataFrame or None.

## :small_orange_diamond-bot-selection: Bot Selection Process

The bot selects stocks based on the following criteria:

- The bot identifies the most promising stocks.
- It utilizes the available funds, following the rules set by the `ResourceManager` class.
- Stocks are held if their performance exceeds a certain threshold (`MAX_HOLD_INDEX`).
- Stocks are bought if specific conditions are met, including:
  - All models' profit ratios are above `PREDICTION_THRESHOLD`.
  - The average profit ratio exceeds the `RISK_REWARD_RATIO`.
- The lambda and loop implemenations use the same functions.
  - Therefore, more implementations can easily be added

## :small_orange_diamond-earnings-processing: Earnings Processing

The project processes earnings in the following manner:

- All earnings are obtained and separated into two lists: dates and the difference between actual and estimated values.
- During runtime, earnings outside of a specific range are removed.
- The processed earnings are transformed into a continuous list:
  - Earnings are represented as 0 if no earnings occurred on a specific day.
  - The difference between the expected and actual values is used when earnings occur.
- Certain limitations prevent the stock bot from detecting earnings in some cases, which is an issue currently being addressed.




# :small_orange_diamond-compare-models: Comparing Models

This project offers various models to choose from, including:

- Base Model: This is the parent class for all other models and has no data of its own unless specified.
- Day Trade Model:
  - Train RMSE: 0.02075242037941444
  - Test RMSE: 0.026771371361829204
  - Train RMSSE: 1.3539866279934776
  - Test RMSSE: 1.3284154118165579
- MACD Model:
  - Train RMSSE: 0.9503971603872557
  - Test RMSSE: 0.8466967848854924
- Impulse MACD Model:
  - Train RMSSE: 0.36591660531622144
  - Test RMSSE: 0.5035604190480721
- Reversal Model:
  - Train RMSSE: 0.42088951956685866
  - Test RMSSE: 0.5215137360642763
- Earnings Model:
  - Train RMSE: 0.023398385228929293
  - Test RMSE: 0.029933115015020682
  - Train RMSSE: 0.6544155735754877
  - Test RMSSE: 0.6228371371469489
- RSI Model:
  - Train RMSSE: 0.8791136390349061
  - Test RMSSE: 1.0664367975707776
- Breakout Model:
  - Train RMSE: 0.025379195809305734
  - Test RMSE: 0.030050545088518107
  - Train RMSSE: 0.6776019152138987
  - Test RMSSE: 0.8600297293130289

# :small_orange_diamond-additional-information: Additional Information

- The models were trained until it stopped improving
- RMSE (Root Mean Squared Error) represents the absolute errors between predictions and expected values. A lower RMSE indicates better accuracy.
- RMSSE (Root Mean Squared Scaled Error) accounts for variations in scale and magnitude among different stocks, enabling more meaningful comparisons across different time series. A lower RMSSE is desirable.
- Remember that the lower the value of these metrics, the better the performance.
