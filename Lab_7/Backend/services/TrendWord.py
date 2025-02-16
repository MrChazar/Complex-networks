import services.WykopHandler as wh
import  services.WordTransform as wt
import  services.TrendDetection as td

def combine (tag_name, number_of_pages):
    posts = wh.get_posts_and_comments(tag_name, number_of_pages)
    print(posts)
    image = wt.generate_text_for_wordcloud(tag_name, number_of_pages, posts)
    print(image)
    trends = td.trend_detection(tag_name, number_of_pages, posts)
    print(trends)
    return {"trends": trends, "image": image}