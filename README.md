# Analysis of Trending Youtube Videos
## STAT 108
Repository for final project of STAT 108: Linear Regression

### Proposal
In this repository, I wish to explore how certain characteristics of a youtube video such as its title, upload time affect the success of a video such as a video's viewcount. One question is whether certain clickbait strategies applied to titles of thumbnails of videos really affect the view count of a video. Additionally do these strategies affect how viewers perceive the video. For example, do videos with clickbait titles end up having a lower like to dislike ratio? I would suspect that specific ways of formatting titles is associated with an increased viewcount. 

The dataset was obtained through [Kaggle](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset?select=RU_youtube_trending_data.csv). The dataset includes all videos that have been trending starting from August of 2020 and includes data on all trending videos up to the present. We have decided only to include trending videos from the US. For the purpose of this project, the data we will use is a simple random sample from the US trending videos dataset. We have also removed the description column as it will not be used in the analysis.

Structure of the Dataset is shown below. See data folder for more information on the dataset.
```
Rows: 10,979
Columns: 15
$ video_id          <chr> "05HuTGeF5AA", "SXrOuIhoslA", "hzwTq8ZZeyM", "Z6dwgWQz-Ck", "Fy7FsMBcUk8", "mtHRN9LpZ8g", "mM7C_Pw7OL8", "H8pM8PbtjfY", "T~
$ title             <chr> "Khabib Nurmagomedov Announces Retirement | UFC 254", "TRYING MORE TIKTOK FOOD HACKS - Part 2", "Among Us But Impostor Can~
$ publishedAt       <chr> "2020-10-24T21:27:37Z", "2020-09-26T15:33:12Z", "2021-04-04T17:00:14Z", "2021-01-19T18:00:08Z", "2020-11-03T13:02:21Z", "2~
$ channelId         <chr> "UCvgfXK4nTYKudb0rFR6noLA", "UCjwmbv6NE4mOh8Z8VhPUx1Q", "UCMDtoPUno_f-puMpHL3Uuqg", "UCYJPby9DRCteedh5tfxVbrw", "UCbD8EppR~
$ channelTitle      <chr> "UFC - Ultimate Fighting Championship", "Rosanna Pansino", "STA Studios", "Smosh Pit", "Mnet K-POP", "More SypherPK", "Tom~
$ categoryId        <int> 17, 26, 20, 22, 24, 20, 27, 17, 10, 26, 17, 24, 20, 17, 27, 24, 10, 2, 1, 28, 10, 17, 10, 20, 1, 20, 17, 10, 22, 24, 22, 1~
$ trending_date     <chr> "2020-10-27T00:00:00Z", "2020-09-30T00:00:00Z", "2021-04-10T00:00:00Z", "2021-01-23T00:00:00Z", "2020-11-12T00:00:00Z", "2~
$ tags              <chr> "khabib|retires|nurmagomedov|retirement|annouces|ufc|254|ufc 254|reaction|interview|post|fight|octagon|jon|anik|justin|gae~
$ view_count        <int> 17992021, 710333, 1647002, 812308, 3662591, 801205, 647030, 598962, 2542185, 295733, 194239, 734852, 557620, 1231254, 6932~
$ likes             <int> 461029, 36136, 49652, 51599, 248601, 30804, 58505, 13988, 200535, 14754, 5949, 9904, 63422, 24758, 20754, 3006, 11273, 453~
$ dislikes          <int> 10048, 619, 1676, 503, 2797, 618, 203, 456, 1492, 201, 98, 1444, 0, 336, 2804, 101, 179, 0, 794, 946, 218, 193, 133, 1770,~
$ comment_count     <int> 50333, 4093, 2179, 2235, 10062, 2418, 1717, 1250, 17124, 495, 1053, 6117, 873, 4222, 5597, 487, 1015, 3014, 5535, 2589, 32~
$ thumbnail_link    <chr> "https://i.ytimg.com/vi/05HuTGeF5AA/default.jpg", "https://i.ytimg.com/vi/SXrOuIhoslA/default.jpg", "https://i.ytimg.com/v~
$ comments_disabled <chr> "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "Fals~
$ ratings_disabled  <chr> "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "Fals~
```
