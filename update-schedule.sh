#!/usr/bin/env bash
set -euo pipefail

POSTS_DIR="docs/_posts"
TASKS_FILE="scheduled-tasks.md"
TODAY=$(date +%Y-%m-%d)

# Collect future/today posts: date|title|status
entries=()
for f in "$POSTS_DIR"/*.md; do
  date=$(grep -m1 '^date:' "$f" | sed 's/date: *//')
  [[ "$date" < "$TODAY" ]] && continue
  title=$(grep -m1 '^title:' "$f" | sed 's/title: *"//;s/"$//')
  status=$(grep -m1 '^status:' "$f" | sed 's/status: *//')
  entries+=("$date|$title|$status")
done

IFS=$'\n' entries=($(sort <<<"${entries[*]}")); unset IFS

# Build the schedule section grouped by month
schedule=""
current_month=""
for entry in "${entries[@]}"; do
  IFS='|' read -r date title status <<< "$entry"
  month=$(date -d "$date" +"%B")
  short_month=$(date -d "$date" +"%b")
  day=$(date -d "$date" +"%d" | sed 's/^0//')

  if [[ "$month" != "$current_month" ]]; then
    [[ -n "$current_month" ]] && schedule+=$'\n'
    schedule+="### $month"$'\n'
    schedule+=$'\n'
    schedule+="| Date | Title | Status |"$'\n'
    schedule+="|------|-------|--------|"$'\n'
    current_month="$month"
  fi
  schedule+="| $short_month $day | $title | $status |"$'\n'
done

# Replace everything between "## Posts" marker and "## Parked" marker
tmp=$(mktemp)
awk -v sched="$schedule" '
  /^## Post/ { print "## Post schedule\n"; printf "%s", sched; skip=1; next }
  /^## Parked/ { print ""; skip=0 }
  !skip { print }
' "$TASKS_FILE" > "$tmp"

mv "$tmp" "$TASKS_FILE"
echo "Schedule updated from $(echo "${entries[@]}" | wc -w) posts."
