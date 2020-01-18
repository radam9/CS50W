import json, requests

def goodreads(isbn):
    r = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "3tqMogqcx8dUmv2zxuw", "isbns": isbn})
    if r.status_code == 200:
        temp = r.json()
        rating = temp["books"][0]["work_ratings_count"]
        count = temp["books"][0]["average_rating"]
        return rating, count
    else:
        return [0, 0]
