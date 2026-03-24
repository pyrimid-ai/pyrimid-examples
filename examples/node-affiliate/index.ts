/**
 * Pyrimid Node.js Affiliate Agent
 * 
 * Discovers products in the Pyrimid catalog, purchases via x402,
 * and earns affiliate commissions — all onchain on Base.
 */

import { PyrimidClient } from '@pyrimid/sdk';

const AFFILIATE_ADDRESS = process.env.AFFILIATE_ADDRESS!;
const PRIVATE_KEY = process.env.PRIVATE_KEY!;

async function main() {
  const client = new PyrimidClient({
    rpcUrl: 'https://mainnet.base.org',
    privateKey: PRIVATE_KEY,
  });

  // 1. Browse the catalog
  console.log('Browsing Pyrimid catalog...');
  const products = await client.catalog.list();
  console.log(`Found ${products.length} products`);

  // 2. Filter for products with affiliate commissions
  const withCommission = products.filter(p => p.affiliateRate > 0);
  console.log(`${withCommission.length} products offer affiliate commissions`);

  if (withCommission.length === 0) {
    console.log('No commission products found');
    return;
  }

  // 3. Pick a product and purchase with affiliate attribution
  const product = withCommission[0];
  console.log(`\nPurchasing: ${product.name}`);
  console.log(`  Price: ${product.price} USDC`);
  console.log(`  Commission: ${product.affiliateRate}%`);
  console.log(`  Affiliate: ${AFFILIATE_ADDRESS}`);

  const receipt = await client.purchase({
    productId: product.id,
    affiliateAddress: AFFILIATE_ADDRESS,
  });

  console.log(`\n✅ Transaction: ${receipt.txHash}`);
  console.log(`   Vendor received: ${receipt.vendorAmount} USDC`);
  console.log(`   Affiliate earned: ${receipt.commission} USDC`);
  console.log(`   Protocol fee: ${receipt.protocolFee} USDC`);
}

main().catch(console.error);
