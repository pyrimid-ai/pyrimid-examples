# How to Add Pyrimid to OpenClaw

Earn affiliate commissions from your OpenClaw agent in 3 minutes.

## Prerequisites
- [OpenClaw](https://openclaw.ai) installed and running
- A Base wallet with some ETH for gas

## Option 1: MCP Server (Recommended)

Add the Pyrimid MCP server to your OpenClaw config:

```json
{
  "mcp": {
    "servers": {
      "pyrimid": {
        "command": "npx",
        "args": ["-y", "@pyrimid/mcp-server"]
      }
    }
  }
}
```

Restart OpenClaw. Your agent now has 7 Pyrimid tools:

| Tool | Description |
|------|-------------|
| `pyrimid_catalog_list` | Browse all products |
| `pyrimid_catalog_search` | Search by category |
| `pyrimid_product_details` | Get product info + pricing |
| `pyrimid_purchase` | Buy with affiliate attribution |
| `pyrimid_vendor_register` | Register as a vendor |
| `pyrimid_vendor_list_product` | List your product |
| `pyrimid_earnings` | Check your commission earnings |

## Option 2: Direct SDK

```bash
npm install @pyrimid/sdk
```

```typescript
import { PyrimidClient } from '@pyrimid/sdk';

const client = new PyrimidClient({
  rpcUrl: 'https://mainnet.base.org',
  privateKey: process.env.PRIVATE_KEY,
});

const products = await client.catalog.list();

await client.purchase({
  productId: 'signal-api-btc',
  affiliateAddress: '0xYourWallet',
});
```

## Links

- [Pyrimid SDK](https://www.npmjs.com/package/@pyrimid/sdk)
- [MYA Directory](https://monetizeyouragent.fun)
- [Examples Repo](https://github.com/pyrimid-ai/pyrimid-examples)
