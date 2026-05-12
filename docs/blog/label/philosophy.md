---
layout: default
lastmod: 2026-05-05
title: "Posts labelled philosophy"
description: "Blog posts labelled philosophy on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > philosophy

# philosophy

Posts labelled **philosophy**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'philosophy'" %}
{% include blog-entries.html posts=filtered %}
