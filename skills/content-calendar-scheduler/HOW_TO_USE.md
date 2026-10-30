# How to Use This Skill

Hey Claude, I just added the "content-calendar-scheduler" skill. Check our scheduled queue for gaps and build next week's calendar for our Facebook Page and TikTok at our best times.

## What you need

- **The InsightfulPipe MCP connected to Claude, with the Social Media Scheduler and your social accounts added.** The skill reads your queue and your post history itself; you don't export anything.
- **Your time zone.** Without it, every time is in UTC.
- **How often you want to post,** if you know. Without it, the skill uses each account's own pace over the last 90 days, and at least twice a week.
- **What to post about,** if you have it: blog post links, an announcement, or a calendar in Google Sheets, Notion or Airtable. Without it, the skill recycles your best past posts.
- **For a holidays and awareness days calendar:** what you sell, to whom, and which countries you post for. With DataForSEO connected, it also checks how many people search for each day.

## Example requests

**Queue check**
Hey Claude, I just added the "content-calendar-scheduler" skill. Review everything in our scheduler for the next two weeks. Show me gaps, clashes and anything that failed.

**Best time to post**
Hey Claude, I just added the "content-calendar-scheduler" skill. When should we post on TikTok, Instagram and our Facebook Page? Use our own numbers, in our own time zone.

**A week from the blog**
Hey Claude, I just added the "content-calendar-scheduler" skill. Turn these three blog posts into a week of posts for LinkedIn, Facebook and Threads, then schedule them as drafts once I approve.

**One announcement everywhere**
Hey Claude, I just added the "content-calendar-scheduler" skill. We launch on Tuesday. Write a version of this announcement for every connected network and stagger them through the morning.

**From our Notion calendar**
Hey Claude, I just added the "content-calendar-scheduler" skill. Read our Notion content calendar for October, flag the rows that aren't ready, and schedule the rest.

**Social media holidays calendar**
Hey Claude, I just added the "content-calendar-scheduler" skill. We run a bakery in Ohio. Build our social media holidays calendar for 2027: the national days and awareness days worth posting for, checked against Google Trends and how our Facebook and Instagram posts did on those days last year, with a post idea for each.

**Pause a campaign**
Hey Claude, I just added the "content-calendar-scheduler" skill. We paused the autumn promo. Find every scheduled post about it and pull them back to drafts after I check the list.

## What you get

1. **Queue health:** coverage, gaps, clashes, failed posts and the reason, stale drafts, and accounts that can't publish.
2. **What your history says:** how often each account really posts, and which weekdays and times beat that account's own average, with the post counts behind each one. When the numbers don't show a better time, it says so.
3. **The calendar:** one row per slot with the time, account, format, copy or brief, media, and whether it's ready or what it still needs.
4. **Ready-to-run payloads** for the slots that pass every network check.
5. **For a holiday calendar:** every candidate day with its date (and whether it still needs confirming), search interest, how your posts did on it last year, a post, optional or skip verdict, and a post idea for each pick.

## What it can change for you

With your yes on the exact list, it can:
- create the posts in the scheduler, as drafts first
- switch approved drafts to scheduled
- move posts to a better time
- edit a scheduled post's copy or media
- stop scheduled posts, for example for a paused campaign, by returning them to draft so nothing goes out

These need a Read & Write connection, and an owner, admin or operator can switch any of them off.

## Tips

- Run the queue check every Monday before you plan the week.
- Give it your time zone once and say it again in later requests.
- Best-time results need history. An account with fewer than 5 posts in a weekday or time block gets "not enough posts", not a guess.
