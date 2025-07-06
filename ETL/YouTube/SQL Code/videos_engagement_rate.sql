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
        ),
engagements AS (
SELECT *,
(videos_channels.like_count + videos_channels.comment_count) / videos_channels.view_count * 100::numeric AS engagement_rate,
AVG((videos_channels.like_count + videos_channels.comment_count) / videos_channels.view_count * 100::numeric) OVER() AS avg_engagement_rate
FROM videos_channels
)
 SELECT DISTINCT ON (engagements.video_id) engagements.video_id,
    engagements.video_title,
    engagements.view_count,
    engagements.like_count,
    engagements.comment_count,
    engagements.engagement_rate,
    engagements.avg_engagement_rate,
    engagements.video_channel_id AS channel_id,
    engagements.channel_name,
    engagements.category_id,
    engagements.category_title,
    engagements.record_date
   FROM engagements
  ORDER BY engagements.video_id, engagements.record_date DESC;
