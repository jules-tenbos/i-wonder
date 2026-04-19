---
layout: default
---

# philosophy

Posts labelled **philosophy**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'philosophy'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
