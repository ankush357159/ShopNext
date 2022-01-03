#Rest_framework imports
from rest_framework.response import Response
from rest_framework.decorators import api_view


#Local imports
from api.models import Product
from api.serializers import ProductSerializer

# Create a new Product (Without Image)
@api_view(['POST'])
def createProduct(request):
    user = request.user
    product = Product.objects.create(
        user = user,
        name = "Product Name",
        brand = "",
        category = "",
        description = "",
        price = 0,
        stock = 1
    )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

# Upload Image for Product
@api_view(['POST'])
def uploadImage(request):
    data = request.data
    product_id = data['product_id']
    product = Product.objects.get(_id = product_id)
    product.image = request.FILES.get('image')
    product.save()
    return Response("Image uploaded successfully")

# Get list of Products
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({'products':serializer.data})

# Get Product details
@api_view(['GET'])
def getProductDetails(request, pk):
    print(request)
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

    
   