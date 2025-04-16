from arbe import Backtester
import pandas as pd


class DummyStrategy(Backtester):
    def add_indicators(self) -> None:
        pass

    def strategy(self, row: pd.Series) -> None:
        pass


if __name__ == "__main__":
    backtester = DummyStrategy()
    backtester.load_historical_market_data(
        ".././csv_port/glbx-mdp3-20241202-20241205.ohlcv-1s.csv"
    )
