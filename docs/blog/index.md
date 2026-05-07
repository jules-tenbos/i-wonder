---
layout: default
title: "In Wonder - The Conversation"
description: "In Wonder — SPLectrum's blog conversations. Exploring language, reality, philosophy, science and engineering from an interrelational pluralism view."
---

[Home](/) > In Wonder

# In Wonder - The Conversation

For more structured browsing of the posts, go to the [labels](label/) page.

{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
{% for post in sorted_posts %}
{% assign series = "discovery,language,mycelium,positioning,seed" | split: "," %}
{% assign img_start = post.content | split: 'src="' %}
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
