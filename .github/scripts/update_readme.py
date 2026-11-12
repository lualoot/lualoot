"""Perbarui bagian otomatis di README.md profil GitHub.

- Jika belum ada repositori publik  -> tampilkan teks "belum ada".
- Jika sudah ada                    -> isi otomatis (proyek unggulan + statistik).
Hanya memakai library bawaan Python.
"""
import json
import os
import re
import urllib.request
from datetime import datetime, timezone

USER = os.environ.get("GH_USER", "lualoot")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
README = "README.md"
MAX_FEATURED = 4
MAX_LANG_REPOS = 30

EMPTY_REPOS = (
    "> 🚧 **Belum ada proyek publik.** "
    "Script Lua SA-MP pertama akan segera hadir — pantau terus!"
)
EMPTY_STATS = (
    "> 📊 **Belum ada data statistik.** "
    "Akan muncul otomatis setelah repositori publik pertama dibuat."
)


def api(url):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "readme-updater",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def get_repos():
    repos, page = [], 1
    while True:
        batch = api(
            f"https://api.github.com/users/{USER}/repos"
            f"?per_page=100&page={page}&type=owner&sort=pushed"
        )
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    # Abaikan fork, arsip, dan repositori profil (nama sama dengan username)
    return [
        r for r in repos
        if not r["fork"]
        and not r["archived"]
        and r["name"].lower() != USER.lower()
    ]


def clean(text):
    return (text or "-").replace("|", "\\|").replace("\n", " ").strip()


def fmt_date(iso):
    return datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b %Y")


def build_repos(repos):
    if not repos:
        return EMPTY_REPOS
    top = sorted(
        repos, key=lambda r: (r["stargazers_count"], r["pushed_at"]), reverse=True
    )[:MAX_FEATURED]
    rows = [
        "| Repositori | Deskripsi | Bahasa | ⭐ | 🍴 | Update |",
        "|:--|:--|:-:|:-:|:-:|:-:|",
    ]
    for r in top:
        rows.append(
            f"| [**{r['name']}**]({r['html_url']}) "
            f"| {clean(r['description'])} "
            f"| {r['language'] or '-'} "
            f"| {r['stargazers_count']} "
            f"| {r['forks_count']} "
            f"| {fmt_date(r['pushed_at'])} |"
        )
    return "\n".join(rows)


def build_stats(repos):
    if not repos:
        return EMPTY_STATS

    user = api(f"https://api.github.com/users/{USER}")
    stars = sum(r["stargazers_count"] for r in repos)
    forks = sum(r["forks_count"] for r in repos)

    langs = {}
    for r in repos[:MAX_LANG_REPOS]:
        try:
            for lang, size in api(r["languages_url"]).items():
                langs[lang] = langs.get(lang, 0) + size
        except Exception:
            continue

    lines = [
        "| 📦 Repositori | ⭐ Total Bintang | 🍴 Total Fork | 👥 Pengikut |",
        "|:-:|:-:|:-:|:-:|",
        f"| **{len(repos)}** | **{stars}** | **{forks}** | **{user['followers']}** |",
    ]

    total = sum(langs.values())
    if total:
        lines += ["", "**Bahasa teratas**", "", "```text"]
        top = sorted(langs.items(), key=lambda x: x[1], reverse=True)[:5]
        width = max(len(n) for n, _ in top)
        for name, size in top:
            pct = size / total * 100
            filled = round(pct / 5)
            bar = "█" * filled + "░" * (20 - filled)
            lines.append(f"{name.ljust(width)}  {bar}  {pct:5.1f}%")
        lines.append("```")

    now = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M UTC")
    lines += ["", f"<sub>Diperbarui otomatis: {now}</sub>"]
    return "\n".join(lines)


def replace(text, name, body):
    pattern = re.compile(
        rf"(<!--START_SECTION:{name}-->)(.*?)(<!--END_SECTION:{name}-->)", re.S
    )
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def main():
    repos = get_repos()
    with open(README, encoding="utf-8") as f:
        text = f.read()
    text = replace(text, "repos", build_repos(repos))
    text = replace(text, "stats", build_stats(repos))
    with open(README, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Selesai. Repositori publik terdeteksi: {len(repos)}")


if __name__ == "__main__":
    main()
