---
layout: default
---

# language

Posts labelled **language**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'language'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
