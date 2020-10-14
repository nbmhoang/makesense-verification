1. Cài đặt labelImg theo link: https://github.com/tzutalin/labelImg
1. Copy tất cả thư mục annotation vào thư mục __data__(mỗi thư mục bao gồm file ảnh + file xml tương ứng) như bên dưới
![Annotation Folder](/images/annotation_folder.jpg)
1. Chạy script: `python main.py`
1. Mở labelImg bằng command: `labelImg`
1. Chọn File > Open Dir và chọn 1 thư mục để verify
1. Chọn *Change Save Dir* ở thanh công cụ bên trái và chọn lại đúng thư mục ở trên(Không được bỏ qua bước này, nếu không sẽ lưu nhầm folder)
![Annotation Folder](/images/change_save_dir.jpg)
1. Chỉnh sửa label(nếu có) bằng cách click chuột phải vào khung hình và chọn Edit label. Nhấn Ctrl + S để lưu, D để tiếp tục ảnh tiếp theo và A để quay lại ảnh trước đó.
![Annotation Folder](/images/edit_label.jpg)