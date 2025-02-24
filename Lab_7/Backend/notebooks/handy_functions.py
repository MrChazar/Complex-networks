from wykop import WykopAPI
import time


api = WykopAPI("w55988974f3d3194b7dd98c7ab2c6765c2", "05f093e009943e9e9b911f2a8a9f1a00")
api.authenticate()

def get_posts_and_comments(tag, pages):
    wpisy = []
    a = 1
    entries = ""
    while entries != []:
        time.sleep(1)
        try:
            entries = api.make_request(f"tags/{tag}/stream?page={a}&limit=25&sort=all&type=entry&multimedia=false'")
            entries = entries['data']
        except:
            continue
        for entry in entries:
            wpis = [entry['id'], entry['author']['username'], str(entry['content']), entry['tags'], entry['created_at']]
            wpisy.append(wpis)
            time.sleep(1)
            try:
                comments = api.make_request(f"entries/{entry['id']}/comments?page=1&limit=25")
            except:
                continue
            comments = comments['data']
            i = 2
            while comments != []:
                for comment in comments:
                    wpisy.append([comment['id'], comment['author']['username'], comment['content'], comment['tags'], entry['created_at'] ])
                try:
                    comments = api.make_request(f"entries/{entry['id']}/comments?page={i}&limit=25")
                except:
                    print("Przerwanie komentarzy")
                    break
                comments = comments['data']
                i += 1
        a += 1

        if a >= pages:
            break
    return wpisy