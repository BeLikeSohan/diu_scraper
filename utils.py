from urllib.parse import urlparse

allowed_url = "daffodilvarsity.edu.bd"
unallowed_types = ["pdf", "jpg", "jpeg", "png", "webp"]


def check_url(url: str):
    file_type = url.split(".")[-1]
    if file_type in unallowed_types:
        return False
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain.__contains__(allowed_url)


def sanitize_url(url: str):
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("/", "[SLASH]")
    return url
