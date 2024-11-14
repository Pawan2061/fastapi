from sqlmodel import Field,SQLModel,create_engine,select,table
class User(SQLModel,table=True):
    id: int | None=Field(default=None,primary_key=True)

    username: str=Field(index=None)
    age: int | None=Field(default=None,index=True)


class ChainRequest(SQLModel,table=True):
    id: int | None=Field(default=None,primary_key=True)
    context: str=Field(index=None)
    question: str=Field(index=None)




DATABASE_URL="postgresql://Pawan2061:eTuqbHO0GJD8@ep-icy-fire-a52bon09.us-east-2.aws.neon.tech/twitter?sslmode=require"
engine=create_engine(DATABASE_URL,echo=True)
def create_database():
    SQLModel.metadata.create_all(engine)



    