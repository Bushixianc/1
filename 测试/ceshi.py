import requests

# url="https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getTenserPlanDetail?guid=19e12baf-31e9-4a6b-98db-d58ff01ed53c"
# header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
# resp=requests.get(url,headers=header)
# print(resp.text)

a=list("""
[{'guid': '954af355-0761-4a7c-920c-50e0e8cf5bd7', 'projectName': None, 'projectCode': None, 'tenderProjectCode': 'GCJH202403200012', 'tenderProjectName': '昆明市东川区阿旺镇长岭子
2024年以工代赈项目', 'version': None, 'jyptid': '东川区', 'isdeleted': None, 'areaCode': '002', 'pv': None, 'creator': None, 'createTime': None, 'modifier': None, 'modifyTime':   
None, 'tradeType': 'gcjs', 'jyGuid': None, 'publishTime': '2024-03-20', 'regionCode': None, 'industryClassification': None, 'majorType': None, 'tenderMethod': None, 'infomationMet
hod': None, 'content': None, 'planNature': None, 'planNatureDesc': '正常', 'fileList': None, 'areaName': None, 'blockChainStatus': None, 'blockBaseDTO': None}, {'guid': '19e12baf-
31e9-4a6b-98db-d58ff01ed53c', 'projectName': None, 'projectCode': None, 'tenderProjectCode': 'GCJH202403200011', 'tenderProjectName': '昆明市滇池度假区大渔街道未搬迁村庄污水全收集
统（除海晏村）工程勘察、设计、施工总承包（EPC）', 'version': None, 'jyptid': '度假区', 'isdeleted': None, 'areaCode': '002', 'pv': None, 'creator': None, 'createTime': None, 'mo o
difier': None, 'modifyTime': None, 'tradeType': 'gcjs', 'jyGuid': None, 'publishTime': '2024-03-20', 'regionCode': None, 'industryClassification': None, 'majorType': None, 'tender
Method': None, 'infomationMethod': None, 'content': None, 'planNature': None, 'planNatureDesc': '正常', 'fileList': None, 'areaName': None, 'blockChainStatus': None, 'blockBaseDTO
': None}, {'guid': '98954243-ceb3-48e4-a529-15eaae9f3f19', 'projectName': None, 'projectCode': None, 'tenderProjectCode': 'GCJH202403200010', 'tenderProjectName': '昆明市滇池度假 
区大渔街道未搬迁村庄污水全收集系统（除海晏村）工程监理服务', 'version': None, 'jyptid': '度假区', 'isdeleted': None, 'areaCode': '002', 'pv': None, 'creator': None, 'createTime': 
None, 'modifier': None, 'modifyTime': None, 'tradeType': 'gcjs', 'jyGuid': None, 'publishTime': '2024-03-20', 'regionCode': None, 'industryClassification': None, 'majorType': None
, 'tenderMethod': None, 'infomationMethod': None, 'content': None, 'planNature': None, 'planNatureDesc': '正常', 'fileList': None, 'areaName': None, 'blockChainStatus': None, 'blo
ckBaseDTO': None}, {'guid': '722233d3-c426-4289-817c-4d869a2c9a74', 'projectName': None, 'projectCode': None, 'tenderProjectCode': 'GCJH202403200009', 'tenderProjectName': '昆明寻
供电局鸡街供电所建设项目施工招标', 'version': None, 'jyptid': '寻甸县', 'isdeleted': None, 'areaCode': '002', 'pv': None, 'creator': None, 'createTime': None, 'modifier': None,   
'modifyTime': None, 'tradeType': 'gcjs', 'jyGuid': None, 'publishTime': '2024-03-20', 'regionCode': None, 'industryClassification': None, 'majorType': None, 'tenderMethod': None, 
'infomationMethod': None, 'content': None, 'planNature': None, 'planNatureDesc': '正常', 'fileList': None, 'areaName': None, 'blockChainStatus': None, 'blockBaseDTO': None}, {'gui
d': 'f7faa34c-d633-4f69-9314-a736e638b82e', 'projectName': None, 'projectCode': None, 'tenderProjectCode': 'GCJH202403200008', 'tenderProjectName': '西山区50号片区城中村改造35KV高
线迁改项目（EPC）', 'version': None, 'jyptid': '西山区', 'isdeleted': None, 'areaCode': '002', 'pv': None, 'creator': None, 'createTime': None, 'modifier': None, 'modifyTime': N N
one, 'tradeType': 'gcjs', 'jyGuid': None, 'publishTime': '2024-03-20', 'regionCode': None, 'industryClassification': None, 'majorType': None, 'tenderMethod': None, 'infomationMeth
od': None, 'content': None, 'planNature': None, 'planNatureDesc': '正常', 'fileList': None, 'areaName': None, 'blockChainStatus': None, 'blockBaseDTO': None}, {'guid': 'cec019a3-7
ed6-4639-833d-e1018237cfdf', 'projectName': None, 'projectCode': None, 'tenderProjectCode': 'GCJH202403200007', 'tenderProjectName': '五华区2024年老旧小区及周边配套基础设施提升改 
造项目-道路部分设计施工总承包', 'version': None, 'jyptid': '五华区', 'isdeleted': None, 'areaCode': '002', 'pv': None, 'creator': None, 'createTime': None, 'modifier': None, 'modi
fyTime': None, 'tradeType': 'gcjs', 'jyGuid': None, 'publishTime': '2024-03-20', 'regionCode': None, 'industryClassification': None, 'majorType': None, 'tenderMethod': None, 'info
mationMethod': None, 'content': None, 'planNature': None, 'planNatureDesc': '正常', 'fileList': None, 'areaName': None, 'blockChainStatus': None, 'blockBaseDTO': None}, {'guid': '
0a3cd946-d9c5-476b-9ec1-1c85151b828d', 'projectName': None, 'projectCode': None, 'tenderProjectCode': 'GCJH202403200006', 'tenderProjectName': '五华区2024年老旧小区及周边配套基础 
设施提升改造项目-道路部分监理服务', 'version': None, 'jyptid': '五华区', 'isdeleted': None, 'areaCode': '002', 'pv': None, 'creator': None, 'createTime': None, 'modifier': None, '
modifyTime': None, 'tradeType': 'gcjs', 'jyGuid': None, 'publishTime': '2024-03-20', 'regionCode': None, 'industryClassification': None, 'majorType': None, 'tenderMethod': None, '
infomationMethod': None, 'content': None, 'planNature': None, 'planNatureDesc': '正常', 'fileList': None, 'areaName': None, 'blockChainStatus': None, 'blockBaseDTO': None}, {'guid
': '9d7defcc-0a54-416e-9c4d-867ce31e84b8', 'projectName': None, 'projectCode': None, 'tenderProjectCode': 'GCJH202403200005', 'tenderProjectName': '昆明禄劝供电局翠华、九龙、转龙 
三个供电所建设项目监理招标', 'version': None, 'jyptid': '禄劝县', 'isdeleted': None, 'areaCode': '002', 'pv': None, 'creator': None, 'createTime': None, 'modifier': None, 'modifyT
ime': None, 'tradeType': 'gcjs', 'jyGuid': None, 'publishTime': '2024-03-20', 'regionCode': None, 'industryClassification': None, 'majorType': None, 'tenderMethod': None, 'infomat
ionMethod': None, 'content': None, 'planNature': None, 'planNatureDesc': '正常', 'fileList': None, 'areaName': None, 'blockChainStatus': None, 'blockBaseDTO': None}, {'guid': '6d8
11ec7-a648-4245-8202-929ced8257b7', 'projectName': None, 'projectCode': None, 'tenderProjectCode': 'GCJH202403200004', 'tenderProjectName': '昆明禄劝供电局转龙供电所建设项目施工招
', 'version': None, 'jyptid': '禄劝县', 'isdeleted': None, 'areaCode': '002', 'pv': None, 'creator': None, 'createTime': None, 'modifier': None, 'modifyTime': None, 'tradeType': :
 'gcjs', 'jyGuid': None, 'publishTime': '2024-03-20', 'regionCode': None, 'industryClassification': None, 'majorType': None, 'tenderMethod': None, 'infomationMethod': None, 'conte
nt': None, 'planNature': None, 'planNatureDesc': '正常', 'fileList': None, 'areaName': None, 'blockChainStatus': None, 'blockBaseDTO': None}, {'guid': '33495b82-96e1-4cc5-aa4a-ea2
26a13433b', 'projectName': None, 'projectCode': None, 'tenderProjectCode': 'GCJH202403200003', 'tenderProjectName': '昆明禄劝供电局翠华供电所建设项目施工招标', 'version': None, 'j
yptid': '禄劝县', 'isdeleted': None, 'areaCode': '002', 'pv': None, 'creator': None, 'createTime': None, 'modifier': None, 'modifyTime': None, 'tradeType': 'gcjs', 'jyGuid': None,
 'publishTime': '2024-03-20', 'regionCode': None, 'industryClassification': None, 'majorType': None, 'tenderMethod': None, 'infomationMethod': None, 'content': None, 'planNature': None, 'planNatureDesc': '正常', 'fileList': None, 'areaName': None, 'blockChainStatus': None, 'blockBaseDTO': None}]
""")