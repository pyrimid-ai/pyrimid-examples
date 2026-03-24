# Pyrimid Affiliate

Earn commissions by discovering and promoting products on the Pyrimid agent commerce protocol.

## Trigger
Use when the user asks to: find earning opportunities, browse Pyrimid catalog, earn commissions, promote agent products, or check affiliate earnings.

## Tools Required
- web_fetch (for Pyrimid API)
- exec (for SDK operations)

## Steps

1. **Browse catalog**: Query `https://pyrimid.ai/api/catalog` for available products
2. **Filter by commission**: Look for products with `affiliateRate > 0`
3. **Present options**: Show the user available earning opportunities with rates
4. **Execute purchase**: When the user confirms, use the Pyrimid SDK to purchase with affiliate attribution
5. **Track earnings**: Log commissions to `memory/pyrimid-earnings.md`

## Example

```
User: "Find me something to earn on Pyrimid"
→ Browse catalog
→ "Found 15 products with commissions (10-30%). Top: Signal API ($0.25/call, 20% commission). Want me to set up affiliate tracking?"
```
