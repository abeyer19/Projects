 WITH videos_channels AS (
         SELECT videos.video_id,
            videos.video_title,
            videos.view_count::numeric AS view_count,
            videos.like_count::numeric AS like_count,
            videos.comment_count::numeric AS comment_count,
            videos.category_id,
            categories.category_title,
            videos.record_date,
            videos.channel_id AS video_channel_id,
            channels.channel_id AS channel_channel_id,
            channels.channel_name
           FROM videos
             LEFT JOIN channels ON videos.channel_id = channels.channel_id
             LEFT JOIN categories ON videos.category_id = categories.category_id
        )
 SELECT DISTINCT ON (videos_channels.video_id) videos_channels.video_id,
    videos_channels.video_title,
    videos_channels.view_count,
    videos_channels.like_count,
    videos_channels.comment_count,
    (videos_channels.like_count + videos_channels.comment_count) / videos_channels.view_count * 100::numeric AS engagement_rate,
    videos_channels.video_channel_id AS channel_id,
    videos_channels.channel_name,
    videos_channels.category_id,
    videos_channels.category_title,
    videos_channels.record_date
   FROM videos_channels
  ORDER BY videos_channels.video_id, videos_channels.record_date DESC;
