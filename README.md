# Aroleid Research Backtesting Environment (ARBE)

Aroleid Research Backtesting Environment (ARBE) is a Python library for the rapid prototyping of price-based trading strategies.


## Backtesting Engine

### Core Architecture

The Aroleid Research Backtesting Environment (ARBE) is architected around a single abstract base class, `BacktesterBase`, which encapsulates the entire backtesting workflow. To implement a custom strategy, users subclass `BacktesterBase` and define the two required abstract methods: `add_indicators()` and `strategy()`. This design ensures that users do not need to reimplement the underlying mechanics of the backtesting engine and enforces a clear separation between infrastructure and strategy logic.

```python
# ...

class BacktesterBase(abc.ABC):
    
    # ...

    @abc.abstractmethod
    def add_indicators(self) -> None:
        pass

    @abc.abstractmethod
    def strategy(self, row: pd.Series) -> None:
        pass

    # ...
```

### Flow of Data

After the `BacktesterBase` class has been subclassed by the user by implementing the two necessary abstract methods, the historical market data can be loaded into a pandas dataframe from a local CSV file (in Databento format, see [Historical Market Data](#historical-market-data)) via the `load_historical_market_data()` method (an optional symbol filter can be applied if necessary).

```python
# ...

# Subclass BacktesterBase abstract base class and implement the two abstract methods
class Backtester(BacktesterBase):
    def add_indicators(self) -> None:
        # ...
        
    def strategy(self, row: pd.Series) -> None:
        # ...

# Instantiate the Backtester class and load historical market data
backtester = Backtester()
backtester.load_historical_data("path/to/csv/file.csv")
```


## Historical Market Data

The Aroleid Research Backtesting Environment (ARBE) is designed with compatibility with the [Databento](https://databento.com/) historical market data formats.
This does not necessarily mean that historical market data needs to be obtained from Databento, but rather that databento's schemas, dataformats, standards, and conventions are observed and data obtained from other sources is converted to the databento format before it is used within ARBE.

### CSV File Format

ARBE expects historical data to be provided in CSV format with the following columns:
- ts_event
- rtype
- open
- high
- low
- close
- volume
- symbol

To convert your existing CSV files to this format, you can use the `convert_csv_to_databento_format()` function from `arbe.data_conversion`.

### Record Types

ARBE supports the following Databento OHLCV bar types (the numbners correspond to Databento record type integer IDs):
- 1-second (32)
- 1-minute (33)
- 1-hour (34)
- 1-day (35)

These record types are used when loading historical price data for backtesting.
Unconventional record types are labelled as `Unknown (<rtype id>)`, but will not raise an error when attempting to load data.

## Planned Features and Known Limitations

### Data Conversion
- Implementation of `convert_csv_to_databento_format()` function
  - Currently, users must manually format their CSV files to match the required schema
  - Expected completion: Q3 2025

### Other Planned Features

Note: This list is subject to change based on user feedback and development priorities.

