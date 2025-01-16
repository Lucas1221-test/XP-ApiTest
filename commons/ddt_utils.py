
import yaml


def read_case_yaml(yaml_path, name):
    with open(yaml_path, encoding='utf-8', mode='r') as f:
        caseinfo = yaml.load(stream=f, Loader=yaml.FullLoader)
        case_list = []
        for case_dict in caseinfo:
            if "parametrize" in case_dict:
                new_cases = ''
                for new_case in new_cases:
                    if new_case['name'] == name:
                        case_list.append(new_case)
            elif case_dict['name'] == name:
                case_list.append(case_dict)
        if not case_list:
            # 如果没有找到匹配的项，抛出异常
            raise ValueError(f"未找到：{name},请检查路径:{yaml_path}是否正确")
        return case_list
