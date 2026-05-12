---
layout: default
lastmod: 2026-05-05
title: "Posts labelled mathematics"
description: "Blog posts labelled mathematics on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > mathematics

# mathematics

Posts labelled **mathematics**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'mathematics'" %}
{% include blog-entries.html posts=filtered %}
