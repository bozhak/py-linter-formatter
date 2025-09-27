def format_linter_error(error: dict) -> dict:
    return \
        {
            "line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"
        }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return \
        {
            "errors":
                [
                    {
                        "line": i["line_number"],
                        "column": i["column_number"],
                        "message": i["text"],
                        "name": i["code"],
                        "source": "flake8"
                    } for i in errors
                ],
            "path": file_path,
            "status": "passed" if not errors else "failed"
        }


def format_linter_report(linter_report: dict) -> list:
    return \
        (
            [
                {
                    "errors": linter_report[list(linter_report.keys())[0]],
                    "path": list(linter_report.keys())[0],
                    "status": "passed"
                },
            ] +
            [
                {
                    "errors":
                        [
                            {
                                "line": result["line_number"],
                                "column": result["column_number"],
                                "message": result["text"],
                                "name": result["code"],
                                "source": "flake8"
                            } for result in value
                        ],
                    "path": key,
                    "status": "passed" if not linter_report else "failed
                } for key, value in list(linter_report.items())[1:]
            ]
        )
