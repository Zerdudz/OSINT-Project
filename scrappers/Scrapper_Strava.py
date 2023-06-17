import json
import requests


class Scrapper_Strava:

    def __init__(self):
        pass

    def get_athletes(self, search_string, num_results=20):
        list_athletes = []

        s = requests.Session()
        cookies = {
            "_ga": "XXXX",
            "_ga_ESZ0QKJW56": "XXXX",
            "_gcl_au": "XXXX",
            "_gid": "XXXX",
            "_sp_id.047d": "XXXX",
            "_sp_id.f55d": "XXXX",
            "_sp_ses.047d": "XXXX",
            "_strava_cbv3": "XXXX",
            "_strava4_session": "XXXX",
            "CloudFront-Key-Pair-Id": "XXXX",
            "CloudFront-Policy": "XXXX",
            "CloudFront-Signature": "XXXX",
            "fbm_284597785309": "XXXX",
            "fbsr_284597785309": "XXXX",
            "sp": "XXXX",
            "xp_session_identifier": "XXXX"
        }

        s.cookies.update(cookies)

        r = s.get(
            f"https://www.strava.com/frontend/challenges/3819/leaderboard?category=country&sub_category={search_string}&limit=20")

        j = json.loads(r.content)

        for entry in j["entries"]:
            athlete = entry['athlete']
            print(athlete)
            print("-------------")
            new_athlete = {
                "id": athlete['id'],
                "nom": athlete['name'],
                "image_url": athlete['profile'],
                "url": f"https://www.strava.com/athletes/{athlete['id']}",
                "location": athlete['location']
            }
            list_athletes.append(new_athlete)

            if len(list_athletes) == num_results:
                break

            # on descend si pas assez

            athletes = {
                "items": list_athletes

            }

        return athletes
