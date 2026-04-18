---
layout: default
---

# The Conversation

Where the thinking gets explored in the open. Posts on philosophy, science, engineering, and everything in between.

{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
{% for post in sorted_posts %}
- **{{ post.date | date: "%B %d, %Y" }}** — [{{ post.title }}]({{ post.url }})
{% endfor %}
