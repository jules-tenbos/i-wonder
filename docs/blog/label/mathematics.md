---
layout: default
---

# mathematics

Posts labelled **mathematics**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'mathematics'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
