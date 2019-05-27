#!/bin/bash
export PATH="/Users/nasa56/anaconda2/bin:$PATH"
source activate instagram-profile-explorer

cd /Users/nasa56/workspace-inta/instagram-profilecrawl-daily
export SETTING=ProfileStatsTrackerSetting
python profile_explorer.py
