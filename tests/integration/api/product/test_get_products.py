import json
import pytest
from dataclasses import asdict

from httpx import AsyncClient

from src.application.product.dto.products import ProductDTO


async def test_get_all_products_without_created(client: AsyncClient) -> None:
    response = await client.get("/product/all")

    assert response.json() == []


# TODO: pass test
@pytest.mark.skip
async def test_get_all_products_with_created(
    client: AsyncClient, created_product_dto: ProductDTO,
) -> None:
    created_product_serialized = json.loads(
        json.dumps(asdict(created_product_dto), default=str),
    )

    response = await client.get("/product/all")

    assert response.json() == [created_product_serialized]
