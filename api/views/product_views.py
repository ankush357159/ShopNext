#Django imports
from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
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

# Get list of Products with query
@api_view(['GET'])
def getProducts(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''
    products = Product.objects.filter(name__icontains=query).order_by('-_id') #name__icontains -> Case-insensitive containment test.
    page = request.query_params.get('page')
    paginator = Paginator(products, 8)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if page == None:
        page = 1
    page = int(page)

    serializer = ProductSerializer(products, many=True)
    return Response({'products':serializer.data, 'page':page, 'pages':paginator.num_pages})

# Get Product details
@api_view(['GET'])
def getProductDetails(request, pk):
    print(request)
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

# Get Top rated Products
@api_view(['GET'])
def getTopRatedProducts(request):
    product = Product.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


# Update Product
@api_view(['PUT'])
def updateProduct(request, pk):
    data = request.data
    # print("Data:",data)
    product = Product.objects.get(_id=pk)
    product.name = data["name"]
    product.price = data["price"]
    product.brand = data["brand"]
    product.stock = data["stock"]
    product.category = data["category"]
    product.description = data["description"]

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
    # For api testing, all fields need to be passed even if only one field is required  # to be changed.

# Delete a Product
@api_view(['DELETE'])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response("Product deleted successfully")







    
   