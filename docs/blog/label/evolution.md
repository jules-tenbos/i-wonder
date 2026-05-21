---
layout: default
lastmod: 2026-05-21
title: "Posts labelled evolution"
description: "Blog posts labelled evolution on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > evolution

# evolution

Posts labelled **evolution**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'evolution'" | reverse %}
{% include blog-entries.html posts=filtered %}
