import pytest
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_400(client):
        client = APIClient()
        response = client.post("/store/collections/", data={"title": "a"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(client):
        client = APIClient()
        """
        force_authenticate là một phương thức của APIClient trong Django REST Framework.
         - Nó dùng để "ép buộc" client được xác thực (authenticated) với một user cụ thể mà không cần qua quá trình login thật (như gửi username/password).
         - user={}: Ở đây, thay vì truyền một đối tượng User thực sự (ví dụ: User.objects.create()), người viết truyền một dictionary rỗng {}. Điều này có nghĩa là client được "xác thực" với một user không hợp lệ hoặc không có thật (không có thông tin gì cả).
         Ý nghĩa: Dòng này mô phỏng một tình huống mà request được gửi từ một user không có quyền hoặc không được xác thực đầy đủ. Nó kiểm tra xem API có từ chối request từ user "giả" này không.
        """
        client.force_authenticate(user={})
        response = client.post("/store/collections/", data={"title": "a"})
        assert response.status_code == status.HTTP_403_FORBIDDEN
