from weaviate.collections import Collection  # type: ignore
from weaviate.client import WeaviateClient  # type: ignore
from typing import Literal
from sentence_transformers import SentenceTransformer  # type: ignore
from typing import Union
from weaviate.collections.classes.internal import (  # type: ignore
    QueryNearMediaReturnType,
    QueryReturnType,
    Properties,
    References,
    TProperties,
    TReferences,
)  # type: ignore


class Retriever:
    """
    A class that represents a retriever for querying a collection.

    Args:
        client (WeaviateClient): The Weaviate client used for communication with the Weaviate server.
        collection_name (str): The name of the collection to query.

    Attributes:
        client (WeaviateClient): The Weaviate client used for communication with the Weaviate server.
        collection (Collection): The Weaviate collection to query.
        embedding (SentenceTransformer): The SentenceTransformer model used for encoding queries.

    Methods:
        query: Executes a query on the collection based on the specified search type.

    """

    def __init__(self, client: WeaviateClient, collection_name: str):
        self.client: WeaviateClient = client
        self.collection: Collection = self.client.collections.get(name=collection_name)
        self.embedding: SentenceTransformer = SentenceTransformer(
            "multi-qa-MiniLM-L6-cos-v1"
        )

    def query(
        self,
        query: str,
        search_type: Literal["keyword", "vector", "hybrid"] = "keyword",
        **kwargs
    ) -> Union[
        QueryReturnType[Properties, References, TProperties, TReferences],
        QueryNearMediaReturnType[Properties, References, TProperties, TReferences],
    ]:
        """
        Executes a query on the collection based on the specified search type.

        Args:
            query (str): The query string.
            search_type (Literal["keyword", "vector", "hybrid"], optional): The type of search to perform. Defaults to "keyword".
            **kwargs: Additional keyword arguments to be passed to the query method.

        Returns:
            Union[QueryReturnType[Properties, References, TProperties, TReferences], QueryNearMediaReturnType[Properties, References, TProperties, TReferences]]: The query result.

        """
        if search_type == "keyword":
            self.result: QueryReturnType[
                Properties, References, TProperties, TReferences
            ] = self.collection.query.bm25(
                query=query,
                **kwargs,
            )
        elif search_type == "vector":
            query_vector = self.embedding.encode(query)
            self.result: QueryNearMediaReturnType[Properties, References, TProperties, TReferences] = self.collection.query.near_vector(  # type: ignore
                near_vector=query_vector.tolist(),
                **kwargs,
            )
        elif search_type == "hybrid":
            query_vector = self.embedding.encode(query)
            self.result: QueryReturnType[Properties, References, TProperties, TReferences] = self.collection.query.hybrid(  # type: ignore
                query=query,
                vector=query_vector.tolist(),
                **kwargs,
            )

        return self.result
