# Analysis of Trending Youtube Videos
## STAT 108
Repository for final project of STAT 108: Linear Regression

In this repository, I wish to explore how certain characteristics of a youtube video such as its title, upload time affect the success of a video such as a video's viewcount. One question is whether certain clickbait strategies applied to titles of thumbnails of videos really affect the view count of a video. Additionally do these strategies affect how viewers perceive the video. For example, do videos with clickbait titles end up having a lower like to dislike ratio? I would suspect that specific ways of formatting titles is associated with an increased viewcount. 

The dataset was obtained through [Kaggle](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset?select=RU_youtube_trending_data.csv). The dataset includes all videos that have been trending starting from August of 2020 and includes data on all trending videos up to the present. We have decided only to include trending videos from the US. For the purpose of this project, the data we will use is a simple random sample from the US trending videos dataset. We have also removed the description column as it will not be used in the analysis.

Structure of the Dataset is shown below.

Rows: 109,791
Columns: 16
$ video_id          <chr> "3C66w5Z0ixs", "M9Pmf9AB4Mo", "J78aPJ3VyNs", "kXLn3HkpjaA", "VIUo6yapDbc", "w-aidBdvZo8", "uet14uf9NsE", "ua4QMFQATco", "Sns~
$ title             <chr> "I ASKED HER TO BE MY GIRLFRIEND...", "Apex Legends | Stories from the Outlands â\200“ â\200œThe Endorsementâ\200\235", "I l~
$ publishedAt       <chr> "2020-08-11T19:20:14Z", "2020-08-11T17:00:10Z", "2020-08-11T16:34:06Z", "2020-08-11T16:38:55Z", "2020-08-11T15:10:05Z", "202~
$ channelId         <chr> "UCvtRTOMP2TqYqu51xNrqAzg", "UC0ZV6M2THA81QT9hrVWJG3A", "UCYzPXprvl5Y-Sf0g4vX-m6g", "UCbg_UMjlHJg_19SZckaKajg", "UCDVPcEbVLQ~
$ channelTitle      <chr> "Brawadis", "Apex Legends", "jacksepticeye", "XXL", "Mr. Kate", "Professor Live", "Les Do Makeup", "CGP Grey", "Louie's Life~
$ categoryId        <int> 22, 20, 24, 10, 26, 24, 26, 27, 24, 10, 22, 22, 20, 10, 23, 22, 24, 22, 26, 10, 28, 1, 24, 24, 22, 24, 10, 1, 10, 22, 27, 22~
$ trending_date     <chr> "2020-08-12T00:00:00Z", "2020-08-12T00:00:00Z", "2020-08-12T00:00:00Z", "2020-08-12T00:00:00Z", "2020-08-12T00:00:00Z", "202~
$ tags              <chr> "brawadis|prank|basketball|skits|ghost|funny videos|vlog|vlogging|NBA|browadis|challenges|bmw i8|faze rug|faze rug brother|m~
$ view_count        <int> 1514614, 2381688, 2038853, 496771, 1123889, 949491, 470446, 1050143, 1402687, 741028, 940036, 591837, 320872, 413372, 921261~
$ likes             <int> 156908, 146739, 353787, 23251, 45802, 77487, 47990, 89190, 95694, 113983, 87111, 44168, 14288, 26440, 124183, 4511, 10102, 3~
$ dislikes          <int> 5855, 2794, 2628, 1856, 964, 746, 440, 854, 2158, 4373, 1860, 409, 774, 293, 1678, 69, 7932, 197, 1425, 15174, 15818, 1120, ~
$ comment_count     <int> 35313, 16549, 40221, 7647, 2196, 7506, 4558, 6455, 6613, 5618, 7052, 2652, 2085, 1495, 16460, 673, 2763, 3666, 15773, 31039,~
$ thumbnail_link    <chr> "https://i.ytimg.com/vi/3C66w5Z0ixs/default.jpg", "https://i.ytimg.com/vi/M9Pmf9AB4Mo/default.jpg", "https://i.ytimg.com/vi/~
$ comments_disabled <chr> "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False"~
$ ratings_disabled  <chr> "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False"~
$ description       <chr> "SUBSCRIBE to BRAWADIS â–¶ http://bit.ly/SubscribeToBrawadis\n\nFOLLOW ME ON SOCIAL\nâ–¶ Twitter: https://twitter.com/Brawad~
