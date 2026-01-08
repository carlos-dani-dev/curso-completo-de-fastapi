from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# cria uma localização para o banco de dados dentro da nossa aplicação FastAPI
SQLALCHEMY_DATABASE_URL="sqlite:///./todos.db"

# database engine permite a abertura de conexões com o banco de dados, para então ser usado
"""
"check_same_thread" => Permite que mais de uma thread se comunique com o banco de dados ao mesmo tempo.
Uma thread para cada requisição, nesse caso.
"""
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

"""
as sessões serão controladas 100% pelo programador.
O autocommit falso impede o commit automático de qualquer operação no banco de dados (qualquer operação
viraria uma transação isolada, o que não é ideal).
Além disso, o autoflush falso impede que as alterações sejam enviadas ao banco de dados automaticamente.
Vincula o sessionmaker à engine criada anteriormente.
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
Base é um objeto banco de dados que permite o controle do banco de dados.
Permite, por exemplo, a criação de tabelas do banco de dados (alterações estruturais).
"""
Base = declarative_base()