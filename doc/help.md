当使用NVIDIA GeForce GTX 750 Ti显卡时，需要安装适用于该显卡的CUDA和cudnn版本。以下是安装步骤：

1. 安装CUDA：

   - 访问NVIDIA官方网站：https://developer.nvidia.com/cuda-toolkit-archive
   - 在CUDA Toolkit Archive页面上，找到适用于NVIDIA GeForce GTX 750 Ti显卡的CUDA版本。根据你的操作系统选择正确的版本，并下载安装程序。
   - 运行下载的安装程序，按照指示进行安装。在安装过程中，确保选择正确的安装路径和组件。
   - 安装完成后，将CUDA的安装路径添加到系统的环境变量中。默认情况下，CUDA的安装路径类似于`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vXX.X`，其中`vXX.X`是CUDA的版本号。

2. 安装cudnn：

   - 访问NVIDIA官方网站：https://developer.nvidia.com/rdp/cudnn-archive
   - 在cuDNN Archive页面上，找到与你安装的CUDA版本兼容的cudnn版本。确保选择适用于Windows操作系统的版本。
   - 下载对应版本的cudnn，需要注册NVIDIA开发者账号。
   - 下载完成后，解压缩cudnn压缩包，你会得到一个包含`bin`、`include`和`lib`文件夹的文件夹。
   - 将解压缩后的cudnn文件夹中的`bin`、`include`和`lib`文件夹中的内容复制到之前安装的CUDA的安装路径中对应的文件夹中，覆盖原有的文件。

3. 配置环境变量：

   - 在Windows上，右键点击“我的电脑”（或“此电脑”），选择“属性”。
   - 在左侧面板中，点击“高级系统设置”。
   - 在弹出的窗口中，点击“环境变量”按钮。
   - 在“系统变量”部分，找到名为“Path”的变量，并点击“编辑”按钮。
   - 在弹出的编辑窗口中，点击“新建”按钮，并将CUDA的安装路径添加进去（例如：`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vXX.X\bin`）。
   - 确认所有窗口，并重新启动Python环境。

完成以上步骤后，你应该已经正确安装了CUDA和cudnn。你可以尝试重新运行PaddleOCR的代码，看看是否还会出现cudnn相关的错误。

要确定适用于NVIDIA GeForce GTX 750 Ti显卡的CUDA版本，可以按照以下步骤进行：

1. 打开NVIDIA官方网站：https://developer.nvidia.com/cuda-gpus
2. 在页面上找到“CUDA-Enabled GeForce Products”部分。
3. 在该部分中，找到"NVIDIA GeForce GTX 750 Ti"显卡的名称。
4. 在该显卡名称下方的表格中，查找“CUDA Compute Capability”列。
5. 该列中的数值表示该显卡支持的CUDA版本。例如，如果该列中的数值为5.0，则表示该显卡支持CUDA 5.0版本。

根据上述步骤，你可以确定适用于NVIDIA GeForce GTX 750 Ti显卡的CUDA版本，并下载相应的CUDA安装程序进行安装。


如果你只是使用Python对接PaddleOCR的API，并不需要自己的环境安装CUDA。因为PaddleOCR的API已经将底层的CUDA和cuDNN等依赖项封装好了，你只需要安装PaddleOCR的Python包即可。

在使用PaddleOCR之前，你需要确保已经安装了Python和PaddlePaddle。可以通过以下步骤安装PaddleOCR：

1. 确保已经安装了Python 3.6+版本。你可以在命令行中运行`python --version`来检查Python的版本。
2. 安装PaddlePaddle。可以使用以下命令来安装最新版本的PaddlePaddle：

```shell
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
```

3. 安装PaddleOCR。可以使用以下命令来安装PaddleOCR：

```shell
pip install paddlepaddle paddleocr -i https://mirror.baidu.com/pypi/simple
```

安装完成后，你就可以使用PaddleOCR的API进行文字识别了，而无需自己安装CUDA和其他底层依赖项。


当然，下面是一个使用PaddleOCR进行文字识别的简单示例：

```python
import paddleocr

# 初始化PaddleOCR
ocr = paddleocr.OCR()

# 读取图像
image_path = 'path/to/your/image.jpg'
image = paddleocr.read_image(image_path)

# 进行文字识别
result = ocr.ocr(image)

# 打印识别结果
for line in result:
    line_text = ' '.join([word_info[1] for word_info in line])
    print(line_text)
```

在这个示例中，我们首先导入`paddleocr`模块，并初始化了一个OCR对象。然后，我们读取了一张图像，并使用OCR对象对图像进行文字识别。最后，我们遍历识别结果，并将每一行的文字拼接起来打印出来。

你可以将上述代码保存为一个Python文件，然后运行它来测试PaddleOCR的文字识别功能。记得将`image_path`替换为你自己的图像路径。