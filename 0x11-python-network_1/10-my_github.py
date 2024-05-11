#!/usr/bin/python3
''' script that takes your GitHub credentials (username and password),
and uses th

    try:
        req = get(url, headers=header)
        req.raise_for_status()
        json = req.json()
        print(json['id'])
    except exceptions.HTTPError as e:
        print(None)
