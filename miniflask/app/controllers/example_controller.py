from flask import jsonify, request
from app.services import example_service

def add():
    """两数求和接口实现"""
    data = request.json

    # 参数验证
    if not isinstance(data, dict):
        return jsonify({"errors": "请求体必须为JSON对象"}), 400
    if 'a' not in data or 'b' not in data:
        return jsonify({"errors": "缺少参数a或b"}), 400
    if not (isinstance(data['a'], (int, float)) and isinstance(data['b'], (int, float))):
        return jsonify({"errors": "参数a和b必须为数字"}), 400

    # 调用服务层计算结果
    result = example_service.add_numbers(data['a'], data['b'])

    return jsonify({"result": result}), 200
