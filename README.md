# Selenium Python Web Automation

## Mô tả

Đây là một project kiểm thử tự động bằng **Selenium WebDriver** kết hợp với **unittest** framework trong Python. Project được thiết kế để tự động hóa việc tìm kiếm trên trang web [python.org](https://www.python.org) và kiểm tra xem kết quả có xuất hiện hay không. 

## Cấu trúc project

Project bao gồm các file chính sau:

1. **`element.py`**:
    - Định nghĩa lớp `BasePageElement`, sử dụng mô hình descriptor trong Python để thiết lập và lấy dữ liệu từ các thành phần HTML trên trang. Các phương thức chính:
      - `__set__`: Đặt giá trị cho một phần tử HTML dựa trên `locator`.
      - `__get__`: Lấy giá trị từ phần tử HTML đó.
    
2. **`locator.py`**:
    - Chứa các `locator` để xác định các phần tử HTML trên trang mà Selenium sẽ tương tác. Sử dụng `By` từ Selenium để xác định kiểu tìm kiếm.
    - Ví dụ:
      - `MainPageLocators.GO_BUTTON`: Xác định nút tìm kiếm trên trang chính.

3. **`page.py`**:
    - Tổ chức các lớp cho các trang chính và kết quả tìm kiếm của trang web. Các lớp này bao gồm:
      - `MainPage`: Chứa logic liên quan đến trang chính của python.org, gồm chức năng kiểm tra tiêu đề trang và nhấp vào nút tìm kiếm.
      - `SearchResultPage`: Kiểm tra xem có kết quả tìm kiếm nào không.

4. **`main.py`**:
    - Đây là file kiểm thử chính, sử dụng `unittest` framework để tổ chức các bài kiểm thử. Các phương thức chính:
      - `setUp`: Khởi tạo WebDriver và mở trang python.org.
      - `test_search_in_python_org`: Thực hiện tìm kiếm từ khóa "pycon" và kiểm tra kết quả.
      - `tearDown`: Đóng trình duyệt sau khi kiểm thử hoàn thành.

## Yêu cầu

- Python 3.x
- Selenium
- Chrome WebDriver (hoặc bất kỳ WebDriver nào bạn muốn sử dụng)

## Cài đặt

1. **Clone project**:

   ```bash
   git clone https://github.com/yourusername/selenium-python-automation.git

2. **Run**:

   ```bash
   python main.py hoặc bấm nút mũi tên run bên phải màn hình

3. **Result**:

  ```bash
   Ran 1 test in 5.764s
   OK
