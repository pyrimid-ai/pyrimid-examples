"""
Pyrimid Python Affiliate Agent

Discovers products in the Pyrimid catalog, purchases via x402,
and earns affiliate commissions — all onchain on Base.
"""

import os
import json
import httpx

PYRIMID_MCP_URL = "https://pyrimid.ai/api/mcp"
AFFILIATE_ADDRESS = os.environ["AFFILIATE_ADDRESS"]


async def main():
    async with httpx.AsyncClient() as client:
        # 1. Query the Pyrimid catalog via MCP
        print("Browsing Pyrimid catalog via MCP...")
        resp = await client.post(
            PYRIMID_MCP_URL,
            json={
                "method": "tools/call",
                "params": {
                    "name": "pyrimid_catalog_list",
                    "arguments": {"limit": 50},
                },
            },
        )
        products = resp.json().get("result", {}).get("content", [])
        print(f"Found {len(products)} products")

        # 2. Filter for affiliate opportunities
        with_commission = [
            p for p in products if p.get("affiliateRate", 0) > 0
        ]
        print(f"{len(with_commission)} offer affiliate commissions")

        if not with_commission:
            print("No commission products available")
            return

        # 3. Purchase with attribution
        product = with_commission[0]
        print(f"\nPurchasing: {product['name']}")
        print(f"  Price: {product['price']} USDC")
        print(f"  Commission: {product['affiliateRate']}%")

        purchase_resp = await client.post(
            PYRIMID_MCP_URL,
            json={
                "method": "tools/call",
                "params": {
                    "name": "pyrimid_purchase",
                    "arguments": {
                        "productId": product["id"],
                        "affiliateAddress": AFFILIATE_ADDRESS,
                    },
                },
            },
        )
        result = purchase_resp.json().get("result", {})
        print(f"\n✅ Transaction: {result.get('txHash')}")
        print(f"   Commission earned: {result.get('commission')} USDC")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
