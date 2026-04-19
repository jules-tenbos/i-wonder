---
layout: default
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > Wittgenstein

# Wittgenstein

Posts labelled **Wittgenstein**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'Wittgenstein'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
