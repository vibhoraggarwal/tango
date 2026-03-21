---
layout: page
title: Tango Events Calendar
permalink: /calendar/
---

# Stuttgart Tango Events Calendar

This calendar aggregates tango events from major Stuttgart venues and communities.

**Last updated:** {{ site.data.tango_events.last_updated }}
**Events found:** {{ site.data.tango_events.event_count }}
**Sources:** {{ site.data.tango_events.source_count }}

## Event Sources

{% for source in site.data.tango_events.sources %}

- [{{ source.name }}]({{ source.url }})
{% endfor %}

## Upcoming Events

{% if site.data.tango_events.event_count > 0 %}

| Date | Time | Event | Venue | Source |
|------|------|-------|-------|--------|
{% for event in site.data.tango_events.events %}
| {{ event.date }} | {{ event.time }} | {{ event.title }} | {{ event.venue }} | [{{ event.source }}]({{ event.source_url }}) |
{% endfor %}

{% else %}

<div class="alert alert-info">
  No events found yet. The scraper will collect events regularly. Check back soon!
</div>

{% endif %}

---

**Note:** This calendar is automatically updated weekly. [View the raw data]({{ site.github.repository_url }}/blob/main/_data/tango_events.json)
