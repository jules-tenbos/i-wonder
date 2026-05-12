---
layout: default
lastmod: 2026-05-12
title: "Posts labelled category-theory"
description: "Blog posts labelled category-theory on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > category-theory

# category-theory

Posts labelled **category-theory**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'category-theory'" %}
{% include blog-entries.html posts=filtered %}
