---
layout: default
lastmod: 2026-07-24
title: "Posts labelled formalisation"
description: "Blog posts labelled formalisation on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > formalisation

# formalisation

Posts labelled **formalisation**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'formalisation'" | reverse %}
{% include blog-entries.html posts=filtered %}
