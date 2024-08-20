from typing import TypeVar, Union
import polars as pl

# 제네릭 타입 변수 정의
DataFrameType = TypeVar('DataFrameType', bound=Union[pl.DataFrame])