import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))


def rename_images(directory):
    # 遍历目标目录下的所有子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 获取文件的完整路径
            file_path = os.path.join(root, file)
            # 获取文件的扩展名
            file_extension = os.path.splitext(file)[1]
            if file_extension.lower() in [".jpg", ".jpeg", ".png", ".gif"]:
                # 构造新的文件名
                new_file_path = os.path.join(root, f"avatar{file_extension}")
                # 重命名文件
                os.rename(file_path, new_file_path)
                print(f"Renamed '{file_path}' to '{new_file_path}'")


# 定义目标目录
target_directory = "content/authors"

# 调用函数
rename_images(os.path.join(cur_dir, "..", target_directory))
