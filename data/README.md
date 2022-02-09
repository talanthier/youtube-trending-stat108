# Data Dictionary
The dataset used in our analysis is sampled_data.csv. This is a random sample of 1/10 of the original dataset and with the description column dropped. I plan on adding more features such as number of capital letters or punctuation in the title.
```
Rows: 10,979 
Columns: 15
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
```
