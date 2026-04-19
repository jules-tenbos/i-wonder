---
layout: default
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > persona

# persona

Posts labelled **persona**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'persona'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
