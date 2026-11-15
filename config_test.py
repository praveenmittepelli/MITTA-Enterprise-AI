from pydantic_settings import BaseSettings
from app.config import settings

print(settings().pinecone_index_name)
print(settings().embed_dim)
print(settings().bedrock_embedding_model)
print(settings().bedrock_chat_model)