# Data Dictionary
The dataset used in our analysis is sampled_data.csv. This is a random sample of 1000 videos from the Kaggle data linked. Each row represents a single video which has hit trending on Youtube. Some videos have been removed since they no longer exist. The original dataset can be found through [Kaggle](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset?select=RU_youtube_trending_data.csv). All variables after `ratings_disabled` were not included in the original dataset. The code for obtaining these variables can be found in [feature_generation.ipynb](feature_generation.ipynb). `video_length`, `subscriberCount`, and `videoCount` were obtained through the Youtube API. All other variables were obtained from performing operations on the original dataset.
```
Rows: 982
Columns: 29
$ video_id          <chr> video id 
$ title             <chr> video title 
$ publishedAt       <chr> date and time published
$ channelId         <chr> uploader channel id 
$ channelTitle      <chr> uploader channel name 
$ categoryId        <int> category id number (see US_category_id.json) 
$ trending_date     <chr> date when video trending 
$ tags              <chr> list of video tags 
$ view_count        <int> number of views 
$ likes             <int> number of likes 
$ dislikes          <int> number of dislikes 
$ comment_count     <int> number of dislikes 
$ thumbnail_link    <chr> link to thumbnail image 
$ comments_disabled <chr> comments are disabled (T/F) 
$ ratings_disabled  <chr> ratings are disablsed (T/F)
$ description       <chr> video description
$ num_tags          <int> number of tags
$ num_caps          <int> number of capital letters in title
$ num_exc           <int> number of exclamation points in title
$ num_qm            <int> number of question marks in title
$ num_period        <int> number of periods in title
$ num_dollar        <int> number of dollar signs in title
$ desc_length       <dbl> length of description (characters)
$ title_length      <int> length of title (characters)
$ weekday_published <int> day of week published (0 = Monday, 1 = Tuesday, ..., 6 = Sunday
$ day_published     <int> day of month published
$ hour_published    <int> hour of day published (UTC)
$ trending_age      <int> number of days between date published and date trending
$ video_length      <dbl> length of video in seconds
$ subscriberCount   <int> number of channel subscribers (approx)
$ videoCount        <int> number of videos on channel
$ category          <chr> category of video
$ channel_length    <int> length of channel name (characters)
```
