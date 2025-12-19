import requests

USERS = ["mangopy", "shizhl"]

headers = {
    "Accept": "application/vnd.github+json"
}

def count_stars(user):
    total = 0
    page = 1
    while True:
        r = requests.get(
            f"https://api.github.com/users/{user}/repos",
            params={"per_page": 100, "page": page},
            headers=headers,
            timeout=20
        )
        data = r.json()
        if not data:
            break
        total += sum(repo["stargazers_count"] for repo in data)
        page += 1
    return total

total_stars = sum(count_stars(u) for u in USERS)

with open("stars.json", "w") as f:
    f.write(f'{{ "total": {total_stars} }}')

print("Total stars:", total_stars)
