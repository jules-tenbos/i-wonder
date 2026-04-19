---
layout: default
---

# reality

Posts labelled **reality**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'reality'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
