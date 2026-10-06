# FORM · 人体绘画参考工具

面向绘画练习的浏览器 3D 人体姿势与透视参考工具。

[在线使用](https://form-study-atelier.fqxxzyw.chatgpt.site) · [完整功能与开发文档](docs/DEVELOPMENT.md)

## 功能

- 四种显示模式：动态线、几何体、完整人体、轮廓线稿。
- 男女模型、15 个姿势预设、关节角度调整、手脚 IK 和左右镜像。
- 单视图、四级并排或网格，支持同步或独立姿势。
- 透视和正交投影，相机角度、距离、焦距与灯光调整。
- 导出前预览；选择当前镜头的局部构图或自动全身取景。
- 单张或四种模式拼图，支持白色、场景和透明背景 PNG。
- 导出长边 1920、2560 或 3840 px；姿势项目保存和载入 JSON。

## 本地运行

需要 Python 3。在项目目录运行：

```bash
python setup_resources.py
python -m http.server 8000 --directory dist
```

打开 http://localhost:8000 。首次运行 setup_resources.py 会在本地解包 Three.js 和模型，无需联网下载资源。无需 npm 安装或构建。请通过 HTTP 访问，不要直接双击 HTML 文件。

## 操作

| 操作 | 方法 |
| --- | --- |
| 旋转视角 | 在空白处左键拖动 |
| 平移视角 | 右键拖动 |
| 缩放 | 滚轮或双指缩放 |
| 调整姿势 | 拖动关节点，或右侧修改角度 |
| 切换模式 | 底部按钮或数字 1–4 |
| 撤销 / 重做 | Ctrl Z / Ctrl Shift Z |
| 保存 / 恢复项目 | 保存姿势 / 载入姿势 |

导出选择“当前镜头”会保留当前缩放、平移和画幅比例，允许只导出头部、上半身或镜头内的其他部分。“完整身体”保持方向并自动重新取景。导出图片不包含关节点和操作控件。

## 文件结构

```text
dist/
  index.html       界面
  style.css        样式
  app.js           姿势、渲染与导出逻辑
  vendor/          Three.js 和加载器
  models/          人体模型与授权说明
resources/        分块压缩的第三方资源
setup_resources.py  校验并还原资源
CHANGELOG.md       更新记录
```

## 模型及第三方授权

- 女性：VRoid AvatarSample_A，版权属于 pixiv / VRoid Project，非 CC0。
- 男性：VRoid HairSample_Male，源模型元数据标注 CC0。
- 来源及女性模型使用条件见 [模型说明](dist/models/NOTICE.txt)。发布、修改或再分发时应分别遵守各资产的条件。
- Three.js 使用 MIT 许可，见 [许可证](dist/vendor/LICENSE)。第三方许可不代表整个项目或所有模型均为 MIT / CC0。

## 当前限制

关节编辑采用角度范围和简化的手臂避让，不是完整的人体碰撞或生物力学求解器。极端姿势仍可能出现穿模。线稿从三维模型的深度、法线和脸部纹理提取，细节取决于模型。项目文件保存在本地，不提供账号或云端同步。
