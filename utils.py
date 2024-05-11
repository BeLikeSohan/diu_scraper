from urllib.parse import urlparse

allowed_url = "daffodilvarsity.edu.bd"
allowed_subdomains = ["daffodilvarsity", "faculty", "www", "admission"]
unallowed_types = ["pdf", "jpg", "jpeg", "png", "webp"]


def check_url(url: str):
    file_type = url.split(".")[-1]
    if file_type in unallowed_types:
        return False

    parsed_url = urlparse(url)

    sub_domain = parsed_url.netloc.split(".")[0]
    if sub_domain not in allowed_subdomains:
        return False

    domain = parsed_url.netloc
    allowed = domain.__contains__(allowed_url)
    return allowed


def sanitize_url(url: str):
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("/", "[SLASH]")
    return url
