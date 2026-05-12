---
layout: default
lastmod: 2026-05-05
title: "Posts labelled Wittgenstein"
description: "Blog posts labelled Wittgenstein on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > Wittgenstein

# Wittgenstein

Posts labelled **Wittgenstein**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'Wittgenstein'" %}
{% include blog-entries.html posts=filtered %}
