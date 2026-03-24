# pyrimid-examples

Working examples for integrating with the [Pyrimid](https://pyrimid.ai) agent commerce protocol on Base.

Pyrimid adds affiliate commissions and revenue splitting to [x402](https://x402.org) payments. Agents discover products via MCP, pay with USDC, and earn commissions — all onchain.

## Examples

### 1. Node.js Affiliate Agent
An agent that discovers products in the Pyrimid catalog, promotes them, and earns commissions on successful referrals.

→ [`/examples/node-affiliate`](./examples/node-affiliate)

### 2. Python Affiliate Agent
Same flow in Python — discover, promote, earn.

→ [`/examples/python-affiliate`](./examples/python-affiliate)

### 3. OpenClaw Skill
Install this skill in [OpenClaw](https://openclaw.ai) and start earning Pyrimid commissions from your agent.

→ [`/examples/openclaw-skill`](./examples/openclaw-skill)

## Quick Start

```bash
npm install @pyrimid/sdk
```

```typescript
import { PyrimidClient } from '@pyrimid/sdk';

const client = new PyrimidClient({
  rpcUrl: 'https://mainnet.base.org',
  privateKey: process.env.PRIVATE_KEY,
});

// Browse the catalog
const products = await client.catalog.list();

// Purchase with affiliate attribution
const receipt = await client.purchase({
  productId: products[0].id,
  affiliateAddress: '0xYourAddress',
});

console.log(`Purchased! Commission: ${receipt.commission} USDC`);
```

## Architecture

```
Agent discovers product → Pyrimid Catalog (MCP)
Agent pays via x402     → USDC on Base
Commission splits       → CommissionRouter contract
Vendor gets paid        → Instant, onchain
Affiliate gets paid     → Instant, onchain
Protocol fee (1%)       → Treasury
```

## Links

- [Pyrimid SDK](https://www.npmjs.com/package/@pyrimid/sdk) — `@pyrimid/sdk`
- [Pyrimid MCP Server](https://smithery.ai) — 7 tools for agent discovery
- [MYA Directory](https://monetizeyouragent.fun) — Find earning opportunities
- [Documentation](https://pyrimid.ai)

## License

MIT
