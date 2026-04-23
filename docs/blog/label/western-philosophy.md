---
layout: default
title: "Posts labelled western philosophy"
description: "Blog posts labelled western philosophy on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > western philosophy

# western philosophy

Posts labelled **western philosophy**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'western philosophy'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
