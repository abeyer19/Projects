 WITH c AS (
         SELECT c.channel_id,
            c.channel_name,
            c.channel_view_count,
            c.subscriber_count,
            c.video_count,
            c.record_date
           FROM channels c
        ), vps AS (
         SELECT c.channel_id,
            c.channel_name,
            c.channel_view_count,
            c.subscriber_count,
            c.video_count,
            c.record_date,
            c.channel_view_count / c.subscriber_count AS views_per_sub,
            avg(c.channel_view_count / c.subscriber_count) OVER () AS avg_views_per_sub
           FROM c
        )
 SELECT DISTINCT ON (vps.channel_id) vps.channel_id,
    vps.channel_name,
    vps.channel_view_count,
    vps.subscriber_count,
    vps.video_count,
    vps.views_per_sub,
    vps.avg_views_per_sub,
    vps.record_date
   FROM vps
  ORDER BY vps.channel_id, vps.record_date;
