import numpy as np
import json
from collections import Counter
import os


def save_json(json_name, data):
    os.makedirs(os.path.dirname(json_name), exist_ok=True)
    with open(json_name, 'w', encoding='utf-8') as f_json:
        json.dump(data, f_json, indent=2)


if __name__ == '__main__':

    with open('eval_result/para_return_mehod.json', encoding='utf-8') as f:
        Equivalence_java = json.load(f)
    with open('eval_result/Name_overall_1.json', encoding='utf-8') as f:
        rq2_1 = json.load(f)
    with open('eval_result/Name_overall_2.json', encoding='utf-8') as f:
        rq2_2 = json.load(f)
    with open('eval_result/Name_overall_3.json', encoding='utf-8') as f:
        rq2_3 = json.load(f)
    with open('eval_result/generalization.json', encoding='utf-8') as f:
        Equivalence_python = json.load(f)


    print('*************')
    print('Section 4.1 results:')
    print('E_APIzator_java:', Equivalence_java['APIzator_Human'].count(1) / 2)
    print('E_APIzator_R_java:', Equivalence_java['APIzator_Human_R'].count(1) / 2)
    print('E_APIzator_P_java:', Equivalence_java['APIzator_Human_P'].count(1) / 2)

    print('E_Code2API_java:', Equivalence_java['Code2API_Human'].count(1) / 2)
    print('E_Code2API_R_java:', Equivalence_java['Code2API_Human_R'].count(1) / 2)
    print('E_Code2API_P_java:', Equivalence_java['Code2API_Human_P'].count(1) / 2)
    print('*************')

    best_APIs = [(i, j, k) for i, j, k in zip(rq2_1['best_API'], rq2_2['best_API'], rq2_3['best_API'])]

    best_API_vote = []
    for t in best_APIs:
        element_counts = Counter(t)
        most_common_elements = [element for element, count in element_counts.items() if
                                count == element_counts.most_common(1)[0][1]]
        if len(most_common_elements) != 1:
            print("The i-th data needs further inspection")
        else:
            best_API_vote.append(most_common_elements[0])

    print('Section 4.2 results:')
    print('Best API:1', best_API_vote.count(1))
    print('Best API:2', best_API_vote.count(2))
    print('Best API:3', best_API_vote.count(3))
    print('*************')


    method_name_APIzator = rq2_1['APIzator'] + rq2_2['APIzator'] + rq2_3['APIzator']
    method_name_Human = rq2_1['Human'] + rq2_2['Human'] + rq2_3['Human']
    method_name_Code2API = rq2_1['Code2API'] + rq2_2['Code2API'] + rq2_3['Code2API']

    print('APIzator:1', method_name_APIzator.count(1), round(method_name_APIzator.count(1) / 6, 1))
    print('APIzator:2', method_name_APIzator.count(2), round(method_name_APIzator.count(2) / 6, 1))
    print('APIzator:3', method_name_APIzator.count(3), round(method_name_APIzator.count(3) / 6, 1))
    print('APIzator:4', method_name_APIzator.count(4), round(method_name_APIzator.count(4) / 6, 1))
    print('avg_APIzator:', round(np.mean(method_name_APIzator), 2))
    print('*************')
    print('Human:1', method_name_Human.count(1), round(method_name_Human.count(1) / 6, 1))
    print('Human:2', method_name_Human.count(2), round(method_name_Human.count(2) / 6, 1))
    print('Human:3', method_name_Human.count(3), round(method_name_Human.count(3) / 6, 1))
    print('Human:4', method_name_Human.count(4), round(method_name_Human.count(4) / 6, 1))
    print('avg_Human:', round(np.mean(method_name_Human), 2))
    print('*************')
    print('Code2API:1', method_name_Code2API.count(1), round(method_name_Code2API.count(1) / 6, 1))
    print('Code2API:2', method_name_Code2API.count(2), round(method_name_Code2API.count(2) / 6, 1))
    print('Code2API:3', method_name_Code2API.count(3), round(method_name_Code2API.count(3) / 6, 1))
    print('Code2API:4', method_name_Code2API.count(4), round(method_name_Code2API.count(4) / 6, 1))
    print('avg_Code2API:', round(np.mean(method_name_Code2API), 2))

    print('*************')

    print('Section 4.3 results:')
    print('E_Code2API_python:', Equivalence_python['Code2API_Human'].count(1) / 1)
    print('E_Code2API_R_python:', Equivalence_python['Code2API_Human_R'].count(1) / 1)
    print('E_Code2API_P_python:', Equivalence_python['Code2API_Human_P'].count(1) / 1)
    print('*************')
