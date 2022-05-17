import datetime
import logging
import requests

DATA_SEOUL_API_KEY = "41514341767265643534646b6f634c"  # 22.05.13

# 일반 인증키(Encoding)
DATA_GO_KR_EN = "goDElEv6gwXdZXibMpPYUHbm9fghO9emaUEGhx4Lu1Ycxj1t0liUCjYL97T9UtnS4qnfo8VkNOdbN94vO7Ce0g%3D%3D"
# 일반 인증키(Decoding )
DATA_GO_KR_DE = "goDElEv6gwXdZXibMpPYUHbm9fghO9emaUEGhx4Lu1Ycxj1t0liUCjYL97T9UtnS4qnfo8VkNOdbN94vO7Ce0g=="

DATA_GOV_URL = "https://api.odcloud.kr/api/{}"

SEOUL_URL = "http://openAPI.seoul.go.kr:8088/{}/{}/{}/{}/{}"

dt_kst = datetime.datetime.utcnow() + datetime.timedelta(hours=9)

YEAR = dt_kst.year

DEFAULT_HEADERS = {"Content-Type": "application/json; charset=utf-8"}

# 서울특별시
SEOUL_MUNICIPALITY_CODE = {
    "강남구": 11680,
    "강동구": 11740,
    "강북구": 11305,
    "강서구": 11500,
    "관악구": 11620,
    "광진구": 11215,
    "구로구": 11530,
    "금천구": 11545,
    "노원구": 11350,
    "도봉구": 11320,
    "동대문구": 11230,
    "동작구": 11590,
    "마포구": 11440,
    "서대문구": 11410,
    "서초구": 11650,
    "성동구": 11200,
    "성북구": 11290,
    "송파구": 11710,
    "양천구": 11470,
    "영등포구": 11560,
    "용산구": 11170,
    "은평구": 11380,
    "종로구": 11110,
    "중구": 11140,
    "중랑구": 11260,
}


DATA_GO_KR_API_KEYS = {
    # 소상공인시장진흥공단_서울 개업 현황
    1: "15069600/v1/uddi:2d1c3fef-b3c7-46b2-8e47-9fcc6ff74faa",
    # 소상공인시장진흥공단_상가(상권)정보
    # 서울특별시 자치구별 상권분석 정보(2017)
    2: "15083033/v1/uddi:324125cb-6185-41a8-9480-8be3a8e4a717",
    # 상권정보업종 코드집(2015년 12월)
    3: "15083033/v1/uddi:7cd9627d-c3c4-4688-8924-d49466c8c4ef_201805091704",
}


SEOUL_DATA_API_KEYS = {
    # https://data.seoul.go.kr/dataList/OA-15568/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권-생활인구)
    1: "VwsmTrdarFlpopQq",
    # https://data.seoul.go.kr/dataList/OA-15569/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권-직장인구)
    2: "VwsmTrdarWrcPopltnQq",
    # http://data.seoul.go.kr/dataList/OA-15582/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권배후지-생활인구)
    3: "VwsmTrdhlFlpopQq",
    # https://data.seoul.go.kr/dataList/OA-15570/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권배후지-직장인구)
    4: "Vwsm_TrdhlWrcPopltnQq",
    # https://data.seoul.go.kr/dataList/OA-15584/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권_상주인구)
    5: "VwsmTrdarRepopQq",
    # https://data.seoul.go.kr/dataList/OA-21278/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권-소득소비)
    6: "trdarNcmCnsmp",
    # http://data.seoul.go.kr/dataList/OA-15572/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권-추정매출)
    7: "VwsmTrdarSelngQq",
    # https://data.seoul.go.kr/dataList/OA-15573/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권배후지-추정매출)
    8: "VwsmTrdhlSelngQq",
    # https://data.seoul.go.kr/dataList/OA-15560/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권영역)
    9: "TbgisTrdarRelm",
    # https://data.seoul.go.kr/dataList/OA-15566/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권-아파트)
    10: "InfoTrdarAptQq",
    # https://data.seoul.go.kr/dataList/OA-15574/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권배후지-아파트)
    11: "VwsmTrdhlAptQq",
    # https://data.seoul.go.kr/dataList/OA-15567/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(자치구별 상권변화지표)
    12: "VwsmSignguIxQq",
    # https://data.seoul.go.kr/dataList/OA-15575/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(행정동별 상권변화지표)
    13: "VwsmAdstrdIxQq",
    # https://data.seoul.go.kr/dataList/OA-15576/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권-상권변화지표)
    14: "VwsmTrdarIxQq",
    # https://data.seoul.go.kr/dataList/OA-15577/S/1/datasetView.do
    # 서울시 우리마을가게 상권분석서비스(상권-점포)
    15: "VwsmTrdarStorQq",
    # https://data.seoul.go.kr/dataList/OA-20471/S/1/datasetView.do
    # 서울시 불법주정차/전용차로 위반 단속 CCTV 위치정보
    16: "TbOpendataFixedcctv",
    # https://data.seoul.go.kr/dataList/OA-13122/S/1/datasetView.do
    # 서울시 공영주차장 안내 정보
    17: "GetParkInfo",
    # http://data.seoul.go.kr/dataList/OA-15410/S/1/datasetView.do
    # 서울시 건축물대장 법정동 코드정보
    18: "bigCmpBjdongMgmInfo",
}





def get_openapi_seoul_data(service_key, start, end, type="json", year="", sub_info=""):
    req_url = SEOUL_URL.format(DATA_SEOUL_API_KEY, type, service_key, start, end)
    if year:
        req_url += f"/{year}"
    res = requests.get(url=req_url, headers=DEFAULT_HEADERS)

    if res.status_code != 200:
        logging.error(f"[{res.status_code}] api requests fails")
        return {}
    try:
        if type == "json":
            data = res.json().get(service_key, {})

        status = data["RESULT"]
        if status["CODE"] != "INFO-000":
            logging.error(f"[{status['CODE']}] {status['MESSAGE']}")
            return {}

        total_count = data.get("list_total_count", -1)
        result = data.get("row", [])

        res = {"count": total_count, "data": result}
        if year:
            res.update({"year": year})
        return res
    except Exception as e:
        logging.error(e.__str__())
        return {}


def get_odcloud_gov_data(service, page, size, type="json", sub_params={}):
    req_url = DATA_GOV_URL.format(DATA_GO_KR_API_KEYS.get(service))
    headers = {"accept": "application/json", "Authorization": DATA_GO_KR_EN}

    params = {"serviceKey": DATA_GO_KR_DE, "type": "json"}
    if sub_params:
        params.update({**sub_params})
    else:
        params.update({"page": page, "perPage": size})

    if type == "XML":
        params.update({"returnType": type, "type": type})

    res = requests.get(url=req_url, params=params, headers=headers)

    if res.status_code != 200:
        raise Exception(f"[{res.status_code}] api requests fails")

    data = res.json()

    total_count = data.get("currentCount", -1)
    result = data.get("data", [])

    return {"count": total_count, "data": result}


def get_all_openapi_data():
    result = list()
    ## 서울시 데이터는 정형화 되어 있음.
    for key, data_api_key in SEOUL_DATA_API_KEYS.items():
        try:
            start, limit = 0, 20
            while True:
                for year in [2017, 2018, 2019, 2020, 2021, 2022]:
                    res = get_openapi_seoul_data(
                        service_key=data_api_key,
                        start=start,
                        end=start + limit,
                        year=year,
                    )
                    if not res.get("data"):
                        break
                    res = {"key": key, **res}

                    result.append(res)  # 아니면 여기를 kafka producer와 연결해야 한다.
                start += limit

        except Exception as e:
            print(e)
            continue

    for key, data_api_key in DATA_GO_KR_API_KEYS.items():
        try:
            page, limit = 1, 20
            while True:
                res = get_odcloud_gov_data(
                    service_key=data_api_key,
                    page=page,
                    size=limit,
                )

                if not res.get("data"):
                    break
                res = {"key": key, **res}
                result.append(res)  # 아니면 여기를 kafka producer와 연결해야 한다.
            start += limit

        except Exception as e:
            print(e)
            continue

    return result

if __name__ == "__main__":
    # print(__name__)
    res = get_all_openapi_data()
    print(res)