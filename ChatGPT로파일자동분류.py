import os
import shutil

# 다운로드 폴더 경로
downloads_folder = r'C:\Users\student\Downloads'

# 대상 폴더 경로
target_folders = {
    "images": os.path.join(downloads_folder, "images"),
    "data": os.path.join(downloads_folder, "data"),
    "docs": os.path.join(downloads_folder, "docs"),
    "archive": os.path.join(downloads_folder, "archive"),
}

# 파일 확장자 분류
file_categories = {
    "images": ['.jpg', '.jpeg'],
    "data": ['.csv', '.xlsx'],
    "docs": ['.txt', '.doc', '.pdf'],
    "archive": ['.zip'],
}

# 폴더 생성
for folder in target_folders.values():
    os.makedirs(folder, exist_ok=True)

# 파일 이동
for file_name in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, file_name)
    
    # 파일이 아닌 경우 건너뛰기
    if not os.path.isfile(file_path):
        continue
    
    # 파일 확장자를 확인하고 이동
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()
    
    moved = False
    for category, extensions in file_categories.items():
        if ext in extensions:
            shutil.move(file_path, os.path.join(target_folders[category], file_name))
            moved = True
            break
    
    # 분류되지 않은 파일은 무시
    if not moved:
        print(f"Uncategorized file: {file_name}")

print("파일 정리가 완료되었습니다!")
