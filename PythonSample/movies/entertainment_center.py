import media

# show info of movie
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org//wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar",
                     "A marine on an `aline planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Post",
                     "https://movie.douban.com/trailer/125082/#content")
# Open browser and play trailer
avatar.show_trailer()