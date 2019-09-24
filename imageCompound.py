# 需要先安装Pillow包： pip install Pillow
from PIL import Image

# 创建白色背景
background_img = Image.new('RGB', (640, 640), (255, 255, 255))
# 加载头像图片
head_img = Image.open('head.jpg')
# 加载红旗图片
red_flag_img = Image.open('flag.png')

# 修改头像图片大小(便于统一)
head = head_img.resize((600, 600), Image.ANTIALIAS)

# 在白色背景图上添加头像图片
background_img.paste(head, (20, 20, 620, 620))

# 可以先输出来看看当前的效果
# background_img.save('out.png')

# 调整红旗图片大小
red_flag = red_flag_img.resize((200, 200), Image.ANTIALIAS)

# 红旗放置区域
red_flag_box = (440, 440, 640, 640)

# 在添加了头像图片的白色背景图上添加红旗图片
background_img.paste(red_flag, red_flag_box, mask=red_flag)

# 保存图片
background_img.save('target.jpg')


