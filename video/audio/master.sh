#!/usr/bin/env bash
# Master to -14 LUFS integrated with a STATIC gain + true-peak limiter (no dynamic loudnorm).
# The limiter runs 4x oversampled so it catches inter-sample (true) peaks; ceiling -1.5 dBFS.
set -euo pipefail
cd "$(dirname "$0")"
IN=score_raw.wav; OUT=score_master.wav; TARGET=-14
measure() { ffmpeg -hide_banner -nostats -i "$1" -af ebur128=peak=true -f null - 2>&1 | awk '/I:/{i=$2} /Peak:/{p=$2} END{print i, p}'; }
read I0 P0 < <(measure $IN); echo "raw: I=$I0 LUFS  TP=$P0 dBTP"
GAIN=$(awk -v t=$TARGET -v i=$I0 'BEGIN{print t-i}')
for pass in 1 2 3 4; do
  ffmpeg -v error -y -i $IN -af "volume=${GAIN}dB,aresample=192000,alimiter=limit=0.84:attack=1:release=60:level=disabled,aresample=48000" -c:a pcm_s24le $OUT
  read I P < <(measure $OUT); echo "pass $pass: gain=${GAIN}dB -> I=$I LUFS TP=$P dBTP"
  awk -v i=$I -v t=$TARGET 'BEGIN{exit !(i-t<0.2 && t-i<0.2)}' && break
  GAIN=$(awk -v g=$GAIN -v t=$TARGET -v i=$I 'BEGIN{print g+(t-i)}')
done
