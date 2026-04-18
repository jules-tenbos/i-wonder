---
layout: default
---

# In Wonder

The conversation. Where the thinking gets explored in the open.

{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
{% for post in sorted_posts %}
- **{{ post.date | date: "%B %d, %Y" }}** — [{{ post.title }}]({{ post.url }})
{% endfor %}
