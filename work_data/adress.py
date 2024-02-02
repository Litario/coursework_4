import pathlib
from pathlib import Path

base_dir: Path = pathlib.Path(__file__).resolve().parent.parent

data_currency = 'data/data_currency.json'
DATA_CURRENCY_PATH: Path = base_dir.joinpath(data_currency)

data_base = 'data/data_base.json'
DATA_BASE_PATH: Path = base_dir.joinpath(data_base)