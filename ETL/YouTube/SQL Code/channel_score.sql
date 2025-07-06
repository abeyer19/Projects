 SELECT DISTINCT ON (c.channel_id) c.channel_id,
    c.channel_name,
    c.channel_view_count / c.video_count AS view_per_video,
    avg(c.channel_view_count / c.video_count) OVER (PARTITION BY c.channel_id)::bigint AS avg_view_per_video,
    c.record_date
   FROM channels c
  ORDER BY c.channel_id, c.record_date DESC;
