from os import getenv

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = getenv('DATABASE_URL')

engine = create_async_engine(DATABASE_URL)

# Crie uma sessão AsyncSession
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession)

# Para criar uma instância de sessão, use AsyncSessionLocal()
async_session = AsyncSessionLocal()
