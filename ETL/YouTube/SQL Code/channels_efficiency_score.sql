 WITH ces AS (
         SELECT c.channel_id,
            c.channel_name,
            c.channel_view_count,
            c.subscriber_count,
            c.video_count,
            c.record_date,
            c.channel_view_count / c.video_count * (c.subscriber_count / c.video_count) AS efficiency_score
           FROM channels c
        )
 SELECT DISTINCT ON (ces.channel_id) ces.channel_id,
    ces.channel_name,
    ces.channel_view_count,
    ces.subscriber_count,
    ces.video_count,
    ces.efficiency_score,
    ces.record_date
   FROM ces
  ORDER BY ces.channel_id, ces.record_date;
