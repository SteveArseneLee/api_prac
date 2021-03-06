import requests

response = requests.get("https://www.nemoapp.kr/api/region/submunicipalities/{}")


def get_submunicipality_code(municipality_code):
    """
    법정동 코드로 행정동 코드 가져오는 함수
    `SEOUL_MUNICIPALITY_CODE` 변수에 정리 완료
    """
    res = requests.get(f"https://www.nemoapp.kr/api/region/submunicipalities/{b_dong_code}")
    if res.status_code != 200:
        raise Exception(f"[{res.status_code}] api requests fails")

    b_dong_list = res.json()

    if not b_dong_list:
        raise Exception("wrong municipality_code")

    return b_dong_list


def get_product(lng, lat, page=0, zoom=15):  # 126  # 37
    """
    매물 정보를 가져오는 함수
    """
    headers = {
        "authority": "www.nemoapp.kr",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "dnt": "1",
        "referer": "https://www.nemoapp.kr/Search?ArticleType=1&PageIndex=0&SWLng=126.97309390890551&SWLat=37.47424501269658&NELng=127.02601325584673&NELat=37.50761852998374&Zoom=15&mode=1&category=1&list=true&articleId=&dataType=",
        # 'request-context': 'appId=cid-v1:1a712dbb-d192-463e-b00b-18b83a52bb78',
        # 'request-id': '|ef7e599764504c8a9015095b37f24602.d948577b90b14056',
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        # 'traceparent': '00-ef7e599764504c8a9015095b37f24602-d948577b90b14056-01',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }

    params = {
        "Radius": "",
        "Latitude": "",
        "Longitude": "",
        "Building": "",
        "PageSize": "",
        "SortBy": "",
        "DepositMin": "",
        "DepositMax": "",
        "MRentMin": "",
        "MRentMax": "",
        "SaleMin": "",
        "SaleMax": "",
        "Premium": "",
        "PremiumMin": "",
        "PremiumMax": "",
        "DealType": "",
        "ArticleType": "1",
        "BuildingType": "",
        "PriceType": "",
        "SizeMin": "",
        "SizeMax": "",
        "MFeeMin": "",
        "MFeeMax": "",
        "Floor": "",
        "IsAllFloors": "",
        "Parking": "",
        "ParkingSlotMin": "",
        "ParkingSlotMax": "",
        "Interior": "",
        "Elevator": "",
        "IndependentSpaceCount": "",
        "Toilet": "",
        "BYearMin": "",
        "BYearMax": "",
        "RoofTop": "",
        "Terrace": "",
        "PantryRoom": "",
        "AirConditioner": "",
        "VR": "",
        "OfficeShare": "",
        "ShopInShop": "",
        "OpenLateNight": "",
        "Remodeling": "",
        "AddSpaceOffer": "",
        "BusinessField": "",
        "IsExclusive": "",
        "AgentId": "",
        "UserId": "",
        "PageIndex": page,
        "Region": "",
        "Subway": "",
        "StoreTrade": "",
        "CompletedOnly": "",
        "LBiz": "",
        "MBiz": "",
        "InitialExpMin": "",
        "InitialExpMax": "",
        "IsCommercialDistrictUnknown": "",
        "IsCommercialDistrictSubway": "",
        "IsCommercialDistrictUniversity": "",
        "IsCommercialDistrictOffice": "",
        "IsCommercialDistrictResidential": "",
        "IsCommercialDistrictDowntown": "",
        "IsCommercialDistrictSuburbs": "",
        "MoveInDate": "",
        "HeatingType": "",
        "SWLng": lng,
        "SWLat": lat,
        "NELng": lng + 1,
        "NELat": lat + 1,
        "Zoom": zoom,
    }

    res = requests.get("https://www.nemoapp.kr/api/articles/search/", params=params, headers=headers)
    if res.status_code != 200:
        raise Exception(f"[{res.status_code}] api requests fails")

    raw_data = res.json()
    return {"next": raw_data["hasNextPage"], "data": raw_data["items"]}
