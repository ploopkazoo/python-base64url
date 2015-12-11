def base64urlencode(arg):
    stripped = arg.split("=")[0]
    filtered = stripped.replace("+", "-").replace("/", "_")
    return filtered
def base64urldecode(arg):
    filtered = arg.replace("-", "+").replace("_", "/")
    padded = filtered + "=" * ((len(filtered) * -1) % 4)
    return padded
