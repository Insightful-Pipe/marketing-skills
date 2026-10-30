# How to Use This Skill

Hey Claude, I just added the "google-app-campaigns-manager" skill. Review my Google App campaigns and tell me what to cut, add or scale.

## What you need

- **Your app's store link** (Google Play, App Store or both).
- **A target cost per install or per action.** If you don't have one, give what a key in-app action is worth to you and the share of installers who complete it, and the skill derives the target with the math shown.
- **Your daily budget** and the countries you target.
- **Optional: the InsightfulPipe MCP connected to Claude,** with Google Ads and GA4 added. The skill then reads your App campaigns, assets, networks and in-app event volume itself, and reads your Google Play and App Store listing and reviews. Without it, paste the listing, some recent reviews and your campaign, asset and network reports.

## Example requests

**Plan a new campaign**
Hey Claude, I just added the "google-app-campaigns-manager" skill. Plan a Google App campaign for installs in the US for my Android app. Here's the Play link. Target cost per install is $1.50 and the budget is $100 a day.

**Installs or in-app actions?**
Hey Claude, I just added the "google-app-campaigns-manager" skill. Should my app install campaign move to in-app actions? Check whether my events have enough volume first.

**Review a running campaign**
Hey Claude, I just added the "google-app-campaigns-manager" skill. Review my App campaigns for the last 30 days by network and by asset, and tell me which assets to swap.

**Write the assets**
Hey Claude, I just added the "google-app-campaigns-manager" skill. Write 5 headlines and 5 descriptions for my App campaign from my store listing, and list the image and video sizes I still need.

## What you get

1. **A verdict per campaign:** goal, bidding, target, budget, whether the budget meets Google's ratio for that goal, and hold, scale, fix or keep.
2. **The goal choice,** with each condition checked against Google's own published guidance, quoted with its source and the date it was checked.
3. **Listing flags** that hold back installs, and review themes in plain words.
4. **Results by network and by asset,** with each asset marked cut, keep or keep learning, and the empty image and video slots.
5. **New text assets** with character counts and the listing fact behind each line, plus a brief for each missing image and video.
6. **The changes ready to run,** each payload marked "not run".

## What it can change for you

With your yes on the exact change, it can create an App campaign (always paused), choose the in-app events it optimises for, add or update App ads, add images, YouTube videos and a deep link, and change a budget or target once. It never turns a campaign on without a second yes, and never cycles bids up and down.

## Tips

- Give a change 7 to 14 days before judging it, and judge over 30 days.
- Link GA4 to your app's Firebase streams so the skill can count different users per event, which is how Google sizes the in-app actions check.
- Run it again after you swap assets to see the labels move.
