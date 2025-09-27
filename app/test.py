errors = {
    "./test_source_code_2.py": [],
    "./source_code_2.py": [
        {
            "code": "E501",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
        {
            "code": "W292",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 100,
            "text": "no newline at end of file",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
    ],
    "./source_code_1.py": [
        {
            "code": "E702",
            "filename": "./source_code_1.py",
            "line_number": 3,
            "column_number": 74,
            "text": "multiple statements on one line (semicolon)",
            "physical_line": '        new_items = [f"{key} -> {value}" for key, '
            "value in items.items()]; return func(new_items)\n",
        },
        {
            "code": "E501",
            "filename": "./source_code_1.py",
            "line_number": 3,
            "column_number": 80,
            "text": "line too long (97 > 79 characters)",
            "physical_line": '        new_items = [f"{key} -> {value}" for key, '
            "value in items.items()]; return func(new_items)\n",
        },
        {
            "code": "E302",
            "filename": "./source_code_1.py",
            "line_number": 15,
            "column_number": 1,
            "text": "expected 2 blank lines, found 1",
            "physical_line": "def number_filter(func):\n",
        },
        {
            "code": "E303",
            "filename": "./source_code_1.py",
            "line_number": 27,
            "column_number": 1,
            "text": "too many blank lines (6)",
            "physical_line": "@number_filter\n",
        },
        {
            "code": "E501",
            "filename": "./source_code_1.py",
            "line_number": 31,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"\n",
        },
    ],
    "./test_source_code_1.py": [
        {
            "code": "E302",
            "filename": "./test_source_code_1.py",
            "line_number": 4,
            "column_number": 1,
            "text": "expected 2 blank lines, found 1",
            "physical_line": "@pytest.mark.parametrize(\n",
        },
        {
            "code": "E501",
            "filename": "./test_source_code_1.py",
            "line_number": 32,
            "column_number": 80,
            "text": "line too long (84 > 79 characters)",
            "physical_line": '            "decorate numbers: 1 -> 2, 2 -> 4, 6 -> 12, -111 -> -222, -50 -> -100!",\n',
        },
        {
            "code": "W292",
            "filename": "./test_source_code_1.py",
            "line_number": 112,
            "column_number": 6,
            "text": "no newline at end of file",
            "physical_line": "    )",
        },
    ],
}


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": linter_report[list(linter_report.keys())[0]],
            "path": list(linter_report.keys())[0],
            "status": "passed"
        },
    ] + [
        { "errors":
            [
                {
                    "line": result["line_number"],
                    "column": result["column_number"],
                    "message": result["text"],
                    "name": result["code"],
                    "source": "flake8"
                }
                for result in value
            ],
            "path": key,
            "status": "passed"
        }
        for key, value in list(linter_report.items())[1:]
    ]

def formatr_linter_report(linter_report: dict) -> list:
    output_dict = [{"errors": linter_report[list(linter_report.keys())[0]], "path": list(linter_report.keys())[0], "status": "passed"}]
    i = 1
    for key, value in list(linter_report.items())[1:]:
        output_dict.append({"errors": []})
        for result in value:
            output_dict[i]["errors"].append(
                {
                    "line": result["line_number"],
                    "column": result["column_number"],
                    "message": result["text"],
                    "name": result["code"],
                    "source": "flake8"
                }
            )
        output_dict[i].update(
            {
                "path": key,
                "status": "failed"
            }
        )
        i += 1
    return output_dict

print(format_linter_report(errors))
#
# array = [
#     {"errors": []},
#     {"errors": ["Old error"]}
# ]
#
# # Додаємо у другий словник
# array[1].update({1: 1})
#
# print(array)
#
#
# output = \
#     [
#         {
#             'errors': [],
#             'path': './test_source_code_2.py',
#             'status': 'passed'
#         },
#         {
#             'errors':
#                 [
#                     {
#                         'line': 18,
#                         'column': 80,
#                         'message': 'line too long (99 > 79 characters)',
#                         'name': 'E501',
#                         'source': 'flake8'
#                     },
#                     {
#                         'line': 18,
#                         'column': 100,
#                         'message': 'no newline at end of file',
#                         'name': 'W292',
#                         'source': 'flake8'
#                     }
#                 ],
#             'patch': './source_code_2.py',
#             'status': 'failed'
#         }
#     ]
#
#
#








# key, value = report_file.items()

# print(value])





# print(format_linter_report(linter_report=report_file))
# # The output will be:
# [
#     {
#         "errors": [],
#         "path": "./test_source_code_2.py",
#         "status": "passed"
#     },
#     {
#         "errors":
#             [
#                 {
#                     "line": 18,
#                     "column": 80,
#                     "message": "line too long (99 > 79 characters)",
#                     "name": "E501",
#                     "source": "flake8"
#                 },
#                 {
#                     "line": 18,
#                     "column": 100,
#                     "message": "no newline at end of file",
#                     "name": "W292",
#                     "source": "flake8"
#                 }
#             ],
#         "path": "./source_code_2.py",
#         "status": "failed"
#     }
# ]


# output = [
#     {
#         'errors': '[]',
#         'path': '',
#         'status': 'passed'
#     },
#     {
#         'errors':
#             [
#                 {
#                     'line': 'E501',
#                     'column': 80,
#                     'message': 'line too long (99 > 79 characters)',
#                     'name': 'E501',
#                     'source': 'flake8'
#                 }
#             ],
#     },
#     {
#         'errors':
#             [
#                 {
#                     'line': 'W292',
#                     'column': 100,
#                     'message': 'no newline at end of file',
#                     'name': 'W292',
#                     'source': 'flake8'
#                 }
#             ],
#         'path': './source_code_2.py',
#         'status': 'failed'
#     }
# ]


# return {"errors": [{"line": i["line_number"], "column": i["column_number"], "message": i["text"], "name": i["code"], "source": "flake8"} for i in errors], "path": file_path, "status": "failed"}

# print(format_linter_report(report_file))
# # The output will be:
# [
#     {
#         "errors": [],
#         "path": "./test_source_code_2.py",
#         "status": "passed"
#     },
#     {
#         "errors":
#             [
#                 {
#                     "line": 18,
#                     "column": 80,
#                     "message": "line too long (99 > 79 characters)",
#                     "name": "E501",
#                     "source": "flake8"
#                 },
#                 {
#                     "line": 18,
#                     "column": 100,
#                     "message": "no newline at end of file",
#                     "name": "W292",
#                     "source": "flake8"
#                 }
#             ],
#         "path": "./source_code_2.py",
#         "status": "failed"
#     }
# ]







# def format_single_linter_file(file_path: str, errors: list) -> dict:
#     return {"errors": [{"line": i["line_number"], "column": i["column_number"], "message": i["text"], "name": i["code"], "source": "flake8"} for i in errors], "path": file_path, "status": "failed"}
#
#
# format_single_linter_file("./source_code_2.py", errorss)
# print(format_single_linter_file(file_path="./source_code_2.py", errors=errors))
# # The output will be:
# {
#     "errors":
#         [
#             {
#                 "line": 18,
#                 "column": 80,
#                 "message": "line too long (99 > 79 characters)",
#                 "name": "E501",
#                 "source": "flake8"
#             },
#             {
#                 "line": 18,
#                 "column": 100,
#                 "message": "no newline at end of file",
#                 "name": "W292",
#                 "source": "flake8"
#             }
#         ],
#     "path": "./source_code_2.py",
#     "status": "failed"
# }

















# error = {
#     "code": "E501",
#     "filename": "./source_code_2.py",
#     "line_number": 18,
#     "column_number": 80,
#     "text": "line too long (99 > 79 characters)",
#     "physical_line": '    return f"I like to filter, rounding, doubling, '
#     "store and decorate numbers: {', '.join(items)}!\"",
# }
#
# output_dict = {
#     "line": error["line_number"],
#     "column": error["column_number"],
#     "message": error["text"],
#     "name": error["code"],
#     "source": "flake8"
# }
#
# print(output_dict)
#
# # print(format_linter_error(error=error))
# # # The output will be:
# # {
# #     "line": 18,
# #     "column": 80,
# #     "message": "line too long (99 > 79 characters)",
# #     "name": "E501",
# #     "source": "flake8"
# # }