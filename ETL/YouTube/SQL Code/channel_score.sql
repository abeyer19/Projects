SELECT c.channel_id, 
	c.channel_name, 
	(c.channel_view_count/c.video_count) AS view_per_video, 
	CAST (AVG(c.channel_view_count/c.video_count) OVER (PARTITION BY c.channel_id) AS BIGINT) AS avg_view_per_video, 
	c.record_date
FROM channels as c
ORDER BY c.channel_id DESC;