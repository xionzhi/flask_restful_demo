"""
@Time    : 18-4-23 下午2:36
@Author  : xionzhi
@Desc    : 测试启动
"""

from service import app


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5002)
