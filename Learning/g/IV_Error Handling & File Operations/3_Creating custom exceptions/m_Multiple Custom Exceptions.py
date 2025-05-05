"""
- Define two custom exceptions: InvalidURLError(ValueError) and UnsupportedSchemeError(InvalidURLError).
- Write a function validate_url(url: str) that checks:
    - If the URL does not contain "://", raise InvalidURLError("Missing scheme separator '://'").
    - Split the URL at "://" into scheme and rest. If the scheme (lowercase) is not "http" or "https", 
    raise UnsupportedSchemeError(f"Unsupported scheme: {scheme}").
    - If valid, print "URL scheme is supported."

- Write calling code that tests various URLs ("https://example.com", "ftp://example.com", "example.com", None) within a try...except structure 
that catches UnsupportedSchemeError first, then InvalidURLError, printing appropriate messages for each specific error. 
Use except Exception as e: at the end to catch any other unexpected errors (like AttributeError if None is passed)
"""

class InvalidURLError(ValueError):
    """Raised if '://' not in url"""
    pass
class UnsupportedSchemeError(InvalidURLError):
    """Raised if 'http' or 'https' not in url"""
    pass

def validate_url(url: str) -> None:
    """
    check if url is valid or raise an error

    Args:
        url:str

    Returns:
        None
    """
    if not isinstance(url, str):
        raise TypeError(f"Input must be a string, but got {type(url).__name__}")

    if '://' not in url:
        raise InvalidURLError(f"Error, '://' not in {url}")
    else:
        scheme = url.split('://')[0]
        if scheme != 'http' and scheme != 'https':
            raise UnsupportedSchemeError(f"Error, 'http' or 'https' not in {url}")
        else:
            print("URL scheme is supported.")

def main() -> None:
    """main function"""
    url_list = ["https://example.com", "ftp://example.com", "example.com", None,"http://example.fr"]

    for url in url_list:
        print(f"tested url : {url}")
        try:
            validate_url(url)
        except InvalidURLError as e:
            print(e)
        except UnsupportedSchemeError as e:
            print(e)
        except Exception as e:
            print(f"Error, {e}")

if __name__ == "__main__":
    main()