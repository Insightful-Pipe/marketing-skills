# How to Use This Skill

Hey Claude, I just added the "ga4-ecommerce-funnel" skill. Show me where shoppers drop out of my purchase funnel in GA4 and what it costs me.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property added.** The skill pulls the data itself; you don't need to export anything.
- **GA4 ecommerce events on your store,** such as `view_item`, `add_to_cart`, `begin_checkout` and `purchase`. If they aren't there, the skill tells you which ones are missing and what each one unlocks, instead of guessing.
- **Anything that changed recently,** like a new checkout or a price change, if you want it taken into account.

## Example requests

**Purchase funnel**
Hey Claude, I just added the "ga4-ecommerce-funnel" skill. Build my GA4 purchase funnel for the last 30 days and compare it with the 30 days before.

**Checkout drop-off**
Hey Claude, I just added the "ga4-ecommerce-funnel" skill. Where do people leave my checkout, and is mobile worse than desktop?

**Cart abandonment**
Hey Claude, I just added the "ga4-ecommerce-funnel" skill. How bad is my cart abandonment, and which products get added but not bought?

**Products, channels and order value**
Hey Claude, I just added the "ga4-ecommerce-funnel" skill. Which products and traffic sources make my revenue, and why did my average order value change?

## What you get

1. **A readiness check first:** which ecommerce events fire, whether purchases carry revenue, and whether the numbers can be trusted.
2. **The purchase funnel,** with each step's rate against the previous 30 days, and **the checkout steps by device** for the last 30 days.
3. **Cart and checkout abandonment,** both windows side by side.
4. **Product performance:** the top sellers, and the products people view but don't add, or add but don't buy.
5. **Revenue by traffic source** for the last 30 days, and **the average order value trend** month by month, with what drove each change in AOV.
6. **The top 3 leaks,** ranked by revenue at stake, each with the numbers and the assumption behind the estimate.

If your property has no ecommerce events, you get an honest "not graded", whether tracking was never set up or broke, and the setup plan in the order to build it.

## What it can change for you

With your yes on the exact change, it can mark `purchase` as a key event when it fires but isn't counted yet. It never changes your tags, never deletes anything, and leaves tracking changes to you or your developer.

## Tips

- Run it monthly, and right after any change to checkout, pricing or tracking.
- Judge the store against its own last month, not an industry average.
- With fewer than 30 purchases in the window, read the funnel as a direction, not a verdict.
