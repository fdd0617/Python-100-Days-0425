# Cronjob Response: Python百日学习-Daily
# (job_id: d7729588bd69)
# -------------

# ---

# ## 📬 Day 29 完成总结：Python 发送电子邮件

# 恭喜你完成了 Day 29！你已经掌握了使用 Python 发送邮件的核心技能。下面是今日知识点回顾：

# ### 🔑 核心知识点

# **1. smtplib 模块 — SMTP 客户端**
# - `smtplib.SMTP_SSL()` — 建立 SSL 加密的 SMTP 连接（端口 465）
# - `smtp_obj.login(user, auth_code)` — 用授权码登录邮箱
# - `smtp_obj.sendmail(from, to, msg)` — 发送邮件
# - `smtp_obj.close()` — 关闭连接

# **2. email 模块 — 构建邮件内容**
# - `MIMEMultipart()` — 创建多部分邮件对象（可同时包含文本和附件）
# - `MIMEText(content, 'plain'/'html', 'utf-8') — 创建文本/HTML 正文
# - `Header('主题', 'utf-8')` — 支持中文主题

# **3. 常用邮箱 SMTP 配置**
# | 邮箱 | SMTP 服务器 | 端口 |
# |------|------------|------|
# | QQ | smtp.qq.com | 465 |
# | 163 | smtp.163.com | 465 |
# | 126 | smtp.126.com | 465 |
# | Gmail | smtp.gmail.com | 465/587 |

# **4. 安全最佳实践**
# - 使用 `.env` 文件 + `python-dotenv` 管理授权码，不要硬编码
# - 授权码 ≠ 密码，需在邮箱设置中单独开启 SMTP 服务获取

# ---

### ✏️ 3 道练习题

# **练习 1：发送 HTML 格式邮件**

# 编写一个函数 `send_html_email()`，发送一封 HTML 格式的邮件。要求：
# - 邮件正文包含 HTML 内容（标题用 `<h1>`，正文用 `<p>`，加一个带样式的表格展示你的课程进度）
# - 使用 `MIMEText(content, 'html', 'utf-8')` 替换 `'plain'`
# - 收件人和邮箱配置从 `.env` 文件读取

# ```python
# # 提示：HTML正文示例
# html_content = """
# <h1 style="color: #333;">Python 学习进度报告</h1>
# <table border="1" cellpadding="8" style="border-collapse: collapse;">
#     <tr><th>阶段</th><th>内容</th><th>状态</th></tr>
#     <tr><td>Day 21-25</td><td>文件操作</td><td>✅ 完成</td></tr>
#     <tr><td>Day 26-28</td><td>Office/PDF/图像</td><td>✅ 完成</td></tr>
#     <tr><td>Day 29</td><td>发送邮件</td><td>✅ 完成</td></tr>
# </table>
# """
# ```




import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv



load_dotenv()

EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_USER = '1210326244@qq.com'
EMAIL_AUTH = os.getenv('QQ_EMAIL_AUTH')

def send_email():
    """发送"""
    try:
        email = MIMEMultipart()

        email['From'] = EMAIL_USER
        email['To'] = 'fanfan6066@gmail.com'
        email['Subject'] = Header('Python 学习进度报告', 'utf-8')


        # HTML格式的邮件内容
        html_content = """
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; }
                h2 { color: #2c3e50; }
                .progress { background-color: #3498db; color: white; padding: 10px; }
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #3498db; color: white; }
            </style>
        </head>
        <body>
            <h2>📊 Python 100天学习进度</h2>
            <div class="progress">
                <p><strong>当前进度：Day 29 / 100</strong></p>
            </div>

            <h3>已完成内容：</h3>
            <table>
                <tr>
                    <th>Day</th>
                    <th>主题</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td>Day 21</td>
                    <td>文件读写和异常处理</td>
                    <td>✅ 完成</td>
                </tr>
                <tr>
                    <td>Day 27</td>
                    <td>PDF文件操作</td>
                    <td>✅ 完成</td>
                </tr>
                <tr>
                    <td>Day 29</td>
                    <td>发送邮件和短信</td>
                    <td>🔄 进行中</td>
                </tr>
            </table>

            <p><strong>继续加油！💪</strong></p>
            <hr>
            <p style="color: #7f8c8d; font-size: 12px;">
                此邮件由Python程序自动生成
            </p>
        </body>
        </html>
        """


        email.attach(MIMEText(html_content, 'html', 'utf-8'))

        smtp_obj = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)

        smtp_obj.login(EMAIL_USER, EMAIL_AUTH)

        smtp_obj.sendmail(EMAIL_USER, ['fanfan6066@gmail.com'], email.as_string())

        smtp_obj.close()

        print('✅ 简单文本邮件发送成功！')
    except Exception as e:
        print(f'❌ 邮件发送失败: {e}')

send_email()

# **练习 2：批量发送邮件**

# 编写一个函数 `send_bulk_emails(recipients, subject, content)`，实现批量发送功能：
# - `recipients` 是一个邮箱列表（如 `['a@qq.com', 'b@163.com']`）
# - 只建立一次 SMTP 连接，在循环中发送给每个收件人
# - 添加发送成功/失败的统计，最后打印：`成功: X 封, 失败: Y 封`
# - 使用 `try-except` 处理单个发送失败不影响其他邮件

import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# 加载配置文件
load_dotenv()

# 设置邮件服务器
EMAIL_HOST = 'smtp.qq.com'
# 设置邮件端口
EMAIL_PORT = 465
# 设置发件账号
EMAIL_USER = '1210326244@qq.com'
# 读取配置文件授权码
EMAIL_AUTH = os.getenv('QQ_EMAIL_AUTH')


# 创建批量发送函数
def send_bulk_emails(recipients, subject, content):
    """批量发送"""
    # 统计变量
    success_count = 0
    fail_count = 0

    try:
    
        # 连接邮件服务器
        smtp_obj = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
        # 通过用户名和授权码登录
        smtp_obj.login(EMAIL_USER, EMAIL_AUTH)
        print('📧 SMTP服务器连接成功')

        for email_to in recipients:
            try:
                # 创建邮件对象
                email = MIMEMultipart()
                # 发件人
                email['From'] = EMAIL_USER
                # 收件人
                email['To'] = email_to
                # 邮件主题
                email['Subject'] = Header(subject, 'utf-8')

                # 添加邮件正文
                email.attach(MIMEText(content, 'plain', 'utf-8'))
                
                # 发送邮件
                smtp_obj.sendmail(
                    EMAIL_USER,
                    [email_to],
                    email.as_string()
                )
                success_count += 1
                print('✅ 简单文本邮件发送成功！')
            
            except Exception as e:
                # 单个发送失败不影响其他邮件
                fail_count += 1
                print(f'❌ 发送失败: {email_to}, 原因: {e}')
        smtp_obj.close()
        
        print('✅ 批量发送成功！')
    except Exception as e:
        print(f'❌ SMTP连接失败: {e}')
        return
    
    # 4️⃣ 打印统计信息
    print(f'\n📊 发送完成 - 成功: {success_count} 封, 失败: {fail_count} 封')

recipients = ['fanfan6066@gmail.com', 'fan1210326244@gmail.com']
send_bulk_emails(
    recipients,
    subject='批量测试邮件',
    content='这是批量发送的测试内容'
)

# **练习 3：带附件的邮件**

# 编写一个函数 `send_email_with_attachment(file_path)`，发送带附件的邮件：
# - 读取本地一个文件（如 PDF、图片或 Excel）作为附件
# - 使用 `MIMEBase` 和 `encoders.encode_base64` 处理附件
# - 设置附件的 `Content-Disposition` 头为 `'attachment'`
# - 邮件正文写一段说明文字，告知收件人附件内容

import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from urllib.parse import quote
from pathlib import Path


load_dotenv()

# 设置邮件服务器
EMAIL_HOST = 'smtp.qq.com'
# 设置邮件端口
EMAIL_PORT = 465
# 设置发件账号
EMAIL_USER = '1210326244@qq.com'
# 读取配置文件授权码
EMAIL_AUTH = os.getenv('QQ_EMAIL_AUTH')

def send_email_with_attachment(file_path):
    email = MIMEMultipart()

    email['From'] = EMAIL_USER
    email['To'] = '1210326244@qq.com'
    email['Subject'] = Header('Python学习资料 - 请查收附件', 'utf-8')
    # 邮件正文
    content = """<p>您好！</p>
<p>附件中是Python学习相关的文档资料，请查收。</p>
<p>如有问题，请随时联系。</p>
<br>
<p>祝学习愉快！</p>
<p>Python学习小组</p>"""

    email.attach(MIMEText(content, 'html', 'utf-8'))

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            attachment = MIMEText(f.read(), 'base64', 'utf-8')
            attachment['Content-Type'] = 'application/octet-stream'

            # 处理文件名（支持中文）
            filename = os.path.basename(file_path)
            filename = quote(filename)
            attachment['Content-Disposition'] = f'attachment; filename="{filename}"'

            email.attach(attachment)
            smtp_obj = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
            smtp_obj.login(EMAIL_USER, EMAIL_AUTH)
            smtp_obj.sendmail(EMAIL_USER, ['fanfan6066@gmail.com'], email.as_string())
            smtp_obj.close()

            print('✅ 带附件的邮件发送成功！')



file_path = Path(__file__).parent / 'XGBoost.pdf'
send_email_with_attachment(file_path)