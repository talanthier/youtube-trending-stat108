# Analysis of Trending Youtube Videos
## STAT 108
Repository for final project of STAT 108: Linear Regression

### Proposal
In this repository, I wish to explore how certain characteristics of a youtube video such as its title, upload time affect the success of a video such as a video's viewcount. One question is whether certain clickbait strategies applied to titles of thumbnails of videos really affect the view count of a video. Additionally do these strategies affect how viewers perceive the video. For example, do videos with clickbait titles end up having a lower like to dislike ratio? I would suspect that specific ways of formatting titles is associated with an increased viewcount. Simultaneously, I suspect these types of strategies used to grab a viewer's attention adversly affects the video's like to dislike ratio.

The dataset was obtained through [Kaggle](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset?select=RU_youtube_trending_data.csv). The dataset includes all videos that have been trending starting from August of 2020 and includes data on all trending videos up to the present. We have decided only to include trending videos from the US. For the purpose of this project, the data we will use is a simple random sample from the US trending videos dataset. We have also removed the description column as it will not be used in the analysis.

Structure of the Dataset is shown below. See data folder for more information on the dataset.
```
Rows: 982
Columns: 32
$ video_id          <chr> "05HuTGeF5AA", "SXrOuIhoslA", "hzwTq8ZZeyM", "Z6dwgWQz-Ck", "Fy7FsMBcUk8", "mtHRN9LpZ8g", "mM7C_Pw7OL8", "H8pM8PbtjfY", "~
$ title             <chr> "Khabib Nurmagomedov Announces Retirement | UFC 254", "TRYING MORE TIKTOK FOOD HACKS - Part 2", "Among Us But Impostor Ca~
$ publishedAt       <chr> "2020-10-24 21:27:37+00:00", "2020-09-26 15:33:12+00:00", "2021-04-04 17:00:14+00:00", "2021-01-19 18:00:08+00:00", "2020~
$ channelId         <chr> "UCvgfXK4nTYKudb0rFR6noLA", "UCjwmbv6NE4mOh8Z8VhPUx1Q", "UCMDtoPUno_f-puMpHL3Uuqg", "UCYJPby9DRCteedh5tfxVbrw", "UCbD8Epp~
$ channelTitle      <chr> "UFC - Ultimate Fighting Championship", "Rosanna Pansino", "STA Studios", "Smosh Pit", "Mnet K-POP", "More SypherPK", "To~
$ categoryId        <int> 17, 26, 20, 22, 24, 20, 27, 17, 10, 26, 17, 24, 20, 17, 27, 24, 10, 2, 1, 28, 10, 17, 10, 20, 1, 20, 17, 10, 22, 24, 22, ~
$ trending_date     <chr> "2020-10-27 00:00:00+00:00", "2020-09-30 00:00:00+00:00", "2021-04-10 00:00:00+00:00", "2021-01-23 00:00:00+00:00", "2020~
$ tags              <chr> "khabib|retires|nurmagomedov|retirement|annouces|ufc|254|ufc 254|reaction|interview|post|fight|octagon|jon|anik|justin|ga~
$ view_count        <int> 17992021, 710333, 1647002, 812308, 3662591, 801205, 647030, 598962, 2542185, 295733, 194239, 734852, 557620, 1231254, 693~
$ likes             <int> 461029, 36136, 49652, 51599, 248601, 30804, 58505, 13988, 200535, 14754, 5949, 9904, 63422, 24758, 20754, 3006, 11273, 45~
$ dislikes          <int> 10048, 619, 1676, 503, 2797, 618, 203, 456, 1492, 201, 98, 1444, 0, 336, 2804, 101, 179, 0, 794, 946, 218, 193, 133, 1770~
$ comment_count     <int> 50333, 4093, 2179, 2235, 10062, 2418, 1717, 1250, 17124, 495, 1053, 6117, 873, 4222, 5597, 487, 1015, 3014, 5535, 2589, 3~
$ comments_disabled <chr> "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "Fal~
$ ratings_disabled  <chr> "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "Fal~
$ description       <chr> "After defeating Justin Gaethje and improving to 29-0 at UFC 254, Khabib Nurmagomedov announced the performance would be ~
$ num_tags          <int> 252, 468, 7, 85, 93, 432, 59, 172, 406, 7, 44, 281, 7, 238, 453, 24, 64, 448, 394, 310, 160, 77, 94, 198, 143, 448, 456, ~
$ num_caps          <int> 7, 26, 7, 7, 38, 13, 7, 7, 16, 9, 4, 17, 5, 7, 12, 6, 3, 18, 8, 5, 7, 14, 7, 6, 9, 10, 17, 13, 7, 25, 3, 12, 14, 3, 41, 2~
$ num_exc           <int> 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0~
$ num_qm            <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0~
$ num_period        <int> 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0~
$ num_dollar        <int> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0~
$ title_length      <int> 50, 38, 37, 43, 64, 76, 42, 39, 83, 51, 54, 95, 38, 41, 47, 47, 25, 96, 66, 34, 40, 58, 56, 36, 44, 57, 79, 47, 42, 31, 2~
$ desc_length       <dbl> 986, 1131, 113, 1835, 64, 753, 866, 647, 648, 739, 440, 1433, 141, 1031, 4864, 685, 445, 4789, 1491, 651, 2319, 584, 2483~
$ weekday_published <int> 5, 5, 6, 1, 1, 1, 0, 1, 3, 0, 4, 6, 3, 1, 0, 2, 1, 0, 5, 1, 4, 2, 2, 6, 2, 2, 3, 2, 1, 3, 3, 6, 5, 0, 6, 2, 4, 6, 4, 2, 6~
$ day_published     <int> 24, 26, 4, 19, 3, 8, 30, 18, 17, 3, 12, 3, 6, 2, 2, 23, 1, 20, 3, 20, 23, 23, 27, 29, 16, 28, 4, 26, 10, 22, 1, 27, 23, 1~
$ hour_published    <int> 21, 15, 17, 18, 13, 6, 16, 17, 19, 22, 19, 6, 16, 18, 15, 16, 17, 17, 17, 13, 4, 6, 19, 12, 15, 19, 18, 18, 17, 16, 20, 2~
$ trending_age      <int> 3, 4, 6, 4, 9, 6, 1, 5, 5, 5, 4, 5, 1, 2, 4, 4, 3, 5, 1, 4, 2, 2, 4, 7, 5, 4, 3, 5, 3, 2, 6, 7, 4, 2, 3, 2, 2, 6, 1, 2, 3~
$ video_length      <dbl> 331, 1226, 524, 902, 351, 613, 287, 920, 233, 690, 1795, 322, 59, 592, 596, 133, 144, 2218, 1176, 1119, 143, 514, 311, 26~
$ subscriberCount   <int> 13300000, 13200000, 1130000, 7330000, 19300000, 1550000, 4910000, 922000, 36400, 424000, 96700, 600000, 1860000, 13300000~
$ videoCount        <int> 11340, 917, 124, 1548, 27360, 594, 648, 895, 52, 133, 2454, 307, 88, 11340, 127, 1746, 689, 507, 334, 1012, 87, 2840, 81,~
$ category          <chr> "Movies", "Horror", "Classics", "Documentary", "Family", "Classics", "Sci-Fi/Fantasy", "Movies", "Comedy", "Horror", "Mov~
$ channel_length    <int> 36, 15, 11, 9, 10, 13, 9, 12, 7, 8, 17, 17, 15, 36, 18, 4, 34, 8, 18, 13, 9, 10, 15, 12, 9, 14, 6, 17, 9, 13, 14, 7, 9, 1~
```
