"""
setting中的配置默认为sqlite3数据库 当需要修改成MySql时
并且在setting.py的同级目录的__init__.py 加入如下配置
否则会报错： Error loading MySQLdb module.
"""
import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()

#django和mtsql版本不匹配的问题，参考https://blog.csdn.net/lpw_cn/article/details/103978909的评论