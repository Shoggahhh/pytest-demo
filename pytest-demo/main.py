import httpx
import asyncio

from httpx import Response


async def main() -> Response:
    async with httpx.AsyncClient() as client:
        response = await client.get("https://petstore.swagger.io/v2/pet/1")
        return response

if __name__ == '__main__':
    asyncio.run(main())
