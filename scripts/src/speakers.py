# stb lib
import json
import os

# third party imports
import requests

SPEAKERS_ENDPOINT = os.getenv("SPEAKERS_ENDPOINT")

SPEAKERS = [
    {
        "name": "Kyle Harrison",
        "avatar": "https://pbs.twimg.com/profile_images/591351050776502272/H6s459Ko_400x400.jpg",
        "bio": "Programmer, Tech Enthusiast, Maker, Geeky Dad",
        "contact": "apoclyps",
        "role": "Software Engineer",
        "topics": ["Python", "Backend", "Flask", "AWS"],
        "diversification": ["parenting"],
        "location": "Belfast",
        "source": "test",
    },
    {
        "name": "Ewa Grabowiecka",
        "avatar": "https://pbs.twimg.com/profile_images/988701324605820929/H5Hkrupc_400x400.jpg",
        "bio": "Shrug Life ¯\_(ツ)_/¯ Eva. Developer. CodeCraft organiser. I'm all for good software practises - diversity being one of them",
        "contact": "lost_semicolon",
        "role": "Software Developer",
        "topics": ["Python", "Django", "Backend"],
        "diversification": ["female"],
        "location": "Glasgow",
        "source": "test",
    },
]


def _post_payload(payload):
    r = requests.post(
        SPEAKERS_ENDPOINT,
        headers={"Content-type": "application/json"},
        data=json.dumps(payload),
    )
    print(r.status_code)


if __name__ == "__main__":
    try:
        for speaker in SPEAKERS:
            _post_payload(speaker)
    except Exception as e:
        print("An HTTP error %s occurred:\n" % (e))
