from flask import jsonify, request
from services import example_service

def add():
    """两数求和接口实现"""
    a = request.form.get('a')
    b = request.form.get('b')
    if a is None or b is None:
        return jsonify({"errors": "缺少参数a或b"}), 400
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return jsonify({"errors": "参数a和b必须为数字"}), 400

    # 调用服务层计算结果
    result = example_service.add_numbers(a, b)

    return jsonify({"result": result}), 200
