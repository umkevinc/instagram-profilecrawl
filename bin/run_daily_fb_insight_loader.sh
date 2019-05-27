#!/bin/bash
source /Users/nasa56/workspace/fb-insight/myenv/bin/activate

python /Users/nasa56/workspace/fb-insight/insight/app/page_summary_stats_crawler.py --basepath /Volumes/InvisibleDataDrive

python /Users/nasa56/workspace/fb-insight/insight/app/publisher/load_fb_summary_to_es.py --basepath /Volumes/InvisibleDataDrive --datetime $(date +"%Y%m%d") 
