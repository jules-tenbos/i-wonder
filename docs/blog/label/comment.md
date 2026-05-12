---
layout: default
lastmod: 2026-05-05
title: "Posts labelled comment"
description: "Blog posts labelled comment on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > comment

# comment

Posts labelled **comment**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'comment'" %}
{% include blog-entries.html posts=filtered %}
