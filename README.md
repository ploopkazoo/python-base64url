# python-base64url

URL and filename-safe base64 codec as described by IETF

  + Replaces `+` with `-`
  + Replaces `/` with `_`
  + Removes `=` padding at end

Example:

    >>> base64url.base64urlencode("/ciN+g==")
    '_ciN-g'
    >>> base64url.base64urldecode("_ciN-g")
    '/ciN+g=='
