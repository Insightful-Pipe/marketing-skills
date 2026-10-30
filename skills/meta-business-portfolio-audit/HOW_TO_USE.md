# How to Use This Skill

Hey Claude, I just added the "meta-business-portfolio-audit" skill. Audit my Meta Business portfolio: what's connected to what, who has access, and anything that changed that we didn't do.

## What you need

- **The InsightfulPipe MCP connected to Claude, with Meta Ads added.** The skill reads your ad accounts, the business that owns each one, their Pages and Instagram accounts, datasets (pixels), catalogs, campaigns and the activity log itself. Without a connection, paste or describe the same things from Business settings and it runs the same checks.
- **Your People and Partners lists** from Business settings, Users. Meta doesn't give these to the connector, so without them the access review is marked unknown.
- **Who should have access:** the people and agencies you expect, who should hold full control, and anyone who has left.
- **If you think you were hacked:** the day you first noticed something odd, and the changes you made yourself in the last two weeks.

## Example requests

**Full audit**
Hey Claude, I just added the "meta-business-portfolio-audit" skill. Audit our Business portfolio. Here are the People and Partners lists from Business settings. Dana and Marcus should be the only admins.

**Setting up Business Manager**
Hey Claude, I just added the "meta-business-portfolio-audit" skill. We're setting up Facebook Business Manager for the first time. Check what we have so far and give me the setup checklist with what's still missing.

**Connecting a pixel to an ad account**
Hey Claude, I just added the "meta-business-portfolio-audit" skill. Our new ad account can't optimise for purchases. Check whether the pixel is connected to it and tell me how to connect it.

**Agency handover**
Hey Claude, I just added the "meta-business-portfolio-audit" skill. We're moving from one agency to another. Show me what the old agency still has access to and what the new one is missing.

**Suspected hack**
Hey Claude, I just added the "meta-business-portfolio-audit" skill. I think our Facebook ad account was hacked. There's a campaign I didn't create. Show me every change from the last two weeks and pause what isn't ours.

## What you get

1. **A grade out of 100,** with the math shown, across six areas: ownership and status, Pages and Instagram, datasets, catalogs, people and partners, and recent changes.
2. **A hack response first,** when you mark any change as not yours, with the daily budget someone else controls.
3. **A portfolio map:** each ad account with the business that owns it, the Pages and Instagram accounts it can use, the datasets shared with it and its live campaigns, then the catalogs.
4. **The top 5 fixes,** security first, each with the evidence and the exact place to fix it.
5. **A change review:** every change that moves money, delivery or access, grouped by campaign, for you to mark as yours or not.
6. **An access review** of every person and partner, and a list of orphan Pages, datasets and catalogs.
7. **A nine-line setup checklist,** each line done, missing or unknown, to use for a new business or an agency handover.

## What it can change for you

With your yes on the exact change, it can pause a live campaign created by a change you marked as not yours. It shows the payload first and checks the campaign's status after. Turning a campaign back on is done in Ads Manager.

Everything else stays with you, with the click path: connecting a dataset to an ad account, sharing Pages and catalogs, removing people and partners, two-factor, payment methods and spending limits.

## Tips

- Run it when an agency joins or leaves, and once a quarter otherwise.
- After a suspected hack, run it again the next day to confirm nothing new appeared.
- The activity log doesn't record who made a change, so the skill never decides on its own that a change was malicious. It asks you.
