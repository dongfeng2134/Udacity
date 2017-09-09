#-*- coding:utf-8 -*-
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org//wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=YPOJsEY7YWc")
avatar = media.Movie("Avatar",
                     "A marine on an `aline planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cX0R3mXaod8")
war_wolf2 = media.Movie("战狼2",
                       "票房神话，中国军魂",
                       "https://upload.wikimedia.org/wikipedia/en/b/b5/Wolf_Warriors_2_poster.jpeg",
                       "https://www.youtube.com/watch?v=KGNAlvAZjIY")
despicable = media.Movie("小黄人3",
                         "蒙蒙哒的xxx星人",
                         "https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg",
                         "https://www.youtube.com/watch?v=euz-KBBfAAo")
the_left_ear = media.Movie("左耳",
                    "青春校园的三角恋爱",
                    "https://upload.wikimedia.org/wikipedia/en/6/62/The_Left_Ear_film_poster.jpg",
                    "https://www.youtube.com/watch?v=O-fzWQCr5vI&list=PLGJw6JmbAkIyZbrXPXCvnI4rlQUGy-v6l")
Paths_of_the_Soul = media.Movie("冈仁波齐",
                                "西藏318国道的故事",
                                "https://upload.wikimedia.org/wikipedia/en/7/7f/Paths_of_the_Soul_poster.jpeg",
                                "https://www.youtube.com/watch?v=xXrieHUY_B0")
# Open browser and play trailer
#despicable.show_trailer()
movies = [toy_story,avatar,war_wolf2,despicable,the_left_ear,Paths_of_the_Soul]
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__dict__)
#fresh_tomatoes.open_movies_page(movies)
