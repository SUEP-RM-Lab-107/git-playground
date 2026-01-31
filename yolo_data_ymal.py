import os
import shutil
from pathlib import Path
import random

# === 配置 ===
ROOT = Path(r"/home/ubuntu/图片/rendar_numyolo/RM2025-Armor-Public-Dataset")
TRAIN_RATIO = 0.8  # 80% 训练，20% 验证

# 创建目标目录
(TRAIN_IMG := ROOT / "train" / "images").mkdir(parents=True, exist_ok=True)
(TRAIN_LBL := ROOT / "train" / "labels").mkdir(parents=True, exist_ok=True)
(VAL_IMG := ROOT / "val" / "images").mkdir(parents=True, exist_ok=True)
(VAL_LBL := ROOT / "val" / "labels").mkdir(parents=True, exist_ok=True)

# 获取所有图像文件（假设是 .jpg）
image_files = sorted(ROOT.glob("*.jpg"))  # 会匹配 0000.jpg, 0001.jpg, ..., 2999.jpg
print(f"找到 {len(image_files)} 张图像")

# 随机打乱并划分
random.seed(42)  # 固定随机种子，确保可复现
random.shuffle(image_files)

split_idx = int(len(image_files) * TRAIN_RATIO)
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

print(f"训练集: {len(train_files)} 张")
print(f"验证集: {len(val_files)} 张")

# 移动文件
def move_files(file_list, img_dst, lbl_dst):
    for img_path in file_list:
        # 移动图像
        shutil.move(str(img_path), str(img_dst / img_path.name))
        # 移动对应的 .txt 标签
        lbl_path = img_path.with_suffix('.txt')
        if lbl_path.exists():
            shutil.move(str(lbl_path), str(lbl_dst / lbl_path.name))
        else:
            print(f"警告: 标签缺失 {lbl_path}")

move_files(train_files, TRAIN_IMG, TRAIN_LBL)
move_files(val_files, VAL_IMG, VAL_LBL)

# 生成 data.yaml
data_yaml = f"""path: /home/ubuntu/图片/rendar_numyolo/RM2025-Armor-Public-Dataset
train: train/images
val: val/images

nc: 1
names: ["B1", "B2", "B3", "B4", "B7", "R1", "R2", "R3", "R4", "R7", "G1", "G2", "G3", "G4", "G7"]
"""

with open(ROOT / "data.yaml", "w", encoding="utf-8") as f:
    f.write(data_yaml)

print("\n✅ 数据集已整理完成！")
print("📁 目录结构:")
print(f"  ├── train/images/ ({len(train_files)} images)")
print(f"  ├── train/labels/ ({len(train_files)} labels)")
print(f"  ├── val/images/ ({len(val_files)} images)")
print(f"  └── val/labels/ ({len(val_files)} labels)")
print("\n📄 配置文件已保存为: data.yaml")