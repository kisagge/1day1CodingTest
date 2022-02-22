# 2022 Kakao Blind Recruitment - 신고 결과 받기
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dict = {}
    for item in report:
        From, To = item.split(' ')
        if To not in report_dict.keys():
            report_dict[To] = []
        if From not in report_dict[To]:
            report_dict[To].append(From)
    
    for id in id_list:
        if id in report_dict.keys() and len(report_dict[id]) >= k:
            for alr_id in report_dict[id]:
                answer[id_list.index(alr_id)] += 1
    return answer