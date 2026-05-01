# Local Jekyll server

The local site runs in a Docker container using the `jekyll/jekyll:pages` image. It needs two fixes at startup: `webrick` (removed from Ruby 3 stdlib) and `PAGES_REPO_NWO` (the container can't see the host git remote since only `docs/` is mounted).

## Start

```
docker run --rm -d --name jekyll-tws \
  -p 4000:4000 -p 35729:35729 \
  -e PAGES_REPO_NWO=splectrum/the-world-of-splectrum \
  -v "/home/herma/splectrum/the-world-of-splectrum/docs:/srv/jekyll" \
  --entrypoint sh jekyll/jekyll:pages \
  -c "gem install webrick --no-document && jekyll serve --future --livereload --host 0.0.0.0"
```

- `--future` shows all scheduled (future-dated) posts, not just published ones.
- `--livereload` auto-refreshes the browser on file changes.
- Site serves at http://localhost:4000/.

## Stop

```
docker stop jekyll-tws
```

The `--rm` flag removes the container automatically on stop.

## Restart after reboot

The container does not survive a reboot. Run the start command again.

## Verify

```
curl -s -o /dev/null -w "%{http_code}" http://localhost:4000/
```

Returns `200` when the site is up.
