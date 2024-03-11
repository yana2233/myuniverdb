from models import *


engine = create_engine("sqlite:///univer.db", paramstyle="pyformat")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
