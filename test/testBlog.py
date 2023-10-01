import unittest
from unittest.mock import Mock, patch
from src.Blog import Blog

class TestBlog(unittest.TestCase):

    @patch('requests.get')
    def test_posts(self, mock_get):
        # Mock da resposta da API
        mock_response = Mock()
        mock_response.json.return_value = [
            {'userId': 1, 'id': 1, 'title': 'Titulo teste 1', 'body': 'Conteudo do blog 1'},
            {'userId': 2, 'id': 2, 'title': 'Titulo teste 2', 'body': 'Teste de conteudo do blog 2'}
        ]
        mock_get.return_value = mock_response

        # Instanciar a classe Blog
        blog = Blog()

        # Chamar o método posts
        result = blog.posts()

        # Verificar se a chamada para a API foi feita corretamente
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/posts")

        # Verificar se o resultado corresponde ao mock da resposta
        self.assertEqual(result, mock_response.json())

    @patch('requests.get')
    def test_post_by_user_id(self, mock_get):
        # Mock da resposta da API
        user_id = 1
        mock_response = Mock()
        mock_response.json.return_value = {
            'userId': user_id, 'id': 1, 'title': 'Titulo teste 1', 'body': 'Conteudo do blog 1'
        }
        mock_get.return_value = mock_response

        # Instanciar a classe Blog
        blog = Blog()

        # Chamar o método post_by_user_id
        result = blog.post_by_user_id(user_id)

        # Verificar se a chamada para a API foi feita corretamente
        mock_get.assert_called_once_with(f"https://jsonplaceholder.typicode.com/posts/{user_id}")

        # Verificar se o resultado corresponde ao mock da resposta
        self.assertEqual(result, mock_response.json())

if __name__ == '__main__':
    unittest.main()