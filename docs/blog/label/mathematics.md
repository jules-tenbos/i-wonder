---
layout: default
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > mathematics

# mathematics

Posts labelled **mathematics**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'mathematics'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
