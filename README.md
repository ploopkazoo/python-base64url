# python-base64url

URL-safe base64 codec

  + Replaces `+` with `-`
  + Replaces `/` with `_`
  + Removes `=` padding at end

Example:

    >>> base64url.base64urlencode("/ciN+g==")
    '_ciN-g'
    >>> base64url.base64urldecode("_ciN-g")
    '/ciN+g=='
