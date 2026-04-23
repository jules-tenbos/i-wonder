---
layout: default
title: "Posts labelled language"
description: "Blog posts labelled language on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > language

# language

Posts labelled **language**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'language'" %}
{% for post in filtered %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
