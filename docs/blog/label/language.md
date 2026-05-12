---
layout: default
lastmod: 2026-05-05
title: "Posts labelled language"
description: "Blog posts labelled language on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > language

# language

Posts labelled **language**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'language'" %}
{% include blog-entries.html posts=filtered %}
