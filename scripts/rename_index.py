import os

def rename_index_files(directory):
    # 遍历目标目录下的所有子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查是否是index.md文件
            if file == "index.md":
                # 获取文件的完整路径
                old_path = os.path.join(root, file)
                # 构造新路径
                new_path = os.path.join(root, "_index.md")
                # 重命名文件
                os.rename(old_path, new_path)
                print(f"Renamed '{old_path}' to '{new_path}'")

# 使用示例
if __name__ == "__main__":
    authors_dir = "content/authors"
    rename_index_files(authors_dir)
