#!/bin/bash
export PATH="/Users/nasa56/anaconda2/bin:$PATH"
source activate instagram-profile-crawler

cd /Users/nasa56/workspace-inta/instagram-profilecrawl-daily
export SETTING=BackfillLikeSettings
python crawl_profile_backfill.py $@
