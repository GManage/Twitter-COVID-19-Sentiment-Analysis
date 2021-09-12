import requests
import json

# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = ""

search_url = "https://api.twitter.com/2/tweets/search/all" # must have academic research access

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {
    "query": "vaccine OR (#vaccine OR #covid OR #covid19)", # https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
    "tweet.fields": "created_at, geo", # https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet
    "user.fields": "verified", # https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user
    # "expansions": "",
}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
