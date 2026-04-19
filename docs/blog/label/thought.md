---
layout: default
---

# thought

Posts labelled **thought**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'thought'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
