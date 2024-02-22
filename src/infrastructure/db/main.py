from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.infrastructure.db.config import DBConfig


async def build_sa_engine(db_config: DBConfig) -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(db_config.full_url, echo=True, pool_size=50)
    yield engine

    await engine.dispose()


def build_sa_session_factory(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    session_factory = async_sessionmaker(
        bind=engine, autoflush=False, expire_on_commit=False
    )
    return session_factory
