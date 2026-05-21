---
layout: default
lastmod: 2026-05-20
title: "Posts labelled preamble"
description: "Blog posts labelled preamble on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > preamble

# preamble

Posts labelled **preamble**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'preamble'" | reverse %}
{% include blog-entries.html posts=filtered %}
