# python-base64url

URL and filename-safe base64url codec as described by IETF

  + Replaces base64 `+` with `-`
  + Replaces base64 `/` with `_`
  + Removes base64 `=` padding at end

Example:

    >>> base64url.base64urlencode("/ciN+g==")
    '_ciN-g'
    >>> base64url.base64urldecode("_ciN-g")
    '/ciN+g=='
