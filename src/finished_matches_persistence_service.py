from sqlalchemy import create_engine, MetaData
from src.data_base_directory.orm_sqlalchemy_create_table \
    import players, matches

metadata = MetaData()
