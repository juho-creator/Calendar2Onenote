[![返回主页](https://img.shields.io/badge/返回主页-blueviolet.svg)](https://github.com/juho-creator/Calendar2Onenote/blob/main/README.CH.md)


# Calendar2Onenote

**概览:** Calendar2Onenote 是一个旨在根据 Google 日历事件在 OneNote 中创建日程安排的程序。
<br><br>

## 演示视频（无 GUI）
[![观看演示视频](https://img.youtube.com/vi/kQ-CY51pwEo/0.jpg)](https://www.youtube.com/watch?v=kQ-CY51pwEo)

<!-- 如果适用，请在此添加演示内容 -->
<br><br>

## 使用方法

### 首次设置

1. **下载**: 从[下载链接](https://github.com/juho-creator/OneNoteSyncScheduler/releases)获取 Calendar2Onenote 和 Credentials.json，并将它们放在同一文件夹中。

2. **运行**: 下载后，双击 Calendar2Onenote 应用程序以运行它。

3. **Microsoft 登录**: 粘贴自动复制的代码并使用您的 Microsoft 帐户登录

4. **同步 OneNote**: 授权访问 OneNote。

5. **Google 登录**: 登录到您的 Google 帐户。

6. **同步 Google 日历**: 授权访问以获取 Google 日历事件。

7. **生成调度程序**: 在终端中输入目标年份以创建一个带有 12 个月份部分的 OneNote 笔记本，自动组织事件。 这需要 5-10 分钟。
<br>

### 后续使用（已登录时）

1. **运行**: 双击 Calendar2Onenote 可执行文件。

2. **生成调度程序**: 输入目标年份以创建一个带有 12 个月份部分的 OneNote 笔记本。 事件将自动按日期在相应的部分中组织。
<br><br>

## 认证和 API 流程图
### 第 1 步. Google OAuth2.0 和 Google 日历 API (G_OAuth.py)
- **文档**: [Google OAuth2.0 文档](https://developers.google.com/workspace/guides/auth-overview?hl=ko), [Google 日历 API 文档](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
<br>![Google OAuth2.0 流程图](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/26717732-7e98-4da7-b845-eebff57423e6)

- **过程**:
  - Google OAuth2.0 对 Google 帐户用户进行身份验证，无需 Calendar2Onenote 需要用户凭据。 （使用 **token.json**）
  - 一旦用户授权访问其 Google 日历事件，Calendar2Onenote 就可以使用 Google 日历 API 获取用户日历事件。 <br><br><br><br>






### 第 2 步. Microsoft OAuth2.0 和 Microsoft Graph API (M_OAuth.py, OneNote.py)
- **文档**: [Microsoft 帐户认证和 Microsoft Graph API 文档](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-authentication-flows)
<br>![Microsoft 帐户认证和 Microsoft Graph API 流程图](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/e1df5d9b-e7e4-4e8f-8bba-fb4b8e718fab)

- **过程**:
  - Microsoft OAuth2.0 对 Microsoft（Onenote）帐户用户进行身份验证，无需 Calendar2Onenote 需要用户凭据（使用 **api_token_access.json**）
  - 一旦用户授权访问其 Onenote，Calendar2Onenote 就被授予创建 a Onenote 笔记本的权限。
  - Calendar2Onenote 现在可以使用 Microsoft Graph API <br><br><br><br>
    


### 第 3 步. OneNote API 开发堆栈 <br>
- **文档**: [OneNote REST API 文档](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview?view=graph-rest-1.0) <br>
![image](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/df597c54-752f-44ed-9967-abe356bb24c2)
- 在认证和授权过程之后，Calendar2Onenote 使用 Onenote API 创建一个带有 Google 日历事件的 OneNote 笔记本，该 API 是 Microsoft Graph API 的一部分。 <br>
<br><br>

## 使用的技术 
  
- **Google 日历 API**: 
  - **文档**: [Google 日历 API](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
  - **模块**: `G_OAuth.py`
  - **功能**: 为获取用户日历事件对 Google 帐户进行身份验证。
  
- **Microsoft Authentication Library (MSAL)**: 
  - **文档**: [Microsoft Authentication Library (MSAL)](https://github.com/AzureAD/microsoft-authentication-library-for-python)
  - **模块**: `M_OAuth.py`
  - **功能**: 为 Onenote 对 Microsoft 帐户进行身份验证。


  
- **Microsoft Graph API**: 
  - **教程**: [Microsoft Graph API](https://www.youtube.com/watch?v=AjOfAQCZsJU&list=PL3JVwFmb_BnT9Ti0MMRj5nPF7XoN-4MQx&index=2)
  - **模块**: `OneNote.py`
  - **功能**: 使用 Google 日历事件创建 OneNote 笔记本。

<br><br>

## 参考

### 开始使用 Google API

- 视频教程: [点击此处观看](https://www.youtube.com/watch?v=I5ili_1G0Vk)

### Google 日历 API

- 教程系列: [点击此处观看](https://www.youtube.com/watch?v=1JkKtGFnua8&list=PL3JVwFmb_BnTO_sppfTh3VkPhfDWRY5on)
- 文档: [点击此处阅读](https://developers.google.com/calendar/api/quickstart/python)

### Microsoft Azure

- 教程系列: [点击此处观看](https://www.youtube.com/watch?v=BErur8WwAsg&list=PL3JVwFmb_BnQ8zwvN4OmP-fYpwJXg47Z6)

### Microsoft Graph API

- 教程系列: [点击此处观看](https://www.youtube.com/watch?v=7ywUs54eGBo&list=PL3JVwFmb_BnT9Ti0MMRj5nPF7XoN-4MQx)
- 尝试 Microsoft Graph : [点击此处观看](https://developer.microsoft.com/en-us/graph/graph-explorer)

### 使用 Microsoft Graph Explorer 进行 Onenote API 测试

- 教程: [点击此处观看](https://www.youtube.com/watch?v=VXd4OeQU1ek)

### Onenote API 文档

- [了解更多](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview?view=graph-rest-1.0)
