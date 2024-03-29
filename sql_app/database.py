from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://curso:sruiz094@localhost/db_clientes"
#SQLALCHEMY_DATABASE_URL =  "postgresql://db_sr:password@host.docker.internal:5440/DB_USERS_TEST"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
#connect_args={"check_same_thread": False}
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()