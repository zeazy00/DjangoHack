import views_model

def init():
    s1 = views_model.review.review_source()
    s1.name = "Ass&Dick"
    p1 = views_model.review.review()
    p1.text = "Assholes"
    p1.source = s1
    p1.sence = "bad"

    s1.save()
    p1.save()
