from .user import UserRegistrationSerializer, UserSerializer
from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .compra import (
    CompraSerializer,
    CompraCreateUpdateSerializer, 
    ItensCompraSerializer, 
    ItensCompraCreateUpdateSerializer,
)
from .editora import EditoraSerializer
from .livro import (
    LivroListSerializer,
    LivroRetrieveSerializer, 
    LivroSerializer,
)
