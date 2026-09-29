from .user import UserRegistrationSerializer, UserSerializer
from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer,
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer,
    ItensCompraSerializer, 
)
from .editora import EditoraSerializer
from .livro import (
    LivroAlterarPrecoSerializer,
    LivroAjustarEstoqueSerializer,
    LivroListSerializer,
    LivroMaisVendidoSerializer,
    LivroRetrieveSerializer, 
    LivroSerializer,
)
