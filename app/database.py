from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)  # Connect to the database

async_session = sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

async def create_db_and_tables():
    from app.models.users import Base  # Import Base here to avoid circular imports
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Create all tables asynchronously
