# 说明

Python 版本：Python3

run.py 是一个 Python 脚本，用于将 Markdown 格式的文件转成成 Things URL Scheme 中的 JSON 格式，run.py 会默认转换同个目录下的 md.txt 文件，你只需把需要转换的内容存入该文件即可。转换案例可以参考 md.txt 文件。

markdown_to_things 是一个 macOS 中的 automator 文件，你可修改这个文件，将其中的 your_path 替换为你存放 run.py 的文件路径。通过 markdown_to_things 将会自动运行 run.py 文件，并将输出的 JSON 格式自动输入到 Things3 当中。

# 使用方法

在配置好 markdown_to_things 中的路径之后，你可通过 Spotlight Search 来快速启动 markdown_to_things，它将会自动根据 md.txt 在 Things 中创建项目。

# Markdown 格式说明

目前将会以一级标题作为项目名称在 Things 中创建项目，在 .txt 文件中，需要把一级标题放在首行。

```
# 一级标题：将作为项目名称
> 紧跟在一级标题下的引用样式，会被转换成项目描述
没有任何标记的段落会成为项目中的 todo list
* 星号也是项目中的 todo list
## 二级标题：会成为 heading
heading 下的 todo list
> 紧跟在 todo list 下的引用会成为 todo list 的描述
- 短横线的项目会成为 todo list 下的 checklist-item
- 可以添加多个
* 又一个 todo list 项目
> todo 的描述说明
```

⚠️ 我尚未尝试过同时创建多个项目
P.S. 你需要安装 Python3.2 以上版本的 Python
