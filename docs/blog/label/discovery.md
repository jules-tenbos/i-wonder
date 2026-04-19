---
layout: default
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > discovery

# discovery

Posts labelled **discovery**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'discovery'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
