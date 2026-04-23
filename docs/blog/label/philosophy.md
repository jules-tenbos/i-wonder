---
layout: default
title: "Posts labelled philosophy"
description: "Blog posts labelled philosophy on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > philosophy

# philosophy

Posts labelled **philosophy**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'philosophy'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
