import smtplib #SMTP客户端
from email.header import Header  #支持中文的邮件头
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# ==================== 邮件配置 ====================
# 常用邮件服务器配置
# 126邮箱: smtp.126.com, 端口465
# QQ邮箱: smtp.qq.com, 端口465/587
# 163邮箱: smtp.163.com, 端口465
# Gmail: smtp.gmail.com, 端口465/587

# 加载.env文件
load_dotenv()

# 读取授权码
qq_auth = os.getenv('QQ_EMAIL_AUTH')

EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_USER = '1210326244@qq.com'
EMAIL_AUTH = qq_auth

def send_simple_email():
    '''发送文本邮件'''
    try:
        # 创建邮件对象
        email = MIMEMultipart()

        # 设置邮件头部信息
        # 发件人
        email['From'] = EMAIL_USER
        # 收件人
        email['To'] = 'fanfan6066@gmail.com'
        # 邮件主题
        email['Subject'] = Header('Python测试邮件', 'utf-8')

        # 邮件正文

        content = """您好！
这是一封来自Python程序的测试邮件。

祝好！
Python学习者"""

        # 添加邮件正文
        email.attach(MIMEText(content, 'plain', 'utf-8'))
        # 连接邮件服务器
        smtp_obj = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
        # 通过用户名和授权码登录
        smtp_obj.login(EMAIL_USER, qq_auth)
        # 发送邮件
        smtp_obj.sendmail(
            EMAIL_USER,
            ['fanfan6066@gmail.com'],
            email.as_string()
        )

        smtp_obj.close()
        print('✅ 简单文本邮件发送成功！')

    except Exception as e:
        print(f'❌ 邮件发送失败: {e}')

send_simple_email()