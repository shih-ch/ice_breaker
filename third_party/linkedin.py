import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in {"people_also_viewed", "certifications"}
    }
    if data.get("groups"):
        for group_dict in data.get("greoups"):
            group_dict.pop("profile_pic_url")

    return data


# gist_response = requests.get("https://gist.githubusercontent.com/shih-ch/c835d4b1ef09c912069d18e50effaefb/raw/7ee78e570cfca9a5153a15721ed2024d854e94fc/eden.json")
# gist_response.json()['full_name']
