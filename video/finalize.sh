#!/usr/bin/env bash
# Mux the mastered score onto a rendered picture and strip metadata down to the brand.
# usage: ./finalize.sh renders/raw-16x9.mp4 out/mojisola-oshinubi-16x9.mp4
set -euo pipefail
IN=$1; OUT=$2; mkdir -p "$(dirname "$OUT")"
ffmpeg -v error -y -i "$IN" -i audio/score_master.wav \
  -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 320k -ar 48000 -shortest \
  -map_metadata -1 -map_chapters -1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact \
  -metadata title="Mojisola Oshinubi — Operations Manager" \
  -metadata artist="Mojisola Oshinubi" \
  -metadata comment="mojisola-oshinubi.vercel.app" \
  -movflags +faststart "$OUT"
ffprobe -v error -show_entries format_tags:stream=codec_name,width,height,r_frame_rate,duration -of compact "$OUT"
ffmpeg -hide_banner -nostats -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | awk '/I:|Peak:/'
