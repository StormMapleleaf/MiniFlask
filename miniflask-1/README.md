# MiniFlask
简单的基于 Flask 的 Web 应用框架

## 项目结构
```
miniflask
├── app
│   ├── config.py
│   ├── run.py
│   ├── controllers
│   ├── database
│   ├── routes
│   ├── services
│   └── utils
├── frontend
├── static
├── requirements.txt
└── .gitignore
```

## 依赖
- Flask

## 启动应用
在项目根目录下运行以下命令启动 Flask 应用：
```
python app/run.py
```

## 功能
该项目提供了一个简单的加法接口，用户可以通过 POST 请求 `/add` 来计算两个数字的和。请求体应为 JSON 格式，包含参数 `a` 和 `b`。