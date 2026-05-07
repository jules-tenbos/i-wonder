---
layout: default
lastmod: 2026-05-05
title: "Posts labelled Rorty"
description: "Blog posts labelled Rorty on The World of SPLectrum."
---

[Home](/) > [In Wonder](/blog/) > [Labels](/blog/label/) > Rorty

# Rorty

Posts labelled **Rorty**.

{% assign filtered = site.posts | where_exp: "post", "post.labels contains 'Rorty'" %}
{% assign series = "discovery,language,mycelium,positioning,seed" | split: "," %}
{% for post in filtered %}
{% assign img_start = post.content | split: 'src="' %}
{% assign img_url = nil %}
{% if img_start.size > 1 %}
{% assign img_url = img_start[1] | split: '"' | first %}
{% endif %}
<div class="blog-entry">
{% if img_url %}<a href="{{ post.url }}"><img class="blog-thumb" src="{{ img_url | replace: 'w=350', 'w=80' | replace: 'h=230', 'h=80' }}" alt="" /></a>{% endif %}
<div class="blog-entry-text">
<strong><a href="{{ post.url }}">{{ post.title }}</a></strong> · {{ post.date | date: "%B %-d, %Y" }}{% for label in post.labels %}{% if series contains label %} · <a href="/blog/label/{{ label }}/">{{ label }} series</a>{% endif %}{% endfor %}<br/>
{% if post.description %}{{ post.description }}{% else %}{{ post.content | strip_html | truncatewords: 30 }}{% endif %}
</div>
</div>

{% endfor %}
