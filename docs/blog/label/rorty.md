---
layout: default
---

# Rorty

Posts labelled **Rorty**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'Rorty'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
