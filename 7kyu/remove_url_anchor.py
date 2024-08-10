# write a routine that returns the url with anything after the anchor (#)
#  removed.


def remove_url_anchor(url):
    return url[:url.index("#")] if '#' in url else url
