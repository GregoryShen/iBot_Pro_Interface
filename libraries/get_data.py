import os
import json as json_parser


def get_data_path(case_path):
    """
    获取测试数据文件的绝对路径
    :param case_path: 测试用例文件的绝对路径
    :return: 测试数据文件的绝对路径
    """
    if "/" in case_path:
        case_path = case_path.replace("/", "\\")
    file_paths = os.path.dirname(case_path).split(os.sep + "api_test" + os.sep,
                                                  1)
    data_file_name = os.path.basename(case_path).replace('.py', '.json')
    data_file_path = os.sep.join([file_paths[0], 'data', file_paths[1],
                                  data_file_name])
    return data_file_path


def get_test_data(test_case_name, test_data_path):
    case = []
    payload = []
    expected = []
    with open(test_data_path, encoding='utf-8') as f:
        dat = json_parser.loads(f.read())
        test_case_info = dat[test_case_name]
        for td in test_case_info:
            case.append(td['case'])
            payload.append(td.get('payload', {}))
            expected.append(td.get('expected', {}))
    list_parameters = list(zip(case, payload, expected))
    return case, list_parameters

